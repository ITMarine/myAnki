from django import forms
from django.forms import Textarea

from .models import Topic, Card


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title',)


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('answer',)
        widgets = {
            'answer': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        exclude = ('answer', 'created',)
        widgets = {
            'correct_answer': Textarea(attrs={'cols': 80, 'rows': 20}),
            'body': Textarea(attrs={'cols': 60, 'rows': 10}),
        }
