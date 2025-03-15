"""
PyScript学習プロジェクト用FastAPIアプリケーション

このスクリプトは、PyScriptの学習用HTMLファイルを提供するためのFastAPIアプリケーションです。
ローカル開発環境でPyScriptの例を試すことができます。JavaScriptを使わずにPythonのみで
インタラクティブなWebアプリケーションを構築することを目的としています。
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from pathlib import Path

# プロジェクトのルートディレクトリを取得
BASE_DIR = Path(__file__).resolve().parent.parent

# FastAPIアプリケーションの作成
app = FastAPI(
    title="PyScript学習プロジェクト",
    description="PyScriptを使用してブラウザ上でPythonコードを実行する方法を学ぶためのアプリケーション",
    version="1.0.0"
)

# 静的ファイルのマウント
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# テンプレートの設定
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    トップページを表示する関数
    
    Args:
        request: FastAPIのリクエストオブジェクト
    
    Returns:
        HTMLResponse: レンダリングされたHTMLページ
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/advanced", response_class=HTMLResponse)
async def advanced(request: Request):
    """
    高度な例のページを表示する関数
    
    Args:
        request: FastAPIのリクエストオブジェクト
    
    Returns:
        HTMLResponse: レンダリングされたHTMLページ
    """
    return templates.TemplateResponse("advanced.html", {"request": request})

@app.get("/resources", response_class=HTMLResponse)
async def resources(request: Request):
    """
    学習リソースのページを表示する関数
    
    Args:
        request: FastAPIのリクエストオブジェクト
    
    Returns:
        HTMLResponse: レンダリングされたHTMLページ
    """
    return templates.TemplateResponse("resources.html", {"request": request})

# APIエンドポイントの例（PyScriptから呼び出し可能）
@app.get("/api/hello")
async def hello():
    """
    簡単なAPIエンドポイントの例
    
    Returns:
        dict: JSONレスポンス
    """
    return {"message": "こんにちは、PyScriptとFastAPIの世界へようこそ！"}

# サーバー起動用のコード
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True) 