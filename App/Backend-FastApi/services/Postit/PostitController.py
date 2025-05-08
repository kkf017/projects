"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for Postit Controller.

-----------------------------------------------------------------------------------------------------------------"""

from services.database.database import HASH
from services.Postit.PostitModel import *

from typing import Dict


def createPostitController(uid:str, title:str, time:str, memo:str, img:str)->None:
    """ 
        Function to create a Postit (in database).
            input:
                uid, title, time, memo, img - informations of Postit
            output:
                None
       opt.
    """
    createPostitModel(uid, title, time, memo, img)



def getPostitController(uid:str, iid:str)->Dict[str, str]:
    """ 
        Function to get a Postit from§ its id (in database).
            input:
                uid, iid - id of postit
            output:
                Postit
       opt.
    """
    return getPostitModel(uid, iid)


def getPostitsController(uid:str)->Dict[str, str]:
    """ 
        Function to get a Postits from its User uid (in database).
            input:
                uid - id of postit
            output:
                Postit
       opt.
    """
    return getPostitsModel(uid)



def removePostitController(uid:str, iid:str)->bool:
    """ 
        Function to remove Postit (in database).
            input:
                uid, iid - informations of user, (password to update)
            output:
                boolean
       opt.
    """
    if getPostitModel(uid, iid) == {}:
        return False
    removePostitModel(uid, iid)
    return True


def removePostitsController(uid:str)->bool:
    """ 
        Function to remove Postit for a User (in database).
            input:
                uid, iid - informations of user, (password to update)
            output:
                boolean
       opt.
    """
    if getPostitsModel(uid) == {}:
        return False
    removePostitsModel(uid)
    return True
