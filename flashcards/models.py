from django.db import models
from users.models import User

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag

class Deck(models.Model):
    deck_name = models.CharField(max_length=255, null=True, blank =True)
    date = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    tags = models.ManyToManyField(to="Tag", related_name="decks")

    def __str__(self):
        return self.title
    # add
    # delete
    # edit

class Flashcard(models.Model):
    Deck = models.ForeignKey(to=Deck, on_delete=models.CASCADE, related_name="flashcards")
    flashcard_name = models.CharField(max_length=255, null=True, blank=True)
    
    # attempts
    # success
    def __str__(self):
        return f"{self.flashcard_name}"
    # add
    # delete
    # edit

class Prompt(models.Model):
    Deck = models.ForeignKey(to=Flashcard, on_delete=models.CASCADE, related_name='prompts')
    prompt = models.CharField(max_length=255, null=True, blank=True)
    # add
    # delete
    # edit

    def __str__(self):
        return f"{self.prompt}"

class Answer(models.Model):
    Deck = models.ForeignKey(to=Flashcard, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.answer}"

    # add
    # delete
    # edit
