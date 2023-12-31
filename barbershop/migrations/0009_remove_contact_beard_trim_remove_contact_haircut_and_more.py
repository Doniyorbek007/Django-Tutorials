# Generated by Django 4.2.3 on 2023-07-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0008_price_remove_contact_email_remove_contact_facebook_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='beard_trim',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='haircut',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='razor_cut',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='shawes',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='starting',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='styling_color',
        ),
        migrations.RemoveField(
            model_name='price',
            name='email',
        ),
        migrations.RemoveField(
            model_name='price',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='price',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='price',
            name='open_time',
        ),
        migrations.RemoveField(
            model_name='price',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='price',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='price',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='price',
            name='youtube',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='facebook',
            field=models.CharField(default=12313, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='instagram',
            field=models.CharField(default=1231224141, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='open_time',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='twitter',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='whatsapp',
            field=models.CharField(default=11, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='youtube',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='beard_trim',
            field=models.FloatField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='haircut',
            field=models.FloatField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='photo',
            field=models.ImageField(default=1, unique=True, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='razor_cut',
            field=models.FloatField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='shawes',
            field=models.FloatField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='starting',
            field=models.FloatField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='price',
            name='styling_color',
            field=models.FloatField(default=11, max_length=6),
            preserve_default=False,
        ),
    ]
