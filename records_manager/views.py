from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Record, Category

def index(request):
    return HttpResponseRedirect(reverse("records_manager:login"))

def login_view(request):
    try:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            response = HttpResponseRedirect(reverse("records_manager:records"))
        else:
            response = render(request, "records_manager/login.html",{"error_message":"Invalid login details"})
    except:
        response = render(request, "records_manager/login.html")
    return response

class RecordListView(LoginRequiredMixin, generic.ListView):
    template_name = "records_manager/record_list.html"
    context_object_name = "records"

    def get_queryset(self):
        try:
           query_string = self.request.GET["search"]
        except:
           query_string = None
        
        group_names = list(self.request.user.groups.values_list('name',flat=True))
        records = Record.objects.order_by("created_date").filter(category__group__name__in=group_names)

        if query_string:
            records = records.filter(Q(name__contains=query_string) | Q(description__contains=query_string))
        return records

class RecordView(LoginRequiredMixin,generic.DetailView):
    model = Record
    template_name = "records_manager/record_details.html"

class EditRecordView(LoginRequiredMixin, generic.DetailView):
    model = Record
    template_name = "records_manager/edit_record_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context

    def post(self, request, pk):
        print(request.POST)
        name = request.POST["name"]
        description = request.POST["description"]
        category = request.POST["category"]

        record = Record.objects.get(pk=pk)

        record.name = name
        record.description = description
        record.category = Category.objects.get(name=category)
        record.save()

        return HttpResponseRedirect(reverse("records_manager:records"))


class CreateRecordView(LoginRequiredMixin, generic.TemplateView):
    model = Record
    template_name = "records_manager/create_record.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context

    def post(self, request):
        name = request.POST["name"]
        description = request.POST["description"]
        category = Category.objects.get(name=request.POST["category"])
        creator = request.user
        created_date = timezone.now()

        record = Record.objects.create(name=name, description=description, category = category, creator=creator, created_date = created_date)

        record.save()

        return HttpResponseRedirect(reverse("records_manager:records"))
    

def search_categories(request):
    return HttpResponse("search categories")

def create_category(request):
    return HttpResponse("Create a category")

def view_category(request):
    return HttpResponse("view & search for records in a single category")
