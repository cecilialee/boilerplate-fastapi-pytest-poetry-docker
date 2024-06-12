################################
# BASE LAYER
# Set shared dependencies for the builder and runtime layers
################################

FROM python:3.12.3-slim AS base

# Enable Python timely log messages without buffer
ENV PYTHONUNBUFFERED=1

# Disable pip version check and upgrade warning
ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
# Enable longer timeout for Poery installation
    PIP_DEFAULT_TIMEOUT=100 

# Set Poetry development mode
ARG DEV=false
# Set Poetry location of virtual environment
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

################################
# BUILDER LAYER
# Build dependencies and install virtual environment
################################

FROM base AS builder

# Disable Poetry interactive questions
ENV POETRY_NO_INTERACTION=1 \
# Create the virtualenv inside the project’s root directory in /app/.venv
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
# Create a new virtual environment if one doesn’t already exist
    POETRY_VIRTUALENVS_CREATE=1 

WORKDIR /app

# Install Poetry
RUN pip install poetry==1.8.3

# Install package dependencies
COPY pyproject.toml poetry.lock ./
RUN if [ $DEV ]; then \
        poetry install --with dev --no-root && rm -rf $POETRY_CACHE_DIR; \
    else \
        poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR; \
    fi

################################
# RUNTIME LAYER
# Final image used for runtime
################################

FROM base AS runtime

# Copy the built virtual environment from builder stage 
# to a bare python runtime image to keep the final image lean
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Copy source codes
COPY app ./app

# Run application
CMD ["fastapi", "run", "app/main.py", "--port", "80"]