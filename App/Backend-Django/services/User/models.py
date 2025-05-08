from django.db import models

import hashlib

from typing import Dict, List


HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()


class User(models.Model):
	"""
		Class to implement the model of a User (in database).
	"""
	uid = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)


def getUsersModel()->List[Dict[str, str]]:
	"""
		Function to get all Users (in database).
			input:
				None
			output:
				Users (in database)
		opt.
	"""
	res = [ x for x in User.objects.all().values()]
	return res
	
	

def createUserModel(email:str, password:str)->bool:
	"""
		Function to create a User (in database).
			input:
				email, password - informations of user
			output:
				True if User created, False otherwise
		opt.
	"""
	if User.objects.filter(uid=HASH(email)).values().exists():
		return False
	res = User(uid=HASH(email), email=email, password=HASH(password))
	res.save()
	return True

def existUserModel(email:str, password:str)->bool:
	"""
		Function to check if a user exists (in database).
			input:
				email, password - informations of user 
			output:
				True if User exists, False otherwise
		opt.
	"""
	if User.objects.filter(uid=HASH(email)).values().exists() and User.objects.filter(uid=HASH(email)).values()[0]["password"]==HASH(password):
		return True
	return False
		
def getUserModel(uid:str)->Dict[str, str]:
	"""
		Function to get a User (from its uid).
			input:
				uid - id of the user
			output:
				User
		opt.
	"""
	if not User.objects.filter(uid=uid).values().exists():
		return {}
	resp = User.objects.filter(uid=uid).values()[0]
	return resp

def updateEmailUserModel(uid:str, email:str)->bool:
	"""
		Function to update email (User).
			input:
				uid, email - id of user, email to update
			output:
				True if done, False otherwise
		opt.
	"""
	if not User.objects.filter(uid=uid).values().exists():
		return False
	resp = User.objects.filter(uid=uid)[0]
	resp.email = email
	resp.uid = HASH(email)
	resp.save()
	return True
	
def updatePasswordUserModel(uid:str, password:str)->bool:
	"""
		Function to update password (User).
			input:
				uid, password - id of user, password to update
			output:
				True if done, False otherwise
		opt.
	"""
	if not User.objects.filter(uid=uid).values().exists():
		return False
	resp = User.objects.filter(uid=uid)[0]
	resp.password = HASH(password)
	resp.save()
	return True
	
def removeUserModel(uid:str)->bool:
	"""
		Function to remove a User (in database).
			input:
				uid - user id
			output:
				True if done, False otherwise
		opt.
	"""
	if not User.objects.filter(uid=uid).values().exists():
		return False
	res = User.objects.filter(uid=uid)[0]
	res.delete()
	return True

