from django.urls import path
from .views import ProfileView, AdminView

app_name = "settings"
urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name="profile"),
    path('admin/', AdminView.as_view(), name="admin"),
]
