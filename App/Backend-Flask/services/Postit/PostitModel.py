"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for Postit Model.

-----------------------------------------------------------------------------------------------------------------"""

from services.database.database import *

from typing import Dict


TABLE_POSTIT = "Postit"



# display Postits - for a user (uid) (ok)
# display a Postit - for iid (ok)
# remove a Postit
# Create a new Postit (ok)

# Update a Postit


def createTablePostit()->None:
    """ 
        Function to create a Table for Postit(s) (in database).
            input:
                None
            output:
                None
       opt.
    """
    request(f"DROP TABLE IF EXISTS {TABLE_POSTIT};")
    request(f"CREATE TABLE {TABLE_POSTIT} (uid, iid, Title, Time, Memo, img);")



def createPostitModel(uid:str, title:str, time:str, memo:str, img:str)->None:
    """ 
        Function to create a Postit in Table.
            input:
                uid, title, time, memo, img - informations of Postit
            output:
                None
       opt.
    """
    value = request(f"INSERT INTO {TABLE_POSTIT} VALUES {uid, HASH(title+time), title, time, memo, img};")


def getPostitModel(uid:str, iid:str)->Dict[str, str]:
    """ 
        Function to get a Postit from its id (in database).
            input:
                uid, iid - id of postit
            output:
                Postit
       opt.
    """
    value = request(f'''SELECT * FROM {TABLE_POSTIT} WHERE uid="{uid}" AND iid="{iid}";''')
    if value == []:
        return {}
    return {"uid": value[0][0], "iid": value[0][1], "title": value[0][2], "time": value[0][3], "memo": value[0][4], "img": value[0][5]}


def getPostitsModel(uid:str)->Dict[str, str]:
    """ 
        Function to get a Postits from its User uid (in database).
            input:
                uid - id of postit
            output:
                Postit
       opt.
    """
    values = request(f'''SELECT * FROM {TABLE_POSTIT} WHERE uid="{uid}";''')
    if values == []:
        return {}
    return [{"uid": value[0], "iid": value[1], "title": value[2], "time": value[3], "memo": value[4], "img": value[5]} for value in values]


def removePostitModel(uid:str, iid:str)->None:
    """ 
        Function to remove Postit (in database).
            input:
                uid, iid - informations of user, (password to update)
            output:
                boolean
       opt.
    """
    value = request(f'''DELETE FROM {TABLE_POSTIT} WHERE uid = "{uid}" AND iid="{iid}";''')


def removePostitsModel(uid:str)->None:
    """ 
        Function to remove Postit for a User (in database).
            input:
                uid - informations of user, (password to update)
            output:
                boolean
       opt.
    """
    value = request(f'''DELETE FROM {TABLE_POSTIT} WHERE uid = "{uid}";''')




