from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse

from EnergyResource.models import *


@api_view(['GET'])
def hello(request):
    return HttpResponse(loader.get_template('nav-1.html').render())


@api_view(['POST'])
def setEnergyResourceView(request):
    """
        Function to create a new Energy Resource.
            URL : http://127.0.0.1:8000/new/ 
    """
    name, types, capacity, location, status = request.data["name"],request.data["type"], request.data["capacity"], request.data["location"], request.data["status"]
    createEnergyResource(name, types, capacity, location, status)
    return JsonResponse({"resp": True})


@api_view(['GET'])
def getEnergyResourceView(request):
    """ 
        Function to get all Energy Resources.
            URL : http://127.0.0.1:8000/energy/ 
    """
    res = getEnergyResourcesModel()
    return JsonResponse(res)


@api_view(['GET'])
def getEnergyResourceSearchView(request):
    """
        Function to get Energy Resources (according to its status).
            URL(s) : 
                http://127.0.0.1:8000/energy/search?type=solar
                http://127.0.0.1:8000/energy/search?min=150&max=300
                http://127.0.0.1:8000/energy/search?status=active&min=150&max=300
                http://127.0.0.1:8000/energy/search?type=solar&status=active&location=LocationA&min=150&max=300
                (...etc)
    """
    types, status, location, gte, lte = request.GET.get("type"), request.GET.get("status"), request.GET.get("location"), request.GET.get("min"), request.GET.get("max")
    res = getEnergyResourceSearchModel(types, status, location, gte, lte)
    return JsonResponse(res)


@api_view(['DELETE'])
def removeEnergyResourceView(request):
    """
        Function to remove an Energy Resource.
            URL : http://127.0.0.1:8000/close?eid=151997d9e640f530cdf2a6b55efdf193270d3405
    """
    res = request.GET.get("eid")
    print(f"From removeEnergyResourceView: {res}")
    res = removeEnergyResource(res)
    return JsonResponse({"resp": True})



