"""-----------------------------------------------------------------------------------------------------------------

            File that contains functions for Database Management.

-----------------------------------------------------------------------------------------------------------------"""

import os.path
import sqlite3
import hashlib

from services.config import *

from typing import List, Tuple, Optional, Any


DATABASE = 'database.db' #os.path.join(PATH, 'database.db')

HASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()


	
def request(value:str)->List[Tuple[Any]]:
    """ 
        Function to execute a query (SQL).
            input:
                value - query to execute
            output:
                result (of request)
       opt.
    """
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    
    rows = cursor.execute(value)
    x = list(rows)

    db.commit()
    db.close()
    return x		




