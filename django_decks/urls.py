"""django_decks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from flashcards import views as flashcards_views


urlpatterns = [
    path('', flashcards_views.homepage, name='homepage'), 
    path('decks/', flashcards_views.deck_list, name='deck_list'),
    path('decks/new/', flashcards_views.add_deck, name='add_deck'),
    path('decks/<int:deck_pk>/delete_deck/', flashcards_views.delete_deck, name='delete_deck'),
    path('decks/<int:deck_pk>/edit/', flashcards_views.edit_deck, name='edit_deck'),
    path('decks/<int:deck_pk>/add_flashcard/', flashcards_views.add_flashcard, name='add_flashcard'),
    path('decks/<int:card_pk>/view_prompt/', flashcards_views.view_prompt, name='view_prompt'),
    path('decks/<int:card_pk>/view_answer/', flashcards_views.view_answer, name='view_answer'),
    path('decks/<int:card_pk>/delete_flashcard/', flashcards_views.delete_flashcard, name='delete_flashcard'), 
    path('decks/<int:card_pk>/edit_flashcard/', flashcards_views.edit_flashcard, name='edit_flashcard'),
    path('decks/<int:deck_pk>/', flashcards_views.deck_detail, name='deck_detail'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    ]   

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

