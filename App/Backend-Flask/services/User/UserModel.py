"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for User Model.
                (functions to create, update, and remove users - (Table (User) in database))

                    # To (...):
                        # Forget password
-----------------------------------------------------------------------------------------------------------------"""

from services.database.database import *

from typing import Dict


TABLE_USER = "User"


def createTableUser()->None:
    """ 
        Function to create a Table for Users (in database).
            input:
                None
            output:
                None
       opt.
    """
    value = request(f"DROP TABLE IF EXISTS {TABLE_USER};")
    value = request(f"CREATE TABLE {TABLE_USER} (uid, Email, Password);")

    


def createUserModel(email:str, password:str)->None:
    """ 
        Function to create a User in Table.
            input:
                email, password - informations of user
            output:
                None
       opt.
    """
    value = request(f"INSERT INTO {TABLE_USER} VALUES {(HASH(email), email, HASH(password))};")



def existUserModel(email:str, flag:bool=True)->bool:
    """ 
        Function to check if a User exists (in database).
            input:
                email - informations of user
            output:
                boolean
       opt.
    """
    if flag:
    	email = HASH(email)
    value = request(f'''SELECT * FROM {TABLE_USER} WHERE uid="{email}";''')
    if not (value == []):
        return True
    return False



def selectUserModel(email:str)->Dict[str, str]:
    """ 
        Function to select a User from its email (in database).
            input:
                email, password - informations of user
            output:
                User
       opt.
    """
    value = request(f'''SELECT * FROM {TABLE_USER} WHERE uid="{HASH(email)}";''')
    if value == []:
        return {}
    return {"uid": value[0][0], "email": value[0][1], "password": value[0][2]}


def getUserModel(uid:str)->Dict[str, str]:
    """ 
        Function to get a User from its id (in database).
            input:
                uid - id of user
            output:
                User
       opt.
    """
    value = request(f'''SELECT * FROM {TABLE_USER} WHERE uid="{uid}";''')
    if value == []:
        return {}
    return {"uid": value[0][0], "email": value[0][1], "password": value[0][2]}




def updateEmailUserModel(uid:str, email:str)->None:
    """ 
        Function to update email (in database).
            input:
                uid, email - informations of user, (email to update)
            output:
                boolean
       opt.
    """
    value = request(f'''UPDATE {TABLE_USER} SET Email = "{email}", uid = "{HASH(email)}" WHERE uid = "{uid}";''')



def updatePasswordUserModel(uid:str, password:str)->None:
    """ 
        Function to update password (in database).
            input:
                uid, password - informations of user, (password to update)
            output:
                boolean
       opt.
    """
    value = request(f'''UPDATE {TABLE_USER} SET Password = "{HASH(password)}" WHERE uid = "{uid}";''')
 
   

def removeUserModel(uid:str)->None:
    """ 
        Function to remove User (in database).
            input:
                uid - informations of user, (password to update)
            output:
                boolean
       opt.
    """
    value = request(f'''DELETE FROM {TABLE_USER} WHERE uid = "{uid}";''')
    



