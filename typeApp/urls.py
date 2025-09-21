from django.urls import path
from . import views

app_name = "typeApp"

urlpatterns = [
    path("", views.top, name="top"),
    path("practice/", views.practice, name="practice"),
    # path("make_quiz/", views.make_quiz, name="make_quiz"),
    # path("list_quiz/", views.list_quiz, name="list_quiz"),
    # path("answer_quiz/<uuid:quiz_id>/answer/", views.answer_quiz, name="answer_quiz"),
    
]