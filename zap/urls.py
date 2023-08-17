from django.urls import path, include
from . import views

app_name = "zap"
urlpatterns = [
    path("", views.home, name="homepage"),
]
# 127.0.0.1:8000/