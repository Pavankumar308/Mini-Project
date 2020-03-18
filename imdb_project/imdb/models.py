from django.db import models

# Create your models here.


class Actor(models.Model):

    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    actor_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    actor_image = models.ImageField(upload_to='home/media/actors', height_field=None, width_field=None, max_length=None, null=True, blank=True) 
    actor_discription = models.TextField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    fb_likes = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    movies = models.ManyToManyField('Movie', through='Cast', blank=True)


    def __str__(self):
        return self.name

class Director(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    name = models.CharField(max_length=100)
    director_image = models.ImageField(upload_to='home/media/directors', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    director_discription = models.TextField(null=True)
    gender = models.CharField(max_length=50, choices=GENDER,null=True)
    no_of_facebook_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Movie(models.Model):

    GENRES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Comedy', 'Comedy'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Family', 'Family'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Sci-fi', 'Sci-fi'),
        ('Thriller', 'Thriller')
        
    )
    movie_id = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=200)
    movie_poster = models.ImageField(upload_to='home/media/movies', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    movie_discription = models.TextField(null=True)
    release_date = models.DateField(("Released Date"), auto_now=False, auto_now_add=False)
    imdb_link = models.CharField(max_length=1000)
    avg_rating = models.FloatField()
    budget = models.IntegerField(default=0)
    collections = models.FloatField()
    language = models.CharField(max_length=100, default='English')
    country = models.CharField(max_length=100, default='USA')
    likes_on_fb = models.IntegerField(default=0)
    genre = models.CharField(max_length=100,null=True, choices=GENRES)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Cast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name=("Acted Movie"), on_delete=models.CASCADE)
    role = models.CharField(max_length=50, null=True)
    is_debut_movie = models.BooleanField(default=False)

    def __str__(self):
        return self.actor.name + '  ' + self.movie.name + ' ' + self.role



