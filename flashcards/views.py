from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# from .forms import FlashcardForm

# create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='deck_list')

    return render(request, "decks/home.html")

@login_required
def deck_list(request):
    your_decks = request.user.decks.all()
    
    return render(request, "decks/deck_list.html", {"decks": your_decks})

@login_required 
def deck_detail(request, pk):
    deck = get_object_or_404(request.user.decks, pk=pk)
    return render(request, "decks/deck_detail.html", {"deck": deck})

@login_required
def add_deck(request, pk):
    if request.method == "POST":
        form = DeckForm(data=request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect (to='deck_detail', deck_pk=deck.pk)
        else: form = DeckForm()

        return render(request, "decks/add_deck.html", {"form": form})

 
 

 

# @login_required
# def add_flashcard(request):
#     if request.method == 'POST':
#         form = FlashcardForm(data=request.POST)
#         if form.is_valid():
#             flashcard = form.save(commit=False)
#             flashcard.user = request.user 
#             flashcard.save()
#             return redirect(to='flashcard_detail', flashcard_pk=flashcard.pk)
#     else:
#         form = FlashcardForm()

#     return render(request, "flashcards/add_flashcard.html", {"form": form})