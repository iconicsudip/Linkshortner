# Generated by Django 3.0.8 on 2021-01-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0011_notuserurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='url_id',
            field=models.IntegerField(default=0),
        ),
    ]
