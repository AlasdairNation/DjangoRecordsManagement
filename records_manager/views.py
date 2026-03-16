from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("records_manager Index")

def login(request):
    return HttpResponse("Login")

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
