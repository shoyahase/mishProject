import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

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
    
def get_gemini_scoring(correct_answer, user_input):
    
    scoring_prompt = f"""あなたは文字起こしアプリの採点アシスタントです。
以下の採点基準とテキストに基づいて、ユーザーの入力を評価してください。

# 採点基準
- 句読点や誤字脱字、内容の過不足を考慮してください。
- 完全に一致していれば100点です。
- 少しの間違いなら減点し、内容が大きく異なる場合は0点に近づけてください。
- 必ず採点結果をJSON形式で返してください。例: {{"score": 85, "advice": "「〇〇」が抜けています。"}}

# テキスト
- 模範解答: "{correct_answer}"
- ユーザーの入力: "{user_input}"

# 採点結果 (JSON形式)
"""

    try:
        # Gemini APIを呼び出す
        response = model.generate_content(scoring_prompt)
        
        # 返ってきたテキストからJSON部分を抽出する
        json_response_text = response.text.strip().replace("```json", "").replace("```", "")
        
        # JSON文字列をPythonの辞書に変換する
        result = json.loads(json_response_text)
        
        # 'score'と'advice'がなければデフォルト値を設定
        result.setdefault('score', 0)
        result.setdefault('advice', '採点できませんでした。')
        
        return result

    except Exception as e:
        print(f"採点中にエラーが発生しました: {e}")
        # エラー時も決まった形式の辞書を返す
        return {"score": 0, "advice": "エラーのため採点できませんでした。"}
    