FROM python:3.12.1-alpine3.19

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /reminder

RUN adduser \
    --disabled-password \
    appuser

RUN apk add postgresql-client postgresql-dev build-base
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

COPY --chown=appuser:appuser . .

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
