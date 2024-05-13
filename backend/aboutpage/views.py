from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello from PersonPage")


@api_view(['GET'])
def getPeople(request):
    personList = PersonSerializer(Person.objects.all(), many = True)
    response = Response(personList.data)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Credentials"] = "true"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"

    return Response(personList.data)


