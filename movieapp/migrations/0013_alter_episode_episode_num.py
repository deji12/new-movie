# Generated by Django 4.0.4 on 2022-07-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0012_alter_series_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode_num',
            field=models.IntegerField(default=1),
        ),
    ]
