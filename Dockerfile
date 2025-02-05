FROM python:3.12-slim

WORKDIR /src

# Install system dependencies
RUN apt-get update \
    && apt-get install -y postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry==1.7.1
RUN poetry config virtualenvs.create false

# Copy the entire src directory first
COPY src/ /src/

# Install dependencies
RUN cd /src && poetry install --no-interaction --no-ansi --no-root

# Make entrypoint executable
RUN chmod +x /src/docker-entrypoint.sh

ENTRYPOINT ["/src/docker-entrypoint.sh"]
