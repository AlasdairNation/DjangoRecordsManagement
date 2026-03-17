from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("records_manager Index")

def login(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            response = HttpResponseRedirect(reverse("records_manager:home"))
        else:
            response = render(request, "records_manager/login.html",{"error_message":"Invalid login details"})
    except:
        response = render(request, "records_manager/login.html")
    return response

@login_required
def home(request):
    return HttpResponse("Home")

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
