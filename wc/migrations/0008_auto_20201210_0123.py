# Generated by Django 3.0.8 on 2020-12-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0007_auto_20201210_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
