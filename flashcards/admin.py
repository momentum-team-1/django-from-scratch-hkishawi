from django.contrib import admin
from .models import Tag, Deck, Flashcard, Prompt, Answer

# Register your models here.

admin.site.register(Tag)
admin.site.register(Deck)
admin.site.register(Flashcard)
admin.site.register(Prompt)
admin.site.register(Answer)