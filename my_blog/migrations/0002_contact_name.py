# Generated by Django 4.2.3 on 2023-07-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
