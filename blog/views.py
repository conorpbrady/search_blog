from django.shortcuts import render
from .models import BlogPost
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = BlogPost
    ordering = 'post_date'
