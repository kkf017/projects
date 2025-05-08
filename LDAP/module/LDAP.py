import sys
from ldap3 import Server, Connection, ALL, Tls, SUBTREE
import ssl, json

from typing import List, Tuple, Dict, Union


sys.path.insert(1, './utils')
from data import create_file, write_file, read_json
from decorators import print_out



def get_config(filename: str) -> Tuple[Union[str, int]]:
    """
        function to read config file
        input: 
            filename - name of the file to read
        output: 
            parameters: server, port, username, password
   """
    config = read_json(filename)
    return config['LDAP']['HOST'], config['LDAP']['PORT'], config['LDAP']['USERNAME'], config['LDAP']['PASSWORD'], config['LDAP']['ROOT_SERVER'], config['LDAP']['SSL']





def ldap_write_user(filename:str, objs:List[Dict[str, str]], header:List[str], attributes:str)->List[List[str]]:
    """
        function to write data in a .csv file
        input: 
            filename - name of the file to write
            objs: result of the ldap query
            header: header .csv
            attributes: attribute of the query to read
        output: 
            written file (data) as a List
    """
    x = []
    create_file(filename, header)
    for obj in objs:
        for attribut in obj['attributes'][attributes]: # A MODIFIER : case of several attributs to print
            x.append([obj['dn'], attribut])
            write_file(filename, [obj['dn'], attribut])
        
        if not obj['attributes'][attributes]:
            x.append([obj['dn'], 'Na'])
            write_file(filename, [obj['dn'], 'Na'])
    return x




def ldap_query( query:str, attribute:List[str]):  
    """
        function to execute LDAP query
        input: 
            domain -  
            query -
            attribute -  ex. 'memberOf'
        output: 
            result of the query
    """    
    ldap_server, ldap_port, ldap_user, ldap_password, ldap_root_server, ldap_ssl = get_config('./config.json')
    
    server = Server(ldap_server, port=ldap_port, get_info=ALL)
    
    if ldap_ssl:
        tls_configuration = Tls(validate=ssl.CERT_REQUIRED, version=ssl.PROTOCOL_TLSv1)
        server = Server(ldap_server, port=ldap_port,  use_ssl=True, tls=tls_configuration, get_info=ALL) 
    
    conn = Connection(ldap_server, user=ldap_user, password=ldap_password)
    
    if not conn.bind():
        raise Exception("[-] Error: Connection failed.")
    
    #if ldap_ssl:
        #conn.start_tls()
    
    #conn.search(domain, query, search_scope=SUBTREE, attributes=attribute)  
    conn.search(ldap_root_server, query, search_scope=SUBTREE, attributes=attribute) 
    objs = [json.loads(a.entry_to_json()) for a in conn.entries]
    

    """
    for a in conn.entries:
        print('\n\n')
        print(a.entry_to_json())
    
    """
    return objs



def ldap(filename:str, query:str, attributes:List[str]) -> List[List[str]]:
    """
        function to execute ldap query and write result in .csv file
        input: 
            filename - name of the file to read
            domain -
            query -
            attributes -
        output: 
            None
    """
    objs = ldap_query(query, attributes)
    if objs==[]:
        return []
    filename = '{}csv_RAW_1.csv'.format(filename)
    
    x = ldap_write_user(filename, objs, ['User']+attributes, attributes[0]) # A MODIFIER : case of several attributs to print for a user
    
    return x



     
    

    
    
        
