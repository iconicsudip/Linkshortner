# Generated by Django 3.0.8 on 2020-12-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0006_auto_20201210_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(max_length=8),
        ),
    ]
