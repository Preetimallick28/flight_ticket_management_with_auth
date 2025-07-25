from django.urls import path
from user_auth import views

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('logout_/',views.logout_,name='logout_'),
    path('profile/',views.profile,name='profile'),
    path('reset_pass',views.reset_pass,name='reset_pass'),
    path('update_profile/<str:pk>',views.update_profile,name='update_profile'),
]
