from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tryView1(request):
    return HttpResponse("Helo")