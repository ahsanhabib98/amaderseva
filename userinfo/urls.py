from django.urls import path
from .views import sign_up, profile, profile_create, profile_detail, profile_edit
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', sign_up, name = 'signup'),
    path('login/', auth_views.login, {'template_name': 'userinfo/login.html'}, name = 'login'),
    path('logout/', auth_views.logout, {'template_name': 'home.html'}, name = 'logout'),
    path('profile/', profile, name = 'profile'),
    path('profile-create/', profile_create, name = 'profile-create'),
    path('profile-detail/', profile_detail, name = 'profile-detail'),
    path('profile-edit/', profile_edit, name = 'profile-edit'),
]
