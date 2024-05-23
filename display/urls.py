from django.urls import path

from . import views

app_name = "display"
urlpatterns = [
    path('', views.Main.as_view(), name="main"),

    path('event/create', views.EventCreate.as_view(), name="event_create"),
    path('event/<int:pk>/update', views.EventUpdate.as_view(), name="event_update"),
    path('event/<int:pk>/delete', views.EventDelete.as_view(), name="event_delete"),
    
    path('practice/create', views.PracticeCreate.as_view(), name="practice_create"),
    path('practice/<int:pk>/update', views.PracticeUpdate.as_view(), name="practice_update"),
    path('practice/<int:pk>/delete', views.PracticeDelete.as_view(), name="practice_delete"),

    path('event/<int:pk>/band/create', views.BandCreate.as_view(), name="band_create"),

]