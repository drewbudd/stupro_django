from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'home/index.html')

@login_required
def webgl(request):
    return render(request, 'home/WebGL.html')
