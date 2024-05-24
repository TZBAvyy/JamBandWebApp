from django.urls import path

from . import views

app_name = "home" #Redirects to landing page if url 'home:home'
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
]