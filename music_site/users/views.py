from django.shortcuts import (redirect,
                              render)
from django.contrib import messages
from .forms import (UserRegisterForm,
                    UserUpdateForm,
                    ProfileUpdateForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Friend



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username}!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('users:profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    friend = Friend.objects.get(current_user=request.user.id)
    context = {'user_form': user_form,
               'profile_form': profile_form,
               'friend': friend,
               }
    return render(request, 'users/profile.html', context)


def change_friend(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
    return redirect('users:profile')


def profile_user(request):
    pass