from django.core.management.base import BaseCommand



class Command(BaseCommand):
	"""
		Class to implement the .... command.
		args:
			python3 manage.py ....
	"""
	def add_arguments(self, parser):
		#parser.add_argument('arg1')
		pass
		
	def handle(self, *args, **options):	
		pass
			
