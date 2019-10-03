from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (register,
                    profile,
                    change_friend,
                    profile_user
                    )


app_name = 'users'
urlpatterns = [
    path('register/',register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>', profile_user, name='profile_user'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',
                                              html_email_template_name='users/password_reset_email.html'
                                              ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'), name='users/password_reset_confirm'),
    path('password-reset/complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete'),
         name='password_reset_complete'),
    path('profile/<operation>/<int:pk>', change_friend, name='change_friends'),

]