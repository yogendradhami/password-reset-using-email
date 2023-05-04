from django.urls import path
from . import views
from .views import Login, Register, Logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),

    path('reset-password/', auth_views.PasswordResetView.as_view(),name='reset_password'),

    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
