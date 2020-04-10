from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
CARDS = (
    ('L', 'Land'),
    ('C', 'Creature'),
    ('A', 'Artifact'),
    ('E', 'Enchantment'),
    ('P', 'Planeswalker'),
    ('I', 'Instant'),
    ('S', 'Sorcery')
)

class Color(models.Model):
    color = models.CharField(max_length=100)

class Card(models.Model):
    name = models.CharField(max_length=200)
    cmc = models.IntegerField()
    card_type = models.CharField(
        max_length = 1,
        choices = CARDS,
        default=CARDS[0][0]
    )
    ability = models.CharField(max_length=250)
    colors = models.ManyToManyField(Color)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Deck(models.Model):
    name = models.CharField(max_length=100)
    commander = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card)

