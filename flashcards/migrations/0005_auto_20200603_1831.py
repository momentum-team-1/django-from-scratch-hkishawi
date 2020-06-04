# Generated by Django 3.0.6 on 2020-06-03 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0004_auto_20200603_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='prompt',
            name='prompt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
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
