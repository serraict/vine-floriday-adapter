FROM python:3.12

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl gnupg2 apt-transport-https

# Clean up to reduce the image size
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /floridayvine

COPY . /floridayvine/

RUN pip install --upgrade pip setuptools wheel setuptools_scm
RUN pip install --no-cache-dir --upgrade .
