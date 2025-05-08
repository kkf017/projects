import sys
import os


from typing import List

sys.path.insert(1, './module')
from data import get_date, write_pickle, read_pickle, read_json
from LDAP import ldap
from preparation import prepare
from algorithm import method
from database import func
from HTMLTable import html_func


def main(name:str, query: str, attributes: List[str])->int:

    if not os.path.isfile('./config.json'):
    	raise Exception("[-] Error: Update configuration file.")
      
    path = "{}/".format(os.path.abspath(name))
    
    
    if not os.path.isdir(path):
        os.mkdir(path)
        #raise Exception("[-] Error: Update directory {}.".format(name))

    
    y = ldap(path, query, attributes)
    # check if ldap query is working - Error
    if y == []:
        raise Exception("[-] Error: Unvalid LDAP query {}.".format(y))
    
    y = prepare(path, y) 
    
    #algorithm
    method(path, y)
    
    #func(path)
    
    #add func HTML
    html_func(path)
    
    return 1


if __name__ == "__main__" :

    if not os.path.isfile('./demo.json'):
        raise Exception("[-] Error: Update demo file.")
    
    
    demo = read_json('./demo.json')
    name = demo['PROFILE']['NAME']   
    query =  demo['PROFILE']['QUERY'] #'(sn=*PsyndDemo)', '(sn=*ACL)',  '(objectclass=*)'
    attributes = [demo['PROFILE']['ATTRIBUTE']] #  ['memberOf'], '*'
    
    main(name, query, attributes)
       
    

