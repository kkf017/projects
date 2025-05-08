import json
import mysql.connector

from typing import List, Dict, Union

def read_json(filename:str) -> Dict[str, Union[str, int]]:
    """
        function to read .json file.
        input: 
            filename - name of the file to read
        output: 
            None
    
    """
    with open(filename, "r") as f:
        return json.load(f)
        

if __name__ == "__main__":


    db = read_json("./config.json")
    database = mysql.connector.connect(
      host=db["DATABASE"]["HOST"], 
      user=db["DATABASE"]["USERNAME"], 
      password=db["DATABASE"]["PASSWORD"], 
      database=db["DATABASE"]["DB"], 
    )

    print(database)
    cursor = database.cursor()
   
  
    print("\n\nSHOW TABLES (before DROP)")
    cursor.execute("SHOW TABLES")   # How to remove ?
    for x in cursor:
        print(x)
   
  
    print("\nSet name of Tables to drop:")
    name = input()
    
    cursor.execute("DROP TABLE IF EXISTS {}".format("{}users".format(name)))
    cursor.execute("DROP TABLE IF EXISTS {}".format("{}rights".format(name)))
    cursor.execute("DROP TABLE IF EXISTS {}".format("{}groups".format(name)))
    cursor.execute("DROP TABLE IF EXISTS {}".format("{}graph".format(name)))
   
    
    print("\n\nSHOW TABLES (after DROP)")
    cursor.execute("SHOW TABLES")  
    for x in cursor:
        print(x)
  
   
    cursor.close()
    database.close()
