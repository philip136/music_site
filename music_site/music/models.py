from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.aggregates import Sum
from django.urls import reverse



class AlbumManager(models.Manager):

    def all_with_related_persons(self):
        queryset = self.get_queryset()
        queryset = queryset.select_related('author')
        return queryset

    def all_with_related_persons_and_score(self):
        queryset = self.all_with_related_persons()
        queryset = queryset.annotate(score=Sum('vote__value'))
        return queryset

    def top_album(self,limit=10):
        queryset = self.get_queryset()
        queryset = queryset.annotate(vote_sum=Sum('vote__value'))
        queryset = queryset.exclude(vote_sum=None)
        queryset = queryset.order_by('-vote_sum')
        queryset = queryset[:limit]
        return queryset

    def classification(self,genre_name):
        queryset = self.get_queryset()
        queryset = queryset.filter(genre=genre_name)
        queryset = queryset.order_by('-release_date')
        return queryset


class Album(models.Model):
    NOT_RATED = 0
    RATED = 1
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED, 'R - Rated'),
    )
    author_album = models.CharField(max_length=100)
    name_album = models.CharField(max_length=140)
    release_date = models.DateTimeField(null=True)
    image_album = ImageField(upload_to='uploads')
    ratings = models.IntegerField(choices=RATINGS,default=NOT_RATED)
    genre = models.CharField(max_length=100)
    author = models.ForeignKey(to='Person', null=True, on_delete=models.SET_NULL, related_name='author', blank=True)
    objects = AlbumManager()

    def __str__(self):
        return '{}'.format(self.name_album)



class Person(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()
    died = models.DateField(null=True,blank=True)


    def __str__(self):
        if self.died:
            return '{},{} ({}-{})'.format(self.last_name,
                                          self.first_name,
                                          self.born,
                                          self.died)

        return '{},{} ({})'.format(self.first_name,
                                   self.last_name,
                                   self.born)



class SongsAlbum(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    name_song = models.CharField(max_length=140)
    file_song = models.FileField(upload_to='static/music/uploads/')
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.name_song

    def get_absolute_url(self):
        return reverse("music:SongAlbum", args=[self.album.id])



class VoteManager(models.Manager):
    def get_vote_or_unsaved_blank_vote(self,album,user):
        try:
            return Vote.objects.get(album=album,
                                    user=user)
        except Vote.DoesNotExist:
            return Vote(album=album,
                        user=user)


class Vote(models.Model):
    LIKE = 1
    DISLIKE = -1
    VALUE_CHOICES = (
        (LIKE, '+1'),
        (DISLIKE, '-1'),
    )
    value = models.SmallIntegerField(choices=VALUE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)
    objects = VoteManager()








