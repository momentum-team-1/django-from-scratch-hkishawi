from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auto.decorators import login_required

# from .forms import FlashcardForm

# create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='flashcard_list')
    
    return render(request, "flashcards/home.html")

# @login_required
# def flashcard_list(request):
#     your_flashcards = request.user.flashcards.all()

#     return render(requst, "recipes/flashcard_list.html", {'flashcards': your_flashcards})

# @login_required
# def flashcard_detail(request, flashcard_pk):
#     flashcard = get_object_or_404(request, user.flashcards, pk=flashcard_pk)
#     return render(request, "flashcards/flashcard_detail.html", {"flashcard": flashcard})

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