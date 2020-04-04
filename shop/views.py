from django.http import HttpResponse
from .models import Person
# Create your views here.

def crud(request):

    objs = Person.objects.all()

    for obj in objs:
        print(Person.__str__(obj))

    return HttpResponse("Done")