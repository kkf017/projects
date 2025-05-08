from django.db import models


import hashlib
from typing import List, Dict, Union


HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()


class EnergyResource(models.Model):
    """
        Class to implement the model of an Energy resource (in database).
    """
    eid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    capacity = models.FloatField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=255)



def createEnergyResource(name:str, types:str, capacity:float, location:str, status:str)->None:
    """
        Function to create an Energy resource (in table).
        input:
            name, types, capacity, location, status - informations of the Energy Resource
        output:
            None
        opt.
    """
    if not EnergyResource.objects.filter(eid=HASH(name+location)).values().exists():
        res = EnergyResource(eid=HASH(name+location), name=name, types=types, capacity=capacity,location=location, status=status)
        res.save()


def getEnergyResourcesModel()->Dict[str, Dict[str, Union[str, float]]]:
    """
        Function to get all Energy resources (in table).
        input:
            None
        output:
            Energy Resources
        opt.
    """
    res = [ x for x in EnergyResource.objects.all().values()]
    return {"ressources": res}



def getEnergyResourceSearchModel(types:str, status:str, location:str, gte:float, lte:float)->Dict[str, Dict[str, Union[str, float]]]:
    """
        Function to get Energy resources (according to a search).
        input:
            types -  solar, wind, hydro, nuclear ...etc
            status - active, inactive, maintenance ...etc
            location - Location A, B, C ....
            lte, gte - range for capacity
            
            types, status, location, minus, maxi can be None
        output:
            Energy Resources
        opt.
    """
    res = EnergyResource.objects.all()
    if types != None:
        res = res.filter(types=types)
    if status != None:
        res = res.filter(status=status)
    if location != None:
        res = res.filter(location=location)
    if gte != None:
        res = res.filter(capacity__gte=float(gte))
    if lte != None:
        res = res.filter(capacity__lte=float(lte))
    res = [ x for x in res.values() ]
    return {"ressources": res}


def removeEnergyResource(eid:str)->None:
    """
        Function to remove an Energy resource (in table).
        input:
            eid - hash of the Energy Resource
        output:
            None
        opt.
    """
    res = EnergyResource.objects.filter(eid=eid)[0]
    res.delete()
