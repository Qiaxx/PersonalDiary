from django.urls import path

from diary import views
from diary.apps import DiaryConfig

app_name = DiaryConfig.name

urlpatterns = [
    path("", views.index, name="home")
]