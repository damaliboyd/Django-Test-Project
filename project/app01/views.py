from django.shortcuts import render
from app01.models import Parent
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ParentListView(ListView):
    model = Parent

class ParentDetailView(DetailView):
    model = Parent
