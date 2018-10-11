from django.shortcuts import render
from django.views import generic
from .models import *


class BlogListView(generic.ListView):
    model = Blog
    template_name = "blog/blog_list.html"


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"