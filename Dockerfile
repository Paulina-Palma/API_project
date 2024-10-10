# Use Python 3.12 base image
FROM python:3.12

# Create directory for the source code
RUN mkdir /src

# Copy the source code into the container
COPY ./src /src

# Copy docker-entrypoint.sh into the root of the container
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

# Update package lists and install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /src

# Set the PYTHONPATH and PWD environment variables
ENV PYTHONPATH="/src" \
    PWD="/src"

# Make docker-entrypoint.sh executable
RUN chmod +x /docker-entrypoint.sh

# Install Poetry (using pip from the base Python image)
RUN pip3 install poetry

# Configure Poetry to avoid creating virtual environments
RUN poetry config virtualenvs.create false

# Install only the main dependencies from the poetry.lock file
RUN poetry install --only main

# Use JSON format for CMD
CMD ["./docker-entrypoint.sh"]
