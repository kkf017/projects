import csv

from typing import List, Dict, Union

from data import read_file, create_file, write_file, read_file_windows
from clustering import clustering


def get_users(data:List[List[str]])->List[str]:
	"""
		Function to get (single) users - from data -.
		input:
			data - extracted data 
		output:
			list of users.
	"""
	y = []
	for x in data:
		if not x[0] in y:
			y.append(x[0])
	return y
	
def get_rights(data:List[List[str]])->List[str]:
	"""
		Function to get (single) rights - from data -.
		input:
			data - extracted data 
		output:
			list of rights.
	"""
	y = []
	for x in data:
		if not x[1] in y:
			y.append(x[1])
	return sorted(y)
	

def get_rights_by_user(data:List[List[str]])->Dict[str, List[str]]:
	"""
		Function to get rights for each user - from data -.
		input:
			data - extracted data 
		output:
			list of rights by user.
	"""
	user = data[0][0]
	rights_by_user = {}
	rights = []
	for x in data:
		if x[0] != user:
			rights_by_user[user] = rights
			user = x[0]
			rights = []
		rights.append(x[1])
	rights_by_user[user] = rights
	return rights_by_user


def get_groups(x:Dict[str, List[str]])->Union[Dict[int, List[str]]]:
	"""
		Function to group (similar) users into groups.
		input:
			data - extracted data 
		output:
			dict of groups.
			dict of rights by groups.
	"""
	users = list(x.keys())
	groups = []
	for user1 in users:
		new = [user1]
		for user2 in users:
			if user1 != user2 and set(x[user1]) == set(x[user2]):
				new.append(user2)
		
		if not set(new) in groups:
			groups.append(set(new))
	
	groups_user = {}
	groups_rights = {}
	for i in range(len(groups)):
		groups_user[i] = groups[i]
		groups_rights[i] = x[list(groups[i])[0]]
		
	return groups_user, groups_rights 
	
	
def binary_matrix(y:Dict[int, List[str]], x:Dict[int, List[str]])->List[List[int]]:
	"""
		Function to get binary matrix (of data).
		input:
			data - extracted data 
		output:
			binary matrix.
	"""
	matrix = []	
	for i in list(y.keys()):
		new = []
		for j in x:
			if j in y[i]:
				new.append(1)
			else:
				new.append(0)
		matrix.append(new)
	return matrix

def method(filename:str, data:List[List[str]])->None:
#if __name__ == "__main__" :
	
	#data: List[List[str]] = read_file_windows("{}csv_RAW_2.csv".format(filename))
	
	users:List[str] = get_users(data)
	
	rights:List[str] = get_rights(data)
	
	rights_by_user:Dict[str, List[str]] = get_rights_by_user(data)

	# build groups
	gp_users, gp_rights = get_groups(rights_by_user)
	
	# print groups in a .csv file

	filenameSummary = '{}csv_summary.csv'.format(filename)
	create_file(filenameSummary, ['Group', 'Size', 'Users','Numbre of rights', 'Rights'])
	for i in list(gp_users.keys()):
		write_file(filenameSummary, [str(i), len(gp_users[i]), " ".join(list(gp_users[i])), len(gp_rights[i]), " ".join(list(gp_rights[i]))])

    
	filenameGroups = '{}csv_groups.csv'.format(filename)
	create_file(filenameGroups, ['Group', 'Size','Numbre of rights'])
    
	filenameUsers = '{}csv_users.csv'.format(filename)
	create_file(filenameUsers, ['Group','User'])
    
	filenameRights = '{}csv_rights.csv'.format(filename)
	create_file(filenameRights, ['Group', 'Rights'])
    
	for i in list(gp_users.keys()):
		write_file(filenameGroups, [str(i), len(gp_users[i]), len(gp_rights[i])])
        
		for user in gp_users[i]:
			write_file(filenameUsers, [str(i), user])
        
		for right in gp_rights[i]:
			write_file(filenameRights, [str(i), right])
        
    
    
	# build binary matrix
	binary = binary_matrix(gp_rights, rights)
	
	"""
	for a in binary:
		print(a)
	
	for a in list(gp_users.keys()):
		print("\n",a, gp_users[a])	
	"""	
	#Agglomerative clustering
	clustering(filename, binary, gp_users, gp_rights)
	
	return None


	
