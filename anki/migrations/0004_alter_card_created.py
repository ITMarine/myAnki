# Generated by Django 4.1.1 on 2022-09-14 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anki', '0003_remove_card_title_alter_card_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
