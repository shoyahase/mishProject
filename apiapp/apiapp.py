import os
import google.generativeai as genai
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# APIキーを設定
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Geminiモデルを初期化
# 現在推奨されているモデル名に変更
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def get_gemini_response(prompt: str) -> str:
    """
    Gemini APIにプロンプトを送信し、応答を返す関数
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # エラーハンドリング
        print(f"An error occurred: {e}")
        return "エラーが発生しました。しばらくしてから再度お試しください。"