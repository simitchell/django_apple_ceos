from django.shortcuts import render

# Create your views here.

from .models import CEOInfo

def index(request):
    num_ceos = CEOInfo.objects.all().count
    ceos = CEOInfo.objects.all()

    return render(
        request,
        'index.html',
        context={ }
    )