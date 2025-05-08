import os
import sys
import csv
import mysql.connector

from typing import List, Tuple, Union

#sys.path.insert(1, './module')
from data import read_file_windows, read_json



    
def get_table_name(folder:str, filename:str)->Tuple[str]:
    """
        function to get name of a Table.
        input: 
            filename - name of the file 
        output: 
            name (ACL, PsyndDemo ..etc)
            datatype (users, rights, groups, graph)
            name of the Table (to create)
    
    """
    name = os.path.basename(os.path.normpath(folder)) # if ACL, PsyndDemo ...etc
    datatype = filename.split(".")[0].split("_")[-1] # if user, rights, groups
    return name, datatype, "{}{}".format(name, datatype)
    

def create_table(name:str, datatype:str)->str:
    """
        function to create a Table (in database).
        input: 
            name - name of the Table to create
            datatype - (users, rights, groups, graph)
        output: 
            None
    
    """
    db = read_json("./config.json")
    database = mysql.connector.connect(
      host=db["DATABASE"]["HOST"], #"192.168.205.148",
      user=db["DATABASE"]["USERNAME"], #"lbeh",
      password=db["DATABASE"]["PASSWORD"], #"Access2Tree",
      database=db["DATABASE"]["DB"], #"treerole"
    )
    
    cursor = database.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS {}".format(name))
    
    
    match datatype:
        case "groups":
            #query to create table for groups
            query = "CREATE TABLE {} {});".format(name, "(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(1000), nbOfusers INT, nbOfrights INT")
        case "rights":
            # query to create table for rights
            query = "CREATE TABLE {} {});".format(name, "(groupname VARCHAR(1000), typeofright VARCHAR(1000)")
        case "users":
            # query to create table for users
            query = "CREATE TABLE {} {});".format(name, "(groupname VARCHAR(1000), user VARCHAR(1000)") 
            
        case "graph":
            #query to create table for Nodes (of graph)
            query = "CREATE TABLE {} {});".format(name, "(nodeParent VARCHAR(1000), nodeChild VARCHAR(1000), probability FLOAT")
                
        case _:
            raise Exception("[-] Error: Unkonown type of data ({}) for this database.".format(datatype)) 
    
    cursor.execute(query)
    
    cursor.close()
    database.close()
    return name


def insert(tablename:str, datatype:str, data:List[List[str]])->None:
    """
        function to insert (data) in a Table of the database.
        input: 
            tablename - name of the Table 
            datatype - (users, rights, groups, graph)
            data - 
        output: 
            None
    
    """
    db = read_json("./config.json")
    database = mysql.connector.connect(
      host=db["DATABASE"]["HOST"], #"192.168.205.148",
      user=db["DATABASE"]["USERNAME"], #"lbeh",
      password=db["DATABASE"]["PASSWORD"], #"Access2Tree",
      database=db["DATABASE"]["DB"], #"treerole"
    )
    
    cursor = database.cursor()
    
    print("\n\n\nINSERT into {}".format(tablename))
    for x in data: 
        #print(x)
        
            
        match datatype:
            case "groups":
                # insert into table for groups
                query = "INSERT INTO {} (name, nbOfusers, nbOfrights) VALUES ({}, {}, {});".format(tablename, x[0], int(x[1]), int(x[2]))
                
            case "users":
                # insert into table for users
                query = 'INSERT INTO {} (groupname, user) VALUES("{}", "{}");'.format(tablename, x[0], x[1])
               
            case "rights":
                # insert into table for rights
                query = 'INSERT INTO {} (groupname, typeofright) VALUES("{}", "{}");'.format(tablename, x[0], x[1])

            case "graph":
                # insert into table for Nodes (of graph)
                query = 'INSERT INTO {} (nodeParent, nodeChild, probability) VALUES("{}", "{}", "{}");'.format(tablename, x[0], x[1], float(x[2]))
                
            case _:
                raise Exception("[-] Error: Unkonown type of data ({}) for this database.".format(datatype))    
        
        cursor.execute(query)
        database.commit()


    print("\nSELECT * from Table")
    cursor.execute("SELECT * FROM {}".format(tablename))
    myresult = cursor.fetchall()
    for x in myresult:
      print(x)

    cursor.close()
    database.close()
    return None
 


def remove():
    """
        function to remove (data) in a Table of the database.
        input: 
            tablename - 
            datatype - (users, rights, groups, graph)
            data - 
        output: 
            None
    
    """
    return 0


    
    
def update(folder:str, filename:str)->None:
    """
        function to create and insert (data) in a Table of the database.
        input: 
            filename - name of the file (containing the data to insert in database)
        output: 
            None
    
    """
    
    datafile = os.path.join(folder, filename) 
    
    print(datafile)
    
    
    # read file
    data = read_file_windows(datafile)    
     
    # create table
    name, datatype, tablename = get_table_name(folder, filename)
    print(name, datatype, tablename)
    flag = create_table(tablename, datatype)
   
    # insert data
    insert(tablename, datatype, data)
 
    # delete data 
    # remove()
   
    return None
 
    

def func(path:str)->None:

    for filename in ["csv_users.csv", "csv_rights.csv", "csv_groups.csv", "csv_graph.csv"]:
        print("\n\n\n")
        update(path, filename)
        #input()
        
    return None

  

   
   
   
 
