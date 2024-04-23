FROM python:3.10.12-slim

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH" \
    POETRY_VERSION="1.8"

EXPOSE 8000
WORKDIR /creonit-test
COPY poetry.lock pyproject.toml /creonit-test/

RUN pip install --upgrade --no-cache-dir pip==24.0 && \
    pip install -U --no-cache-dir poetry==$POETRY_VERSION && \
    python -m venv $VIRTUAL_ENV && \
    poetry install --no-root --no-interaction

COPY . /creonit-test/
COPY env.example .env

RUN chmod a+x /creonit-test/entrypoint.sh
ENTRYPOINT ["/creonit-test/entrypoint.sh"]

RUN useradd -ms /bin/bash dockeruser
USER dockeruser

CMD ["poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
