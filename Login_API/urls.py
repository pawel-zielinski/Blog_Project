from django.urls import path
from . import views


app_name = 'Login_API'

urlpatterns = [
    path('signup/', views.sign_up, name = 'signup'),
    path('login/', views.login_page, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('change_profile/', views.user_change, name = 'user_change'),
    path('password/', views.pass_change, name = 'pass_change'),
    path('change_profile_image/', views.add_profile_pic, name = 'add_profile_pic'),
    path('change_picture/', views.change_profile_pic, name = 'change_profile_pic'),
]
