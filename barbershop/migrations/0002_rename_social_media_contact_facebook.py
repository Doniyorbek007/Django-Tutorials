# Generated by Django 4.2.3 on 2023-07-20 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='social_media',
            new_name='facebook',
        ),
    ]
