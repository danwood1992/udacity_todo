FROM ubuntu:22.04

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    python3.10 \
    python3-pip \
    python3.10-venv \
    python3.10-dev \
    build-essential \
    libpq-dev \
    gcc \
    wget \
    autoconf \
    automake \
    pkg-config \
    libtool \
    procps

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./compose/api/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/api/start /start
RUN chmod +x /start

WORKDIR /opt/udado

ENTRYPOINT [ "/entrypoint" ]