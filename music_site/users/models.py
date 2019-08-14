from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about_me = models.TextField(blank=True)
    avatar = ImageField(upload_to='avatars')

    def __str__(self):
        return '{} Profile'.format(self.user.username)


