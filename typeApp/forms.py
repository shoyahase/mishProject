from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Transcription

class TranscriptionForm(ModelForm):
    class Meta:
        model = Transcription
        fields = ['text']

