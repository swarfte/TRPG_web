from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.

class HomeView(generic.View):
    def get(self, request):
        return render(request, 'introduce/home.html')