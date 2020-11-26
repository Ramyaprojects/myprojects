from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def abc_view(request):
    s="<h1>hello this is abacproject</h1>"
    return HttpResponse(s)