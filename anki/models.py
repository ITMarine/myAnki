from django.db import models
from django.urls import reverse
from django.utils import timezone


class Topic(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default='title')

    def __str__(self):
        return self.title

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('anki:topic', args=[str(self.id)])


class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='cards')
    body = models.TextField()
    answer = models.TextField(blank=True)
    correct_answer = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.body[:50]

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('anki:card_detail', args=[str(self.id)])

    def get_next_card_or_first(self):
        self.next_card = Card.objects.filter(is_active=True).filter(pk__gt=self.id).order_by('pk').first()
        if self.next_card:
            return self.next_card
        else:
            return Card.objects.filter(is_active=True).first()

    def get_previous_card_or_last(self):
        self.previous_card = Card.objects.filter(is_active=True).filter(pk__lt=self.id).order_by('-pk').first()
        if self.previous_card:
            return self.previous_card
        else:
            return Card.objects.filter(is_active=True).last()

