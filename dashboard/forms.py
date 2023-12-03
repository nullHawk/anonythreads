from django import forms
from .models import Confession

class ConfessionForm(forms.ModelForm):
    subject = forms.CharField(max_length=60,required=True,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    class Meta:
        model = Confession
        fields = ['subject', 'content']