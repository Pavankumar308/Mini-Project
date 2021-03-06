# Generated by Django 3.0.4 on 2020-03-18 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('actor_image', models.ImageField(blank=True, null=True, upload_to='home/media/actors')),
                ('actor_discription', models.TextField(null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=50)),
                ('fb_likes', models.IntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('director_image', models.ImageField(blank=True, null=True, upload_to='home/media/directors')),
                ('director_discription', models.TextField(null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=50, null=True)),
                ('no_of_facebook_likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('movie_poster', models.ImageField(blank=True, null=True, upload_to='home/media/movies')),
                ('movie_discription', models.TextField(null=True)),
                ('release_date', models.DateField(verbose_name='Released Date')),
                ('imdb_link', models.CharField(max_length=1000)),
                ('avg_rating', models.FloatField()),
                ('budget', models.IntegerField(default=0)),
                ('collections', models.FloatField()),
                ('language', models.CharField(default='English', max_length=100)),
                ('country', models.CharField(default='USA', max_length=100)),
                ('likes_on_fb', models.IntegerField(default=0)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Sci-fi', 'Sci-fi'), ('Thriller', 'Thriller')], max_length=100, null=True)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='imdb.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, null=True)),
                ('is_debut_movie', models.BooleanField(default=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.Movie', verbose_name='Acted Movie')),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(blank=True, through='imdb.Cast', to='imdb.Movie'),
        ),
    ]
