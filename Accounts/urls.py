from django.urls import path
from . import views


urlpatterns = [
    # home page
    path('', views.home, name="home"),

    # login page
    path('login/', views.login_request, name="Login"),

    # logout page
    path('logout/', views.logout_request, name="Logut"),

    # register page
    path('registration/', views.registration, name="Register")
]
