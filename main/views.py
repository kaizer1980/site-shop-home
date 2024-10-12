from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import title, first


def index(request):
    context = {'title' : 'Home',
               'content' : ' Главная страница магазина - Home',
               'list': ['first', 'second'],
               'dist': {'first' : 1},
               'bool': True,
}
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About')
