import os.path
import csv
import sqlite3
import hashlib

from services.config import PATH

from typing import List, Tuple, Optional, Any

HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()

DATABASEUSER = os.path.join(PATH, "users.db")
USERS = "Users"
FAVORITES = "Favorites"

def drop(table:str)->sqlite3.Cursor:
	return request(f"DROP TABLE IF EXISTS {table};", False)
	

def create(table:str, columns:str)->sqlite3.Cursor:
	drop(table)
	return request(f"CREATE TABLE {table} ({columns})", False)
	
	
def insert(table:str, values:Tuple[Any])->sqlite3.Cursor:
	return request(f"INSERT INTO {table} VALUES {values}", False)
	
	
def delete(table:str, condition:str)->sqlite3.Cursor:
	return request(f"DELETE FROM {table} WHERE {condition}", False)


def select(table:str, value:str)->sqlite3.Cursor:
	return request(value, True)
	

def request(value:str, verbose:bool)->List[Tuple[Any]]: #sqlite3.Cursor:
	db = sqlite3.connect(DATABASEUSER)
	cursor = db.cursor()
	
	rows = cursor.execute(value)
	x = list(rows)
	#if verbose:
		#for row in rows:
			#print(f"\n{row}")
	
	db.commit()
	db.close()
	return x		


