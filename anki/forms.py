from django import forms

from .models import Topic, Card


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title',)


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('answer',)
    answer = forms.CharField(widget=forms.Textarea)


class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        exclude = ('answer', 'created',)
