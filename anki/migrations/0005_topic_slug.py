# Generated by Django 4.1.1 on 2022-09-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anki', '0004_alter_card_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default='title', max_length=100),
        ),
    ]