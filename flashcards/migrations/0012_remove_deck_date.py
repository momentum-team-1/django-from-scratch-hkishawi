# Generated by Django 3.0.6 on 2020-06-05 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0011_auto_20200604_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='date',
        ),
    ]
