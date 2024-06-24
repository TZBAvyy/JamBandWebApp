from django.urls import path

from . import views

app_name = "display"
urlpatterns = [
    #Main Views
    path('', views.Main.as_view(), name="main"),
    path('members/', views.MemberView.as_view(), name="members"),

    #Event CRUD Views
    path('event/create', views.EventCreate.as_view(), name="event_create"),
    path('event/<int:pk>/update', views.EventUpdate.as_view(), name="event_update"),
    path('event/<int:pk>/delete', views.EventDelete.as_view(), name="event_delete"),
    
    #Practice CRUD Views
    path('practice/create', views.PracticeCreate.as_view(), name="practice_create"),
    path('practice/<int:pk>/update', views.PracticeUpdate.as_view(), name="practice_update"),
    path('practice/<int:pk>/delete', views.PracticeDelete.as_view(), name="practice_delete"),

    # #Band CRUD Views
    # path('event/<int:pk>/band/create', views.BandCreate.as_view(), name="band_create"), #Event_id for foreign key creation
    # path('band/<int:pk>/update', views.BandUpdate.as_view(), name="band_update"),
    # path('band/<int:pk>/delete', views.BandDelete.as_view(), name="band_delete"),

    # #BandMember CRUD Views
    # path('band/<int:pk>/member/create', views.BandMemberCreate.as_view(), name="bandmember_create"), #Band_id for foreign key creation
    # path('member/<int:pk>/update', views.BandMemberUpdate.as_view(), name="bandmember_update"),
    # path('member/<int:pk>/delete', views.BandMemberDelete.as_view(), name="bandmember_delete"),

]