from django.shortcuts import render
from .models import Flashcard
from .forms import FlashcardForm

# Create your views here.
def list_decks(request):
    decks = Deck.objects.all()
    return render(request, "decks/list_decks.html", {"contacts": contacts})



def show_deck(request,pk):
    deck = 

def add_deck_title(request, contact_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    if request.method =='GET':
        form = DeckForm(instance=Deck)
    else:
        form = DeckForm(data=request.POST, instance=Deck)
        if form.is_valid():
            form.save()
            return redirect(to='list_decks')
