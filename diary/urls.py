from django.urls import path

from diary import views
from diary.apps import DiaryConfig
from diary.views import RecordListView, RecordCreateView, RecordUpdateView, RecordDeleteView, RecordDetailsView

app_name = DiaryConfig.name

urlpatterns = [
    path("", views.index, name="home"),
    path("diary/", RecordListView.as_view(), name="diary"),
    path("diary/add/", RecordCreateView.as_view(), name="create_record"),
    path("diary/<int:pk>/edit/", RecordUpdateView.as_view(), name="edit_record"),
    path("diary/<int:pk>/", RecordDeleteView.as_view(), name="delete_record"),
    path("diary/<int:pk>/detail/", RecordDetailsView.as_view(), name="detail_record"),
]
