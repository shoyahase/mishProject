import os
from gtts import gTTS # ★★★ gTTSをインポート ★★★
from io import BytesIO # メモリ内でバイナリデータを扱うため


def generate_mp3_from_text(text: str, filename: str, output_dir: str) -> str:
    """
    指定されたテキストからMP3音声を生成し、指定されたディレクトリに保存する関数。
    """
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

