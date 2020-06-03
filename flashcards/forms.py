from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta: 
        model = Deck
        fields = [
            'deck_name',
            'date',
        ]

class Flashcard(forms.ModelForm):
    class Meta: 
        model = Flashcard
        field = [
            'flashcard_name',
            'note',
        ]