from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Event
def homePage(request):
    return HttpResponse('<h1> welcome to ...</h1>')


def listEventsStatic(request):
    list = [
    
        {
        'title':'Event1',
        'description':'description'
        },
        {
        'title':'Event2',
        'description':'description2'
        },
        {
        'title':'Event3',
        'description':'description3'
        }
    ]
    return render(
        request,
        'events/listEvents.html',
        {
            'events':list,
        }
    )

def listEvents(request):
    list = Event.objects.all() # select event from event

    return render(
        request,
        'events/listEvents.html',
        {
            'events':list,
        }
    )