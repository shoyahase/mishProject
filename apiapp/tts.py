import os
from gtts import gTTS # ★★★ gTTSをインポート ★★★
from io import BytesIO # メモリ内でバイナリデータを扱うため

import re

def generate_mp3_from_text(text: str, filename: str, output_dir: str) -> str:
    """
    指定されたテキストからMP3音声を生成し、指定されたディレクトリに保存する関数。
    """

    if not text.strip(): # 空白文字のみのテキストは処理しない
        print("警告: 空または空白のみのテキストの音声生成はスキップされました。")
        return None


    tts = gTTS(text=text, lang='ja', slow=False) # lang='ja'で日本語を指定
    
    # ファイルのフルパスを構築
    file_path = os.path.join(output_dir, filename)
    
    try:
        # MP3ファイルを保存
        tts.save(file_path)
        print(f"音声ファイルを生成しました: {file_path}")
        return filename # 保存したファイル名を返す
    except Exception as e:
        print(f"音声生成または保存中にエラーが発生しました: {e}")
        return None # エラー時はNoneを返す

def split_text_by_punctuation(text: str) -> list[str]:
    """
    テキストを句点（。！？）で分割し、句点を含むフレーズのリストを返す。
    例: "こんにちは。元気ですか？はい！" -> ["こんにちは。", "元気ですか？", "はい！"]
    """
    # 句点ごとに分割し、句点自体もフレーズに含める
    # re.splitは句点の直前で分割し、(?!$)で句点が文字列の末尾でないことを確認
    # re.findallは句点を含むグループを抽出
    
    # 正規表現パターン: 句点(。！？)の後に続く(改行を含む)空白文字の0個以上の繰り返し
    # (?:...) は非キャプチャグループ
    phrases = re.findall(r'[^。！？]+(?:[。！？]|\n|$)', text)
    
    # 各フレーズから前後の空白を除去し、空のフレーズを除外
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]
    
    return phrases
