from django.shortcuts import render
from django.views import generic

from .models import Job


class JobListView(generic.ListView):
    model = Job
    template_name = "jobs/home.html"
