from django.core.exceptions import ValidationError
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
    topic.delete()
    return redirect('anki:topic_list')


def card_detail(request, pk):
    card = get_object_or_404(Card, id=pk)
    card_next = Card.objects.filter(pk__gt=card.id).order_by('pk').first()
    card_previous = Card.objects.filter(pk__lt=card.id).order_by('-pk').first()
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return render(request, 'anki/card.html', {'form': form, 'card': card,
                                                      'card_next': card_next,
                                                      'card_previous': card_previous})

    card.answer = ''
    form = CardForm()
    return render(request, 'anki/card.html', {'card': card, 'form': form,
                                              'card_next': card_next,
                                              'card_previous': card_previous})


def card_create(request):
    if request.method == 'POST':
        form = CardCreateForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.created = timezone.now()
            card.save()
            return redirect('anki:card_detail', pk=card.id)
        raise ValidationError("Incorrect card data")
    form = CardCreateForm()
    return render(request, 'anki/card_create.html', {'form': form})


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
    card_next = Card.objects.filter(pk__gt=card.id).order_by('pk').first()
    card_first = Card.objects.first()
    card.is_active = False
    if card_next:
        return redirect('anki:card_detail', card_next.id)
    else:
        return redirect('anki:card_detail', card_first.id)






