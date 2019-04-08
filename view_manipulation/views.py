from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

from .models import Item

def index(request):
    items = Item.objects.order_by('birthday')
    template = loader.get_template('view_manipulation/index.html')

    context = {
        'items': items,
    }
    
    return render(request, 'view_manipulation/index.html', context)


def details(request, name):
    detailed_info = Item.objects.get(name=name)

    template = loader.get_template('view_manipulation/details.xml')

    context = {
        'detailed_info': detailed_info
    }

    response = HttpResponse(template.render(context, request))

    response['Content-Type'] = 'text/xml'

    return response

def add(request):
    if request.method == 'GET':
        template = loader.get_template('view_manipulation/add.html')
        return HttpResponse(template.render({}, request))

    elif request.method == 'POST':      
        try:
            name = request.POST['dev_name']
            
            q = Item(name=name)
            q.save()
            
            print('q.name', q.name)
            print('all data ------------', [ item.name for item in Item.objects.all()])

            return HttpResponseRedirect(reverse('index'))

        except:
            print('!------------------------------------------!')
            return HttpResponseRedirect(reverse('index'))
        
