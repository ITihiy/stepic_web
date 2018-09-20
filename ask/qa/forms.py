from django import forms
from .models import Question

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.TextInput)


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.ModelChoiceField(queryset=Question.objects.all(), empty_label=None)
