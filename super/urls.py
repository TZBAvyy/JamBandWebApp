from django.urls import path
from super.views import SuperView, BandDetailView

app_name = "super"
urlpatterns = [
    path('', SuperView.as_view(), name="home"),
    path('detail/<int:pk>', BandDetailView.as_view(), name="detail"),
]
