from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from myapp.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'book']

    def get_success_url(self):
        return '/list/'

class AuthorListView(ListView):
    template_name = 'myapp/author_list.html'
    model = Author
    context_object_name = "authors"
