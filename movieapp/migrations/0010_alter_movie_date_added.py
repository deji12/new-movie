# Generated by Django 4.0.4 on 2022-06-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0009_alter_profile_comments_alter_profile_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
