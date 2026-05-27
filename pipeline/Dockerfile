FROM python:3.13.13-slim
# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# RUN pip install pandas pyarrow
WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

# Copy from host to docker image
COPY pipeline.py .

ENTRYPOINT ["python", "pipeline.py"]