from django.db import models

# Create your models here.

class Transcription(models.Model):
    text = models.TextField(verbose_name="入力欄")
