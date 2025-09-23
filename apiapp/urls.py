from django.urls import path
from . import views

app_name = "apiapp"

urlpatterns = [
    path("", views.ask_gemini, name="ask_gemini"),
]
