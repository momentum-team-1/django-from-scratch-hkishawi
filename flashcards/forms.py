from django import forms
from .models import Flashcard

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'deck_name',
            'date',
            'tags',
        ]

# class Flashcard(forms.ModelForm):
#     class Meta: 
#         model = Flashcard
#         field = [
#             'flashcard_name',
#             'note',
#         ]