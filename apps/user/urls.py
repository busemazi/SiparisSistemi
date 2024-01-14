from django.urls import path
from .views import register_user
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    path('register_user/', register_user, name='register-user'),
    path('login/', LoginView.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(), name='logout' ),

]