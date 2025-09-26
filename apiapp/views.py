from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .apiapp import get_gemini_response # 作成したサービスをインポート


class AskGeminiView(View):
    def get(self, request):
        # 最初のページ表示
        return render(request, 'apiapp/ask_gemini.html')

    def post(self, request):
        # フォームから送信された質問を取得
        user_prompt = request.POST.get('prompt', '')

        
        # Gemini APIから応答を取得
        # gemini_answer = get_gemini_response(user_prompt)
        
        # gemini_answer = "この文を入力してください。きっちょう"

        # gemini_answer = f'''皆様、日々の生活で「もっとこうだったら良いのに」と感じる瞬間はありませんか？そのお悩みを、この新商品「スマートアシスト」が解決します。これ一つで、あなたの日常がもっと快適で豊かに。ぜひ、この感動を体験してください。'''

        gemini_answer = "文章1だよ。文章2だよ。"

        # ★★★ 取得した答えをセッションに保存 ★★★
        request.session['correct_answer'] = gemini_answer
        request.session['user_prompt'] = user_prompt



        return redirect('typeApp:practice')


ask_gemini = AskGeminiView.as_view()

