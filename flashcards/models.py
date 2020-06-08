from django.db import models
from users.models import User

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

class Deck(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="decks", null=True)
    deck_name = models.CharField(max_length=255, null=True, blank =True)
    # date = models.DateField(auto_now=False, auto_now_add=False, editable=False, blank=True)
    tags = models.ManyToManyField(to="Tag", related_name="decks")

    def __str__(self):
        return self.deck_name
    # add
    # delete
    # edit

class Flashcard(models.Model):
    deck = models.ForeignKey(to=Deck, on_delete=models.CASCADE, related_name="flashcards")
    flashcard_name = models.CharField(max_length=255, null=True, blank=True)
    prompt = models.CharField(max_length=255, null=True, blank=True)
    answer = models.CharField(max_length=255, null=True, blank=True)
    # attempts
    # success
    def __str__(self):
        return f"{self.prompt} {self.answer}"
  

  