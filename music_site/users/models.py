from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Profile(models.Model):
    Male = "Mal"
    Female = "Fem"
    gender_choice = [
        (Male, "Male"),
        (Female, "Female"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(blank=True)
    avatar = ImageField(upload_to='avatars', default='default.png')
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=3,choices=gender_choice)

    def __str__(self):
        return '{} Profile'.format(self.user.username)


class Friend(models.Model):
    users = models.ManyToManyField(Profile)
    current_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)

    def __str__(self):
        return f'{self.current_user} has {self.users.count()}'



