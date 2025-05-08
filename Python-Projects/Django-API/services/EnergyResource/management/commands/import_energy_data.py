from django.core.management.base import BaseCommand

import csv
from typing import List

from EnergyResource.models import createEnergyResource



class Command(BaseCommand):
    """
        Class to implement the import_energy_data command.
        args:
            python3 manage.py import_energy_data [filename]
    """
    def add_arguments(self, parser):
        parser.add_argument('arg1')

    def handle(self, *args, **options):

        def read_csv(filename:str)->List[List[str]]:
            with open(filename) as csv_file:
                data = [ row for row in csv.reader(csv_file, delimiter=',') if row != []]
                return data[1:]

        filename = options["arg1"]
        for x in read_csv(filename):
            createEnergyResource(x[0], x[1], float(x[2]), x[3], x[4])
            
