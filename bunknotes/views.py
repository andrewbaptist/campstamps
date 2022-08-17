from django.shortcuts import render

# Create your views here.
from .models import Family
from django.template import loader
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def families(request):
    family_list = Family.objects.order_by('-balance')
    template = loader.get_template('bunknotes/families.html')
    context ={
            'family_list':family_list
            }
    return HttpResponse(template.render(context,request))
