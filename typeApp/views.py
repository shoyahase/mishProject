from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from datetime import datetime
from zoneinfo import ZoneInfo
# Create your views here.

from .forms import TranscriptionForm

class TopView(View):
    def get(self, request):
        date = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y年%m月%d日 %H:%M:%S")

        return render(request, "typeApp/top.html", {"date": date})
    
top = TopView.as_view()

class PracticeView(View):
    def get(self, request):

        correct_answer = request.session["correct_answer"]
        user_prompt = request.session['user_prompt']

        form = TranscriptionForm()

        context = {"correct_answer":correct_answer,
                   "form": form,
                   "user_prompt": user_prompt}

        return render(request, "typeApp/practice.html", context)
    
    def post(self, request):
        form = TranscriptionForm(request.POST)

        if form.is_valid():#データが正しいかどうか
            user_text = form.cleaned_data['text']

            print("入力したテキスト：", user_text)

            request.session['user_input'] = user_text

            return redirect('typeApp:result')
        else:
            return render(request, "typeApp/practice.html", {"form":form})
    
    
practice = PracticeView.as_view()

class ResultView(View):
    def get(self, request):

        user_input = request.session.get('user_input', '(入力がない)')

        if 'user_input' in request.session:
            del request.session['user_input']

        correct_answer = request.session["correct_answer"]

        if user_input == correct_answer:
            score = 10
        else:
            score = 0

        context = {
        'user_input': user_input,
        'correct_answer': correct_answer,
        'score': score,
        }


        return render(request, "typeApp/result.html", context)
    
result = ResultView.as_view()