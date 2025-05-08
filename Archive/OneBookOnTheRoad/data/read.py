import os
import csv
import hashlib
import geopy

HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()

#from services.database import *

from typing import Tuple, Dict, Union



def readtxt(filename:str)->None:
	""" Function to read a .txt file. """
	if os.path.exists(f"{filename}.csv"):
		os.remove(f"{filename}.csv")
			
	if os.path.exists(f"{filename}-err.csv"):
		os.remove(f"{filename}-err.csv")
		
	with open(f"{filename}.txt", 'r') as f:
		for line in f.readlines():
			add(filename, line)


def readCSV(filename:str)->None:
	""" Function to read a .csv file. """
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			print(f"\n\n")
			for i in range(len(row)):
				print(f"{i} - {row[i]}")	
		
			
def writeCSV(filename:str, *args:Tuple[Union[str, float]])->None:
	""" Function to write .csv file. """
	print(f"\033[31mCSV -> {filename}\033[00m")		
	with open(filename, 'a', encoding='utf8') as fp:
        	writer = csv.writer(fp, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
        	writer.writerow(args)


def coordinates(location:str)->Dict[str, str]:
	""" Function to get coordinates of a location. """
	def dictionnary(location:Dict[str, str], address:str, latitud:float, longitud:float)->Dict[str, str]:
		x={"house_number": "", "road": "", "town": "", "municipality": "", "county": "", "state": "", "region": "", "postcode": "", "country": ""}
		for key in location.keys():
			if not key in ["ISO3166-2-lvl6", "ISO3166-2-lvl4"]:
				x[key] = location[key]
		x["name"] = address
		x["latitud"] = latitud
		x["longitud"] = longitud
		return x
	LANGUAGE = "eng"
	try:	
		coder = geopy.geocoders.Nominatim(user_agent="GetLoc")
		loc = coder.geocode(location, language=LANGUAGE, addressdetails=True)
	except geopy.exc.GeopyError: 
		print("Error: geocode failed with message %s"%("geopy.exc.GeocoderTimedOut"))
		loc = None
	if loc == None:
		return {}
	return dictionnary(loc.raw['address'], loc.address, loc.latitude, loc.longitude)
	
	

def add(filename:str, x:str)->None:
	""" Function to commit ... """	
	location = coordinates(x)
	if not location == {}:
		print(f"\n\n{x}")
		
		for key in location.keys():
			print("{}: {}".format(key, location[key]))
		
		writeCSV(f"{filename}.csv", HASH(location["name"]), location["name"],location["house_number"], location["road"], location["town"], location["municipality"], location["county"], location["state"], location["postcode"], location["country"], location["latitud"], location["longitud"])
	else:
		print(f"\n\nERREUR !! - {x}")
		writeCSV(f"{filename}-err.csv", x)
		


def populate(filename:str, name:str)->None:
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			#insert(name, (row[0], float(row[1]), float(row[2])))
			insert(name, (row[0], row[1], f"{row[2]} {row[3]}", row[4], row[5], row[6], row[7], row[8], row[9], float(row[10]), float(row[11])))


if __name__ == "__main__":

	"""
	with open("deparments.txt", 'r') as f:
		for line in f.readlines():
			print(f"\033[35m\n\n\n************************************************************\033[00m")
			print(f"\033[34m\t./{line[:-1]}/{line[:-1]}.txt\033[00m")
			print(f"\033[35m************************************************************\033[00m")
			filename = f"./{line[:-1]}/{line[:-1]}"
			readtxt(filename)
			readCSV(f"{filename}.csv")
			print(f"\033[34m\n\n\nEnd.\033[00m")
			#input()
	"""
			
	#filename = "zExceptions"
	#readtxt(filename)
	#readCSV(f"{filename}.csv"
	
	# fill exceptions - for each location (from LOC-err.csv)
	
	#drop(table)
	#create(table, "Address, Latitud, Longitud")
	#create(table,"Hash, Name, Address, Town, Municipality, Department, Region, Postcode, Country, Latitud, Longitud")
	
	#populate("Haute-Savoie.csv", table)
	
	# Correct HTML with departments, regions ..etc
	#select(table, f"SELECT * FROM {table}")
	#select(table, f"SELECT * FROM {TABLE} ORDER BY Region,Department,Municipality,Town")
	

