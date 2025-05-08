from services.database.database import *

FOLDER = "/home/kkf/Repositories/Archive"

def CreateTableLocation():
	drop(LOCATION)
	create(LOCATION,"Hash, Name, Address, Town, Municipality, Department, Region, Postcode, Country, Latitud, Longitud")


def CreateTableUsers():
	drop(USERS)
	create(USERS,"Hash, Email, Username, Password")
	create(FAVORITES,"User, Location")
	

def  FillTableLocation():
	with open(f"{FOLDER}/Project3/data/deparments.txt", encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for filename in reader:
			filename = f"{FOLDER}/Project3/data/{filename[0]}/{filename[0]}.csv"
			print(f"\033[33m{filename}\033[00m")
			populate(filename, LOCATION)
			#select(table, f"SELECT DISTINCT Department FROM {LOCATION}")
			#input()	

	
def FillTableUsers():
	username = "smililly"
	email = "smililly@yahoo.com"
	password = "smililly<3LOVEsU"
	insert(USERS, (HASH(email), email, username, HASH(password)))
		
	username = "summer85"
	email = "summer.85@yahoo.com"
	password = "summer:)85"
	insert(USERS, (HASH(email), email, username, HASH(password)))


if __name__ == "__main__":
	
	#CreateTableLocation()
	#CreateTableUsers()
	
	#FillTableLocation()
	#FillTableUsers()
	
	#for x in select(f'''SELECT * FROM {LOCATION}'''):
		#print("\n",x)

	print("\n\n\n")
	input()
	
	for x in select(f'''SELECT * FROM {USERS}'''):
		print("\n",x)
		
	print("\n\n\n")
	input()
	
	for x in select(f'''SELECT * FROM {FAVORITES}'''):
		print("\n",x)
	
