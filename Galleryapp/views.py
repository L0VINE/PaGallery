from typing import NamedTuple
from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import *
# Create your views here.
def home(request):
    images = Image.objects.all()
    location = Location.objects.all()
    category = categories.objects.all()

    if 'location' in request.GET and request.GET['location']:
        name = request.GET.get('location')
        images = Image.view_location(name)

    elif 'category' in request.GET and request.GET['category']:
        cat = request.GET.get('categories')
        images = Image.view_category(cat)
        return render(request, 'all-images.html', {"name":NamedTuple,"images":images,"cat":cat })

    return render(request,"all-images.html",{"images":images,"location":location,"category":category})
