from services.database.database import *

from typing import Tuple, Dict

def loginUser(email:str, password:str)->str:
	""" Function to ... """
	x = select(f'''SELECT * FROM {USERS} WHERE Email="{email}"''')
	for row in x:
		if row[3] == HASH(password):
			return row[0]
	return ""


def getUserInfo(key:str, value:str)->Dict[str, str]:
	""" Function to get informations of a user. """
	x = select(f'''SELECT * FROM {USERS} WHERE {key}="{value}"''')
	user = {}
	if x != []:
		x = x[0]
		user["hash"] = x[0]
		hashs = x[0]
		user["email"] = x[1]
		user["username"] = x[2]
		user["password"] = x[3]
	x = select(f'''SELECT Location FROM {FAVORITES} WHERE User="{x[0]}"''')
	user["favorites"] = []
	if x != []:
		user["favorites"] = [xi[0] for xi in x]
	return user
	

##################################################################################################
# Users	

def exists(key:str, value:str, *args:Tuple[str])->bool:
	""" Function to check if a user exists (in database). """
	x = select(f'''SELECT * FROM {USERS} WHERE {key}="{value}"''')
	if key == "Email" and args != ():
		for row in x:
			if row[2] == args[0]:
				return True
				
	if (key == "Email" and args == ()) or (key == "Username"):
		if x != []:
			return True
	return False


def createUser(email:str, username:str, password:str)->None:
	""" Function to add a user (in database). """
	insert(USERS, (HASH(email), email, username, HASH(password)))
	

def updateUser(uid:str, key:str, value:str)->str:
	""" Function to update user informations (in database). """
	def UpdateUsername(uid:str, key:str, value:str)->str:
		x = f'''UPDATE {USERS} SET {key} = "{value}" WHERE Hash = "{uid}";'''
		x = request(x)
		return uid
		
	def UpdateEmail(uid:str, key:str, value:str)->str:
		new = HASH(value)
		x = f'''UPDATE {USERS} SET {key} = "{value}", Hash = "{new}" WHERE Hash = "{uid}";'''
		# change hash also for FAVORITES (table)
		x = request(x)
		x = f'''UPDATE {FAVORITES} SET {User} = "{new}" WHERE Hash = "{uid}";'''
		x = request(x)
		return new
		
	def UpdatePassword(uid:str, key:str, value:str)->str:
		new = HASH(value)
		x = f'''UPDATE {USERS} SET {key} = "{new}" WHERE Hash = "{uid}";'''
		x = request(x)
		return uid

	if key == "Email":
		return UpdateEmail(uid, key, value)
	if key == "Password":
		return UpdatePassword(uid, key, value)
	return UpdateUsername(uid, key, value)


##############################################################################################
# Favorites

def exist(ids:str, uid:str)->bool:
	""" Function to check if a favorite place exists (in database). """
	x = select(f'''SELECT * FROM {FAVORITES} WHERE Location="{ids}" AND User="{uid}"''')
	if x != []:
		return True
	return False

def favorites(uid:str, ids:str)->None:
	""" Function to add a favorite Location for a user. """
	insert(FAVORITES, (uid, ids))
	

def remove_favorite(uid:str, ids:str):
	value = f'''DELETE FROM {FAVORITES} WHERE Location="{ids}" AND User="{uid}"'''
	if exist(ids, uid):
		#delete(FAVORITES, f'''User="{uid}" AND Location="{ids}"''')
		db = sqlite3.connect(DATABASE)
		cursor = db.cursor()
		
		rows = cursor.execute(value)
		x = list(rows)
		
		db.commit()
		db.close()



