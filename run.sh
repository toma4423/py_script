#!/bin/bash

# 仮想環境が存在するか確認
if [ ! -d "pyscript_env" ]; then
    echo "仮想環境を作成しています..."
    python -m venv pyscript_env
fi

# 仮想環境をアクティベート
source pyscript_env/bin/activate

# 依存関係をインストール
echo "依存関係をインストールしています..."
pip install -r requirements.txt

# FastAPIアプリケーションを実行
echo "FastAPIアプリケーションを起動しています..."
cd src
uvicorn main:app --reload --host 127.0.0.1 --port 8000

# 終了時に仮想環境を非アクティベート
deactivate 