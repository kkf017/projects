import hashlib
import requests
from urllib.request import urlretrieve
from datetime import datetime

from typing import List, Dict, Union

N = 12
HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()
API_KEY = "pTeCTuKyjgeJie7BkwIuFnTunwuCBXGO3p1Ur6Zp"


class Nasa():
	def __init__(self,n:int=0)->None:
		images = self.get_IMG(n)
	
	def get_IMG(self, n:int)->None:	
		""" Function that get a set of images from API. """
		URL = "https://api.nasa.gov/planetary/apod"
		params = {'api_key':API_KEY, 'count':n}#, 'hd':'True'}
		response = requests.get(URL,params=params).json()

		# check if media type : 'media_type': 'video'
		
		self.images = []
		for resp in response:
			resp["id"] = HASH(resp['url'])
			self.images.append(resp)			
		
		
	def get_image(self, uid:str)->Dict[str, Union[str, Dict[str,str]]]:
		""" Function that get an image (hash)."""
		for img in self.images:
			if img["id"] == uid:
				return img
		return {}
	
	def select(self, x:str, y:str)->List[Dict[str, Union[str, Dict[str,str]]]]:
		""" Function that select images (between two dates). """
		date1 = (None if x == "" else datetime.strptime(x, '%Y-%m-%d').date())
		date2 = (None if y == "" else datetime.strptime(y, '%Y-%m-%d').date())
		if date1 == None and date2 == None:
			return self.images
		img = []
		for image in self.images:
			date = datetime.strptime(image["date"], '%Y-%m-%d').date()
			if (date2 == None and date1 != None and date1<= date) or (date1 == None and date2 != None and date <= date2) or (date2 != None and date1 != None and date1<= date and date <= date2) :
				img.append(image)
		return img
		
		





