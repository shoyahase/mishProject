import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

# .envファイルから環境変数を読み込む
load_dotenv()

# APIキーを設定
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEYが.envファイルに設定されていません。")
genai.configure(api_key=api_key)

# --- 変更点：v1beta APIで利用可能なモデル名に修正 ---
# google-generativeaiライブラリはv1betaエンドポイントを呼び出すため、
# それに対応したプレビュー版のモデル名を指定する必要があります。
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

def get_gemini_response(prompt: str, length_request: str = "300文字程度") -> str:
    """
    指定された状況に基づき、文字起こし練習用のモノローグ形式の文章を生成します。
    出力は句点区切りで、改行を含まない単一のパラグラフになるように指示します。
    """
    
    # Geminiへの指示をより詳細に定義したプロンプト
    prompt_for_script = f"""あなたは、文字起こし練習アプリのシナリオライターです。
以下の指示に従って、一人の人物が話している形式（モノローグ）の練習用文章を生成してください。

# 指示
- **状況**: {prompt}
- **文字数**: {length_request}

# 形式の制約 (非常に重要)
- 文章はすべて句点「。」で区切ってください。疑問符「？」や感嘆符「！」は使用しないでください。
- 改行は絶対に使用せず、全ての文章を一つのパラグラフとして出力してください。
- 話者名（例：「話者１：」）や括弧は含めないでください。

# 文章生成開始
"""

    try:
        response = model.generate_content(prompt_for_script)
        # 念のため、AIが誤って追加した可能性のある改行や不要な空白を削除する
        cleaned_text = response.text.replace("\n", "").strip()
        return cleaned_text
    except Exception as e:
        print(f"文章生成中にエラーが発生しました: {e}")
        return "エラーのため文章を生成できませんでした。"
    
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
    