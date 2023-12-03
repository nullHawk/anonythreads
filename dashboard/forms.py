from django import forms
from .models import Confession

class ConfessionForm(forms.ModelForm):
    class Meta:
        model = Confession
        fields = ['subject', 'content']