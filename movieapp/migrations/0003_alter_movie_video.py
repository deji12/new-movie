# Generated by Django 4.0.4 on 2022-06-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_series_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
