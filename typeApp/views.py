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

        form = TranscriptionForm()

        return render(request, "typeApp/practice.html", {"form":form})
    
    def post(self, request):
        form = TranscriptionForm(request.POST)

        if form.is_valid():#データが正しいかどうか
            user_text = form.save()

            print("入力したテキスト：", user_text.text)

            return redirect('typeApp:top')
        else:
            return render(request, "typeApp/practice.html", {"form":form})
    
    
practice = PracticeView.as_view()
