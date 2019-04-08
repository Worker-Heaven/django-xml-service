from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Item

def index(requests):
    items = Item.objects.order_by('birthday')[:5]
    template = loader.get_template('view_manipulation/index.html')

    context = {
        'items': items,
    }
    
    return render(requests, 'view_manipulation/index.html', context)


def details(requests, name):
    detailed_info = Item.objects.get(name=name)

    template = loader.get_template('view_manipulation/details.xml')

    context = {
        'detailed_info': detailed_info
    }

    response = HttpResponse(template.render(context, requests))

    response['Content-Type'] = 'text/xml'

    return response