import os
import math
import geopy
import folium

from typing import Tuple, Union

#https://www.boites-a-livres.fr/

# pip install geopy
# pip3 install folium
# pip install googlesearch-python

LANGUAGE = "eng"
R = 6371 # radius of Earth 


"""
	
	Module to (...)
	
"""	

class Location:
	""" Class containing informations about a location. """
	def __init__(self, location:str, latitud:float, longitud:float)->None:
		self.addr, self.latitud, self.longitud = (location, latitud, longitud)
		
		self.x, self.y, self.z = self.CoordSphere(self.latitud, self.longitud)
		
	def CoordSphere(self, delta:float, phi:float)->Tuple[float]:
		""" Function to compute spherical coordinates of a point. """
		radian = lambda degree: degree * math.pi / 180
		
		delta, phi = (radian(delta), radian(phi))
				
		x = R * math.cos(delta) * math.cos(phi)
		y = R * math.cos(delta) * math.sin(phi)
		z = R *  math.sin(delta)
		return (x, y, z)


	def nearest(self, radius:float)->Tuple[float]:
		""" Function to compute .... """
		return (R**2 - (radius**2 - (self.x**2+self.y**2+self.z**2))) / (2*R) #(loc1.x, loc1.y, loc1.z, const)



def coordinates(location:str)->Tuple[Union[str, float]]:
	""" Function to get coordinates of a location. """
	try:	
		coder = geopy.geocoders.Nominatim(user_agent="GetLoc")
		loc = coder.geocode(location, language=LANGUAGE, addressdetails=True)
	except geopy.exc.GeopyError: #geopy.exc.GeocoderTimedOut:
		print("Error: geocode failed with message %s"%("geopy.exc.GeocoderTimedOut"))
		loc = None
	if loc == None:
		return (None, None, None)
	return (loc.address, loc.latitude, loc.longitude)



def euclidean(loc1:Location, loc2:Location)->float:
	""" Function to compute ...(km) between two points. """
	x1, y1, z1 = (loc1.x, loc1.y, loc1.z)
	x2, y2, z2 = (loc2.x, loc2.y, loc2.z)
	return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def mappy(name:str, point:Tuple[float]):
	""" Function to create a map (with folium library) """
	if not os.path.exists(f"./static/maps/{name}.html"):
		matlon = [point]
		mapit = folium.Map( location=point, zoom_start=6 ) #None
		for coord in matlon:
		   folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )	  
		mapit.save(f"./static/maps/{name}.html")


