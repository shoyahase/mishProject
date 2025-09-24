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
                   "user_prompt": user_prompt,
                   "form": form}

        return render(request, "typeApp/practice.html", context)
    
practice = PracticeView.as_view()



class ResultView(View):
    def post(self, request):

        user_input = request.POST.get('user_input_text', '')

        print(user_input)


        # ★★★ セッションから正解データを取得 ★★★
        correct_answer = request.session.get('correct_answer', '')

        print("入力したテキスト：", user_input)

        scoring_result = get_gemini_scoring(correct_answer, user_input)


        context = {
            'user_input': user_input,
            'correct_answer': correct_answer,
            'score': scoring_result.get('score'),
            'advice': scoring_result.get('advice'),
        }



        return render(request, "typeApp/result.html", context)
    
result = ResultView.as_view()