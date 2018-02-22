from django.shortcuts import render
from django.http import HttpResponse
from .models import Portifolio, Tag
from django.db.models.base import ObjectDoesNotExist


def projects(request):
    
    projo=Portifolio.all_projects()  


    return render(request,'index.html',{"projo":projo})



def description(request,id):
    
    try:
   
        project=Portifolio.objects.get(id=id)
    except Portifolio.DoesNotExist:
        raise Http404()  

    return render(request,'all-news/portofolio.html',{"project": project})