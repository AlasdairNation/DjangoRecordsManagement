from django.urls import path
from . import views

app_name = "records_manager"
urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login_view, name = "login"),
    path("records/", views.RecordListView.as_view(), name = "records"),
    path("records/<pk>/view/", views.RecordView.as_view(), name="record_details"),
    path("records/<pk>/edit/", views.EditRecordView.as_view(), name="edit_record_details"),
    path("records/create/", views.CreateRecordView.as_view(), name="create_record"),
]