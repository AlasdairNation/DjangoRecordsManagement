from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, models
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Record, Category

def index(request):
    return HttpResponse("records_manager Index")

def login_view(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            response = HttpResponseRedirect(reverse("records_manager:home"))
        else:
            response = render(request, "records_manager/login.html",{"error_message":"Invalid login details"})
    except:
        response = render(request, "records_manager/login.html")
    return response

@login_required
def home(request):
    return HttpResponse("Home")

class HomeView(generic.ListView):
    template_name = "records_manager/home.html"
    context_object_name = "records"

    def get_queryset(self):
        group_names = list(self.request.user.groups.values_list('name',flat=True))
        print(group_names)
        return Record.objects.order_by("created_date").filter(category__group__name__in=group_names)

def create_record(request):
    return HttpResponse("create record")

def view_record(request):
    return HttpResponse("view record")

def search_categories(request):
    return HttpResponse("search categories")

def create_category(request):
    return HttpResponse("Create a category")

def view_category(request):
    return HttpResponse("view & search for records in a single category")


def verify_auth(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("records_manager:login"))
