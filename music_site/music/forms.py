from django import forms
from django.contrib.auth import get_user_model
from .models import (Vote,
                     Album,
                     Comments)



class VoteForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput,
                                  queryset=get_user_model().objects.all(),
                                  disabled=True)

    album = forms.ModelChoiceField(widget=forms.HiddenInput,
                                  queryset=Album.objects.all(),
                                  disabled=True)

    value = forms.ChoiceField(label='Vote',
                              widget=forms.RadioSelect,
                              choices=Vote.VALUE_CHOICES)

    class Meta:
        model = Vote
        fields = ('value', 'user', 'album')


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text')




