# ベースとなるイメージを指定
FROM python:3.12-slim
# uv をインストール
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 必要な依存関係をインストール、不要なファイルを削除
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y make git && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app /venv

ENV UV_PROJECT_ENVIRONMENT="/venv"
ENV PATH="$UV_PROJECT_ENVIRONMENT/bin:$PATH"

WORKDIR /app/

COPY ./README.md ./pyproject.toml ./uv.lock* /app/
RUN uv sync

CMD ["make", "run"]
