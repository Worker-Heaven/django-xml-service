from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger

from .models import Item

import random

logger = get_task_logger(__name__)


@task()
def hello():
    print('Hello World')


@task(name='add_to_django_model')
def add():
    random_name = str(random.randint(1, 1000))
    
    print(random_name)   
    
    Item.objects.get_or_create(name=random_name)