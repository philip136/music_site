from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about_me = models.TextField(blank=True)
    avatar = ImageField(upload_to='avatars',default='default.png')

    def __str__(self):
        return '{} Profile'.format(self.user.username)
