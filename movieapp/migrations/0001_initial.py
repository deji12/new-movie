# Generated by Django 4.0.4 on 2022-06-10 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=200)),
                ('episode_num', models.CharField(default='1', max_length=100)),
                ('video', models.CharField(blank=True, max_length=10000, null=True)),
                ('duration', models.CharField(max_length=100)),
                ('dou', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20000)),
                ('info', models.TextField()),
                ('video', models.FileField(upload_to='film/')),
                ('thumbnail', models.FileField(upload_to='thumb/')),
                ('age', models.CharField(default=13, max_length=20)),
                ('cat', models.CharField(default='cartoon', max_length=200)),
                ('premier', models.BooleanField(default=False)),
                ('rating', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('year_range', models.CharField(blank=True, max_length=200, null=True)),
                ('new', models.BooleanField(default=False)),
                ('duration', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=200)),
                ('draft', models.BooleanField(default=False)),
                ('date_added', models.CharField(default='text', max_length=200)),
                ('clicks', models.IntegerField(blank=True, default=0, null=True)),
                ('genre1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category1', to='movieapp.category')),
                ('genre2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category2', to='movieapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_value', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='series_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20000)),
                ('info', models.TextField()),
                ('thumbnail', models.FileField(upload_to='thumb/series/')),
                ('age', models.CharField(default=13, max_length=20)),
                ('rating', models.CharField(max_length=100)),
                ('new', models.BooleanField(default=False)),
                ('premier', models.BooleanField(default=False)),
                ('series_air_date', models.DateField(auto_now_add=True)),
                ('year_range', models.CharField(blank=True, max_length=200, null=True)),
                ('year', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=200)),
                ('draft', models.BooleanField(default=False)),
                ('genre1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='series_category1', to='movieapp.category')),
                ('genre2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='series_category2', to='movieapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_num', models.CharField(max_length=100)),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
                ('collapse', models.CharField(blank=True, max_length=100, null=True)),
                ('series_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season_val', to='movieapp.series')),
            ],
        ),
        migrations.CreateModel(
            name='reviewss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5000)),
                ('body', models.TextField()),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_review', to='movieapp.movie')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(upload_to='movie-photos')),
                ('series_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.series')),
            ],
        ),
        migrations.CreateModel(
            name='episode_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5000)),
                ('body', models.TextField()),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_reviews', to='movieapp.episode')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('series_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movieapp.series')),
            ],
        ),
        migrations.CreateModel(
            name='episode_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_comments', to='movieapp.episode')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('series_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movieapp.series')),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='season_val',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode', to='movieapp.season'),
        ),
        migrations.AddField(
            model_name='episode',
            name='series_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season_epi', to='movieapp.series'),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to='movieapp.movie')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
