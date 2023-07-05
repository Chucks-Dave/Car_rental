from django.urls import path
from .views import edit_profile, login, logout, register
from django.contrib.auth import views as auth_views

# URL patterns
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    # Retrieve Password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name="password_reset_complete"),
    # Change Password
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='user/change_password.html', success_url='/'), name="change_password"),
    
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("logout/", logout, name="logout"),
]
