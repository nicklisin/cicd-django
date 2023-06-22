from django.shortcuts import render
from .models import Page


def index(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'index.html', context=context)
