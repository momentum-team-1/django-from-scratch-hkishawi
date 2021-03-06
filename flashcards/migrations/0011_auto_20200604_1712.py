# Generated by Django 3.0.6 on 2020-06-04 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcards', '0010_auto_20200604_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prompt',
            name='Deck',
        ),
        migrations.RenameField(
            model_name='flashcard',
            old_name='Deck',
            new_name='deck',
        ),
        migrations.AddField(
            model_name='deck',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='decks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flashcard',
            name='answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='flashcard',
            name='prompt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Prompt',
        ),
    ]
