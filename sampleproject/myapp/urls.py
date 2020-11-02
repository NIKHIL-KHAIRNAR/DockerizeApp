from django.urls import path
from django.contrib import admin
from myapp.views import AuthorCreate, AuthorListView

app_name = 'myapp'
urlpatterns = [
    path('', AuthorCreate.as_view()),
    path('list/',AuthorListView.as_view(), name = 'author-list'),
]