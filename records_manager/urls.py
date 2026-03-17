from django.urls import path
from . import views

app_name = "records_manager"
urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login_view, name = "login"),
    path("home/", views.HomeView.as_view(), name = "home"),
]