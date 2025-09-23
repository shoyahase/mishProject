from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from datetime import datetime
from zoneinfo import ZoneInfo
# Create your views here.

from .forms import TranscriptionForm

from apiapp.apiapp import get_gemini_scoring

class TopView(View):
    def get(self, request):
        date = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y年%m月%d日 %H:%M:%S")

        return render(request, "typeApp/top.html", {"date": date})
    
top = TopView.as_view()

class PracticeView(View):
    def get(self, request):

        correct_answer = request.session.get("correct_answer", '')
        user_prompt = request.session.get('user_prompt', "")

        form = TranscriptionForm()

        context = {"correct_answer":correct_answer,
                   "form": form,
                   "user_prompt": user_prompt}

        return render(request, "typeApp/practice.html", context)
    
    def post(self, request):
        form = TranscriptionForm(request.POST)

        if form.is_valid():#データが正しいかどうか
            user_input = form.cleaned_data['text']

            # ★★★ セッションから正解データを取得 ★★★
            correct_answer = request.session.get('correct_answer', '')

            print("入力したテキスト：", user_input)

            scoring_result = get_gemini_scoring(correct_answer, user_input)

            request.session['user_input'] = user_input
            request.session['score'] = scoring_result.get('score')
            request.session['advice'] = scoring_result.get('advice')

            return redirect('typeApp:result')
        else:
            return render(request, "typeApp/practice.html", {"form":form})
    
    
practice = PracticeView.as_view()

class ResultView(View):
    def get(self, request):

        user_input = request.session.pop('user_input', '(入力がない)')
        correct_answer = request.session.pop("correct_answer", "")
        score = request.session.pop('score', 0)
        advice = request.session.pop('advice', '') # ★アドバイスもセッションから取得


        context = {
            'user_input': user_input,
            'correct_answer': correct_answer,
            'score': score,
            'advice': advice, # ★コンテキストに追加
        }



        return render(request, "typeApp/result.html", context)
    
result = ResultView.as_view()