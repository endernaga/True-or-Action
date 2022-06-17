from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from random import choice

def mainpage(request):
    tables = []
    tables_add = []
    for i in range(len(GlobalList.objects.all())):
        if i % 2 == 1 and len(GlobalList.objects.all()) >= 2:
            tables_add.append(list(GlobalList.objects.all())[i])
            tables.append(tables_add)
            tables_add = []
        else:
            tables_add.append(list(GlobalList.objects.all())[i])
    context = {'forms' :  GlobalList.objects.all(),
               'category' : ChoseType.objects.all(),
               'type' : 0,
               'random_action': choice(GlobalList.objects.all()),
               'tables': tables}
    return render(request, 'TrueorAction/mainpage.html', context=context)

def choseType(request, type):
    context = {'forms' : GlobalList.objects.filter(type_id=type),
               'category' : ChoseType.objects.all(),
               'type': type,
               'random_action' : choice(GlobalList.objects.filter(type_id=type)),
               'types': ChoseType.objects.get(pk=type)}
    return render(request, 'TrueorAction/mainpage.html', context=context)