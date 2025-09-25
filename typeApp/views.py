from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from datetime import datetime
from zoneinfo import ZoneInfo
# Create your views here.

from .forms import TranscriptionForm

from apiapp.apiapp import get_gemini_scoring

import uuid
import os
from django.conf import settings

from apiapp.tts import generate_mp3_from_text

class TopView(View):
    def get(self, request):
        date = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y年%m月%d日 %H:%M:%S")

        return render(request, "typeApp/top.html", {"date": date})
    
top = TopView.as_view()

class PracticeView(View):
    def get(self, request):

        correct_answer = request.session.get("correct_answer", '')
        user_prompt = request.session.get('user_prompt', "")

        # #音声データを取得.とりあえず固定ファイルを静的に取得
        # audio_file_path = "typeApp/audio/audio.mp3" 

        #ユニークな音声ファイル名を作成
        audio_filename = f"audio_{uuid.uuid4().hex}.mp3"
        #正解テキスト
        text_to_synthesize = correct_answer

        # #ここ仮
        # # 仮の音声生成関数 (実際にはTTS APIを呼び出す)
        # #今は仮で、
        # def generate_audio_from_text(text, filename):
        #     # 例: テキストを基にしたダミーのMP3ファイルを作成
        #     # 実際には、TTS APIを呼び出し、そのレスポンスをファイルに書き込む
        #     with open(os.path.join(settings.MEDIA_ROOT, filename), 'wb') as f:
        #         # ここに音声データを書き込む
        #         f.write(b'DUMMY_MP3_DATA_FOR_' + text.encode('utf-8')) # ダミーデータ
        #     return filename


        # 音声データを生成し、MEDIA_ROOTに保存
        generate_mp3_from_text(text_to_synthesize, audio_filename, settings.MEDIA_ROOT)

        # 保存したファイルの相対URLを生成 (MEDIA_URLを利用)
        returned_filename = os.path.join(settings.MEDIA_URL, audio_filename)


        # 音声生成に失敗した場合はエラー処理（例: デフォルト音声やエラーメッセージ）
        if returned_filename is None:
            # エラー処理。例: デフォルトの音声URLにするか、エラーページにリダイレクト
            audio_url = os.path.join(settings.MEDIA_URL, "typeApp/audio/audio.mp3") # デフォルト音声の例
            print("音声ファイルの生成に失敗しました。デフォルト音声を使用します。")
            # この場合、セッションに削除対象を保存しない
        else:
            print("elseの方だよ")
            # 保存したファイルの相対URLを生成 (MEDIA_URLを利用)
            audio_url = os.path.join(settings.MEDIA_URL, returned_filename)
            # 結果Viewで削除するから保存した音声ファイルの相対パスをセッションに保存しておく。
            request.session['temp_audio_file_to_delete'] = audio_url

            print("audio_url",audio_url)


        form = TranscriptionForm()


        context = {"correct_answer":correct_answer,
                   "user_prompt": user_prompt,
                   "form": form,
                   "audio_file_path": audio_url,
                   }

        return render(request, "typeApp/practice.html", context)
    
practice = PracticeView.as_view()



class ResultView(View):
    def post(self, request):

        user_input = request.POST.get('text', '')

        print(user_input)

        #一時的に作成した今回の音声ファイルの削除
        audio_url = request.session.pop('temp_audio_file_to_delete', None)

        if audio_url:
            # settings.MEDIA_URLが '/media/' なら、それを除去する
            relative_filename = audio_url.replace(settings.MEDIA_URL, '', 1) 
            full_audio_path = os.path.join(settings.MEDIA_ROOT, relative_filename)
            if os.path.exists(full_audio_path):
                try:
                    os.remove(full_audio_path)
                    print("音声ファイルを削除しました。")
                except OSError as e:
                    print("音声ファイルの削除に失敗しました。")
            else:
                print("削除対象が見つかりませんでした。")


        # ★★★ セッションから正解データを取得 ★★★
        correct_answer = request.session.get('correct_answer', '')

        print("入力したテキスト：", user_input)



        # scoring_result = get_gemini_scoring(correct_answer, user_input)

        # context = {
        #     'user_input': user_input,
        #     'correct_answer': correct_answer,
        #     'score': scoring_result.get('score'),
        #     'advice': scoring_result.get('advice'),
        # }



        context = {
            'user_input': user_input,
            'correct_answer': correct_answer,
            'score': 0,
            'advice': "仮のアドバイス",
        }



        return render(request, "typeApp/result.html", context)
    
result = ResultView.as_view()