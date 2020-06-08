from django import forms
from .models import Deck, Flashcard

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'deck_name',
            # 'date',
            # 'tags',
        ]

class FlashcardForm(forms.ModelForm):
    class Meta: 
        model = Flashcard
        fields = [
            'prompt',
            'answer'
        ]

#