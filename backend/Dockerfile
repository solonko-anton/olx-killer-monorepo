FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:${PATH}"
ENV PYTHONPATH="/code:${PYTHONPATH}"


RUN apt-get update && \
    apt-get install -y --no-install-recommends gettext && \
    python3 -m pip install --no-cache-dir pipx && \
    python3 -m pipx install poetry && \
    poetry config virtualenvs.create false && \
    apt-get remove --purge -y && \
    apt-get autoremove --purge -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache/*

WORKDIR /code

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi && rm -rf /root/.cache/*

COPY . .
