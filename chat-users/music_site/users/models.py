from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(blank=True)
    avatar = ImageField(upload_to='avatars', default='default.png')

    def __str__(self):
        return '{} Profile'.format(self.user.username)


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)

    #Add new friend
    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    #Remove friend from friends
    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)



