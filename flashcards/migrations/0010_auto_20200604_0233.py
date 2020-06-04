# Generated by Django 3.0.6 on 2020-06-04 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0009_auto_20200604_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='Deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='flashcards.Flashcard'),
        ),
        migrations.AlterField(
            model_name='prompt',
            name='Deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prompts', to='flashcards.Flashcard'),
        ),
    ]
