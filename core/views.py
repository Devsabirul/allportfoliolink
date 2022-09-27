from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    blogs = BlogModel.objects.all()
    src = SocailMediaLink.objects.all()
    return render(request, 'home/index.html', {'blogs': blogs, 'src': src})
