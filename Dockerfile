FROM python:3.11-slim as builder

RUN pip install poetry
RUN mkdir -p /app
COPY . /app

WORKDIR /app
RUN poetry install

FROM python:3.11-slim as base

WORKDIR /app
COPY --from=builder /app /app

RUN addgroup --system --gid 1001 nonroot && \
  useradd --uid 1001 -g nonroot nonroot && \
  chown -R nonroot:nonroot /app
USER nonroot

ENV PORT 8000
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE $PORT
CMD ["faker-events", "-n", "5", "-s", "src/generator.py"]