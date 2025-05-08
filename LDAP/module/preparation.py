import hashlib

from data import read_file, create_file, write_file, read_file_windows

from typing import List


def filter_Na(x:List[List[str]])->List[List[str]]:
	"""
		function to remove Na elements.
		input: 
		    x - data
		output: 
		    filtered data (without Na)
	"""
	return [y for y in x if y[1] != 'Na']


def get_users(x:List[List[str]])->List[str]:
	"""
		function to get users (from data).
		input: 
		    x - data
		output: 
		    list of (single) users
    """
	users = []
	for y in x:
		if not y[0] in users:
			users.append(y[0])
	return users
	
	
def get_rights(x:List[List[str]])->List[str]:
	"""
		function to get users (from data).
		input: 
		    x - data
		output: 
		    list of (single) rights
	"""
	rights = []
	for y in x:
		if not y[1] in rights:
			rights.append(y[1])
	return sorted(rights)
	

def prepare_data(filename: str, data:List[List[str]]) -> List[List[str]]:
	"""
		function data from .csv file
		input: 
		    filename - name of the file to read
		output: 
		    prepared data
	"""
	#data = read_file_windows(filename) 
	
	# filter Na
	X = filter_Na(data)
	
	users = get_users(X)
	rights = get_rights(X)
	
	# add label for rights
	X = [x+[rights.index(x[1])] for x in X]
	
	# add hashes for rights
	X = [x+[hashlib.sha1(x[1].encode("UTF8")).hexdigest()] for x in X]
	
	return X


def prepare(filename: str, data:List[List[str]]) -> List[List[str]]:
    """
        function to write data in a .csv file
        input: 
            filename - name of the file to read
        output: 
            None
    """        
    filename1 = '{}csv_RAW_1.csv'.format(filename)
    filename2 = '{}csv_RAW_2.csv'.format(filename)
    x = prepare_data(filename1,data)
    
    create_file(filename2, ['User', 'Group', 'Label', 'Hash'])
    for y in x:
    	write_file(filename2, y)
    
    return x
		
 
    
