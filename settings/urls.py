from django.urls import path
from settings.views import ProfileView

app_name = "settings"
urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name="profile"),
]
