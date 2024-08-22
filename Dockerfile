FROM python:3.12

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl gnupg2 apt-transport-https cron

# Clean up to reduce the image size
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /floridayvine

COPY . /floridayvine/

RUN pip install --upgrade pip setuptools wheel setuptools_scm
RUN pip install --no-cache-dir --upgrade .

RUN touch /var/log/cron.log

CMD floridayvine about \
    && echo "Started floriday-vine container." \
    && printenv > /etc/environment \
    && cron \
    && tail -f /var/log/cron.log
