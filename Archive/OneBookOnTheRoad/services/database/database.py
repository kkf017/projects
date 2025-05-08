import os.path
import csv
import sqlite3
import hashlib

from services.config import PATH

from typing import List, Tuple, Optional, Any


DATABASE = os.path.join(PATH, 'database.db')
LOCATION = "Location"

HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()

USERS = "Users"
FAVORITES = "Favorites"


def drop(table:str)->sqlite3.Cursor:
	return request(f"DROP TABLE IF EXISTS {table};")	
	

def create(table:str, columns:str)->sqlite3.Cursor:
	drop(table)
	return request(f"CREATE TABLE {table} ({columns})")
	
	
def insert(table:str, values:Tuple[Any])->sqlite3.Cursor:
	return request(f"INSERT INTO {table} VALUES {values}")
	
	
def delete(table:str, condition:str)->sqlite3.Cursor:
	return request(f"DELETE FROM {table} WHERE {condition}")
	

def select(value:str)->sqlite3.Cursor:
	return request(value)


def update(table:str, ):
	pass
	
	
def request(value:str)->List[Tuple[Any]]: #sqlite3.Cursor:
	db = sqlite3.connect(DATABASE)
	cursor = db.cursor()
	
	rows = cursor.execute(value)
	x = list(rows)
	
	db.commit()
	db.close()
	return x		




def populate(filename:str, name:str)->None:
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			#insert(name, (row[0], float(row[1]), float(row[2])))
			insert(name, (row[0], row[1], f"{row[2]} {row[3]}", row[4], row[5], row[6], row[7], row[8], row[9], float(row[10]), float(row[11])))	
				


