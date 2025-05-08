from django.core.management.base import BaseCommand


from EnergyResource.models import *



class Command(BaseCommand):
    """
        Class to implement the clear_database command.
        args:
            python3 manage.py clear_database
    """
    def handle(self, *args, **options):
        for x in getEnergyResourcesModel()["ressources"]:
            removeEnergyResource(x["eid"])
            
