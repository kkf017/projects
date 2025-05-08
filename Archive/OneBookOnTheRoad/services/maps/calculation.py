import csv
import math

from services.database.database import *
from services.maps.geography import Location, coordinates, euclidean, mappy

from typing import List, Dict, Union

	
	
def filters(key:str, value:str)->List[str]:	
	""" Function to get paces accordind to filters."""
	request = f'''SELECT * FROM {LOCATION} WHERE {key}="{value}" ORDER BY Region,Department,Municipality,Town;'''
	
	if key == None and value == None:
		return []
		
	result = []
	for row in select(request):
		new = {}
		new["Hash"] = row[0]
		new["Address"] = row[1]
		result.append(new)
		
	return result

def searchID(value:str):
	""" Function to search a place and get its map."""
	request = f'''SELECT * FROM {LOCATION} WHERE Hash="{value}";'''
	result = []
	for row in select(request):
		new = {}
		new["Hash"] = row[0]
		new["Address"] = row[1]
		new["street"] = row[2]
		new["Town"] = row[3]
		new["Municipality"] = row[4]
		new["Department"] = row[5]
		new["Region"] = row[6]
		new["Postcode"] = row[7]
		new["Country"] = row[8]
		new["Latitud"] = row[9]
		new["Longitud"] = row[10]
		
		mappy(row[0], (row[9], row[10]))
		result.append(new)
		
	return result[0]

def sphere(location:str, radius:float)->Dict[str, List[Dict[str, Union[str, float]]]]:
	""" Function to find th nearest places - according to a radius -."""
	addr, latitud, longitud = coordinates(location)
	if (addr == None and latitud == None and longitud == None):
		return []
	loc1 = Location(addr, latitud, longitud)
	
	const = loc1.nearest(radius)
	rad = math.pi / 180
	request = f"SELECT Hash, Name, Latitud, Longitud FROM {LOCATION} a WHERE ( {const} <= {loc1.x} * cos(a.latitud * {rad}) * cos(a.longitud * {rad}) + {loc1.y} * cos(a.latitud * {rad}) * sin(a.longitud * {rad}) + {loc1.z} * sin(a.latitud * {rad}) )"
	
	result = []
	for row in select(request):
		new = {}
		loc2 = Location(row[1], float(row[2]), float(row[3]))
		new["Hash"] = row[0]
		new["Address"] = row[1]
		new["distance"] = '{:.2f}'.format(euclidean(loc1,loc2))
		result.append(new)
	
	solution = {}
	solution["Location"] = loc1.addr
	solution["result"] = result
	return solution
			
	
	
