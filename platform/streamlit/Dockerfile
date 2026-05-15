FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock /tmp/

RUN pip install --no-cache-dir uv && \
    cd /tmp && \
    uv sync --frozen

ENV PATH="/tmp/.venv/bin:$PATH"

COPY platform/streamlit/app.py /app/app.py

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]