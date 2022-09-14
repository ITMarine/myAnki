from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Topic, Card
from .forms import TopicForm, CardForm, CardCreateForm


def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'anki/home.html', {'topics': topics})


def topic_detail(request, pk):
    topic = get_object_or_404(Topic, id=pk)
    cards = topic.cards.all().filter(is_active=True)
    return render(request, 'anki/topic.html', {'topic': topic, 'cards': cards})


def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic = form.save()
            return redirect('anki:topic', pk=topic.id)
    else:
        form = TopicForm()
        return render(request, 'anki/topic_create.html', {'form': form})


def topic_delete(request, pk):
    topic = get_object_or_404(Topic, id=pk)
    if request.method == 'POST':
        topic.delete()
        return redirect('anki:topic_list')
    return render(request, 'anki/topic_delete.html', {'topic': topic})


def card_detail(request, pk):
    card = get_object_or_404(Card, id=pk)
    topic = card.topic
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return render(request, 'anki/card.html', {'form': form,
                                                      'card': card,
                                                      'topic': topic})

    card.answer = ''
    form = CardForm()
    return render(request, 'anki/card.html', {'card': card,
                                              'form': form,
                                              'topic': topic})


def card_create(request, pk):
    topic = Topic.objects.get(id=pk)
    if request.method == 'POST':
        form = CardCreateForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.created = timezone.now()
            card.save()
            return redirect('anki:card_detail', pk=card.id)
        raise ValidationError("Incorrect card data")

    form = CardCreateForm(initial={'topic': topic})
    return render(request, 'anki/card_create.html', {'form': form, 'topic': topic})


def card_update(request, pk):
    card = get_object_or_404(Card, id=pk)
    if request.method == 'POST':
        form = CardCreateForm(request.POST, instance=card)
        if form.is_valid():
            card = form.save()
            return redirect('anki:card_detail', pk=card.id)
        raise ValidationError("Incorrect card data")
    form = CardCreateForm(instance=card)
    return render(request, 'anki/card_update.html', {'form': form, 'card': card})


def card_to_archive(request, pk):
    card = get_object_or_404(Card, id=pk)
    card.is_active = False
    next_card = card.get_next_card_or_first()
    return redirect('anki:card_detail', next_card.id)








