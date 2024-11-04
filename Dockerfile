# ベースイメージ
FROM python:3.10-slim

# 作業ディレクトリの設定
WORKDIR /app

# Poetryのインストール
RUN pip install poetry

# Poetryの設定（仮想環境を無効化して、依存関係をグローバルにインストールする）
RUN poetry config virtualenvs.create false

# 依存関係ファイルをコピー
COPY pyproject.toml poetry.lock ./

# 依存関係をインストール
RUN poetry install --no-root

# アプリケーションコードをコピー
COPY . .

# アプリケーションの起動コマンド
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
