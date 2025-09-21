from django import forms
from django.forms import ModelForm, inlineformset_factory


class TranscriptionForm(forms.Form):
    # 'text'という名前の入力欄を定義します。
    # CharFieldは文字列の入力欄です。
    text = forms.CharField(
        label='文字起こし', 
        widget=forms.Textarea(attrs={'rows': 20, 'cols': 80}) # Textareaウィジェットを使い、入力欄を大きくします。
    )

