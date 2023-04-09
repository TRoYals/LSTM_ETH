from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class dataFetch(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")