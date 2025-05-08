from django.core.management.base import BaseCommand

from User.models import *


class Command(BaseCommand):
	"""
		Class to implement the clear_database_user command.
		args:
			python3 manage.py clear_database_user
	"""
	def add_arguments(self, parser):
		#parser.add_argument('arg1')
		pass
		
	def handle(self, *args, **options):	
		for x in getUsersModel():
			removeUserModel(x["uid"])
			
