# FastAPI プロジェクト

このプロジェクトはFastAPIを使用したWebアプリケーションのテンプレートです。

Julesを使って作成しています。

## セットアップ方法

1. 仮想環境の作成と有効化:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

2. 依存関係のインストール:
```bash
pip install -r requirements.txt
```

## アプリケーションの起動

以下のコマンドでアプリケーションを起動できます：

```bash
uvicorn main:app --reload
```

アプリケーションは http://localhost:8000 でアクセス可能です。

## API ドキュメント

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 利用可能なエンドポイント

- GET /: ウェルカムメッセージ
- GET /health: ヘルスチェック 