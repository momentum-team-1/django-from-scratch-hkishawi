from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, FlashcardForm
from .models import Flashcard 
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
def deck_detail(request, deck_pk):
    deck = get_object_or_404(request.user.decks, pk=deck_pk)
    
    return render(request, "decks/deck_detail.html", {"deck": deck})

@login_required
def add_deck(request):
    if request.method == "POST":
        form = DeckForm(data=request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect(to='deck_detail', deck_pk=deck.pk)
    else: 
        form = DeckForm()

    return render(request, "decks/add_deck.html", {"form": form})

@login_required
def delete_deck(request, deck_pk):
    deck = get_object_or_404(request.user.decks, pk=deck_pk)

    if request.method == "POST":
        deck.delete()
        return redirect(to='deck_list')

    return render(request, "decks/delete_deck.html", { "deck": deck }) 
 
@login_required
def edit_deck(request, deck_pk):
    deck = get_object_or_404(request.user.decks, pk=deck_pk)

    if request.method == "POST":
        form = DeckForm(instance=deck, data=request.POST)
        if form.is_valid():
            deck = form.save()
            return redirect(to='edit_deck', deck_pk=deck.pk)
    else: 
        form = DeckForm(instance=deck)

    return render(request, "decks/deck_detail.html", {
        "form": form,
        "deck": deck
    })

@login_required
def add_flashcard(request, deck_pk):
    deck = get_object_or_404(request.user.decks, pk=deck_pk)

    if request.method == "POST": #user is submitting form
        form = FlashcardForm(data=request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.deck = deck
            flashcard.save()
            return redirect(to='deck_detail', deck_pk=deck.pk)
    else: #if user is viewing pg for first time
        form = FlashcardForm()
    
    return render(request, "decks/add_flashcard.html", {
        "form": form,
        "deck": deck
    })

@login_required
def view_prompt(request, card_pk):
    flashcard = get_object_or_404(Flashcard, pk=card_pk)
    return render(request, "decks/view_prompt.html", 
    {"flashcard": flashcard})

@login_required
def view_answer(request, card_pk):
    flashcard = get_object_or_404(Flashcard, pk=card_pk)
    return render(request, "decks/view_answer.html", 
    {"flashcard": flashcard})

@login_required
def delete_flashcard(request, card_pk):
    flashcard = get_object_or_404(Flashcard, pk=card_pk)

    if request.method == "POST":
        flashcard.delete()
        return redirect(to='deck_detail', deck_pk=flashcard.deck.pk)
 
    return render(request, "decks/delete_flashcard.html", 
    { "flashcard": flashcard }) 

@login_required
def edit_flashcard(request, card_pk):
    flashcard = get_object_or_404(Flashcard, pk=card_pk)

    if request.method == "POST":
        form = FlashcardForm (instance=flashcard, data=request.POST)
        if form.is_valid():
            deck = form.save()
            return redirect(to='deck_detail', deck_pk=flashcard.deck.pk)
    else: 
        form = FlashcardForm(instance=flashcard)

    return render(request, "decks/deck_detail.html", {
        "form": form,
        "flashcard": flashcard
    })