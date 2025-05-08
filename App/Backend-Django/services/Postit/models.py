from django.db import models

import hashlib

from typing import Dict, List


HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()

class Postit(models.Model):
	"""
		Class to implement the model of a Postit (in database).
	"""
	uid = models.CharField(max_length=255)
	iid = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	time = models.CharField(max_length=255)
	memo = models.CharField(max_length=1025)
	img = models.CharField(max_length=655)
	
	

def getPostitsAllModel()->List[Dict[str, str]]:
	"""
		Function to get all Postits (in database).
			input:
				None
			output:
				Postits (in database)
		opt.
	"""
	res = [ x for x in Postit.objects.all().values()]
	return res
	


def createPostitModel(uid:str, title:str, time:str, memo:str, img:str)->bool:
	"""
		Function to create a Postit (for a User).
			input:
				uid:str, title:str, time:str, memo:str, img:str
			output:
				True if Postit created, False otherwise
		opt.
	"""
	if Postit.objects.filter(uid=uid, iid=HASH(title+time)).values().exists():
		# remove from database - if already exists
		removePostitModel(uid, HASH(title+time))
	res = Postit(uid=uid, iid=HASH(title+time), title=title, time=time, memo=memo, img=img)
	res.save()
	return True
	

def getPostitModel(uid:str, iid:str)->Dict[str, str]:
	"""
		Function to get a Postit.
			input:
				uid, iid - user id, postit id
			output:
				Postit (with uid and iid)
		opt.
	"""
	if not Postit.objects.filter(uid=uid, iid=iid).values().exists():
		return {}
	resp = Postit.objects.filter(uid=uid, iid=iid).values()[0]
	return resp
	

def getPostitsModel(uid:str)->Dict[str, str]:
	"""
		Function to get (all) Postits (for a User).
			input:
				uid - user id
			output:
				Postits (for a User)
		opt.
	"""
	if not Postit.objects.filter(uid=uid).values().exists():
		return {}
	#res = Postit.objects.filter(uid=uid).values()	
	res = [ x for x in Postit.objects.filter(uid=uid).values() ]
	return res
	
def removePostitModel(uid:str, iid:str)->bool:
	"""
		Function to remove a Postit.
			input:
				uid, iid - user id, postit id
			output:
				True if done, False otherwise
		opt.
	"""
	if not Postit.objects.filter(uid=uid, iid=iid).values().exists():
		return False
	for res in Postit.objects.filter(uid=uid, iid=iid):
		res.delete()
	return True

def removePostitsModel(uid:str)->None:
	"""
		Function to remove (all) Postits (for a User).
			input:
				uid - user id
			output:
				True if done, False otherwise
		opt.
	"""
	if not Postit.objects.filter(uid=uid).values().exists():
		return False
	for res in Postit.objects.filter(uid=uid):
		res.delete()
	return True


