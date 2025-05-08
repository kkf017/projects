import random

from typing import List, Dict, Callable

from data import create_file, write_file

import pydot




G = pydot.Dot(graph_type='digraph')


def hamming(x:List[int], y:List[int])->int:
	"""
		Function to compute Hamming distance.
		input:
			x - vector (binary)
			y - vector (binary)
		output:
			Hamming distance between x and y.
	"""
	return sum([(i+j)%2 for i,j in zip(x,y)])
	

def xor(x:List[int], y:List[int])->int:
	"""
		Function to compute xor distance.
		input:
			x - vector (binary)
			y - vector (binary)
		output:
			xor distance between x and y.
	"""
	return sum([(i+j)%2 for i,j in zip(x,y)])


def distance_matrix(func:Callable[[List[int], List[int]], int], x:List[List[int]])->List[List[float]]:
	"""
		Function to compute distance matrix.
		input:
			x - data (set of binary vectors)
		output:
			Distance matrix between vectors of data set.	
	"""
	n:int =len(x)
	return [[func(x[i], x[j]) for j in range(n) ] for i in range(n)]
	
		
	
def single_linkage(func:Callable[[List[int], List[int]], int], x:List[int], y:List[int], X:List[List[int]])->int:
	"""
		Function to compute single linkage between two clusters.
		input:
			x - cluster 1 (index)
			y - cluster 2 (index)
			X - vectors (data)
		output:
			single linkage between two clusters
			
	"""
	#Distance (C1, C2) = Min { d(i, j), where item i is within C1, and item j is within C2}
	z = []
	for i in x:
		for j in y:
			#print("{}, {} : d({},{}) = {}".format(i,j, X[i], X[j], hamming(X[i], X[j])))
			z.append(func(X[i], X[j]))
	return min(z)
	


def complete_linkage(func:Callable[[List[int], List[int]], int], x:List[int], y:List[int], X:List[List[int]])->int:
	"""
		Function to compute complete linkage between two clusters.
		input:
			x - cluster 1 (index)
			y - cluster 2 (index)
			X - vectors (data)
		output:
			complete linkage between two clusters
	"""
	#Distance (C1, C2) = Max { d(i, j), where item i is within C1, and item j is within C2}
	z = []
	for i in x:
		for j in y:
			#print("{}, {} : d({},{}) = {}".format(i,j, X[i], X[j], hamming(X[i], X[j])))
			z.append(func(X[i], X[j]))
	return max(z)

def average_linkage(func:Callable[[List[int], List[int]], int], x:List[int], y:List[int], X:List[List[int]])->float:
	"""
		Function to compute average linkage between two clusters.
		input:
			x - cluster 1 (index)
			y - cluster 2 (index)
			X - vectors (data)
		output:
			average linkage between two clusters	
	"""
	#Distance (C1, C2) = Sum{ d(i, j) } / Total Number of distances
	z = []
	for i in x:
		for j in y:
			#print("{}, {} : d({},{}) = {}".format(i,j, X[i], X[j], hamming(X[i], X[j])))
			z.append(func(X[i], X[j]))
	return sum(z)/len(z)
	


def centroid_linkage(func:Callable[[List[int], List[int]], int], x:List[int], y:List[int], X:List[List[int]])->int:
	"""
		Function to compute centroid linkage between two clusters.
		input:
			x - cluster 1 (index)
			y - cluster 2 (index)
			X - vectors (data)
		output:
			centroid linkage between two clusters	
	"""
	# Centroid: Distance between the cluster is determined based on the distance between the centroid of the two clusters
	vx = [X[i] for i in x]
	vy = [X[i] for i in y]
	
	x_centroid = [round(sum(i)/len(i)) for i in zip(*vx)]  #check round()
	y_centroid = [round(sum(i)/len(i))  for i in zip(*vy)]
	
	return func(x_centroid, y_centroid )


def linkage(func:Callable[[List[int], List[int]], int], y:List[List[int]], X:List[List[int]])->List[List[int]]:
	"""
		Function to compute linkage between clusters.
		input:
			y - clusters (index)
			X - vectors (data)
		output:
			linkage matrix between clusters	
	"""
	# clusters = [[1,3],[2],[4,5]]
	n = len(y)
	x = []
	for i in range(n):
		z = []
		for j in range(n):
			if i == j:
				res = None
			else:
				res = average_linkage(func,y[i], y[j], X)
				#res = single_linkage(func,y[i], y[j], X)
				#res = complete_linkage(func,y[i], y[j], X)
				#res = centroid_linkage(func,y[i], y[j], X)	
			z.append(res)
		x.append(z)
	return x
	
	
def merge_clusters(filename:str, y:List[List[int]], x:List[List[int]], n:int)->List[List[int]]:
	"""
		Function to merge clusters.
		input:
			y - clusters (index)
			X - linkage matrix
		output:
			updated clusters (list of index)	
	"""
	#y = [[1,3],[2],[4,5]] # clusters (indexes)
	#x=[[None, 3.5, 3.5], [3.5, None, 3.0], [3.5, 3.0, None]] # linkage matrix
	
	#Repeat: Merge the two closest clusters and update the proximity matrix

	x_min = [min(x for x in nums if x is not None) for nums in x]
	x_min_abs = min(x_min)
	index_min = [i for i, j in enumerate(x_min) if j == x_min_abs]

	#print("\nx_min: {} x_min_abs: {} index_min: {}".format(x_min, x_min_abs, index_min))
	
	x_min = index_min[0]
	indices = [list(set([x_min, i])) for i, j in enumerate(x[x_min]) if j == x_min_abs]
	
	#print("\nx_min: {} indices: {}".format(x_min,indices))
	
	#print("\ny before: {}".format(y))
	
	merge = indices[0]
	
	name_parent =  "-".join([str(i) for i in y[merge[0]]+y[merge[1]]])
	name_children_1 = "-".join([str(i) for i in y[merge[0]]])
	name_children_2 = "-".join([str(i) for i in y[merge[1]]])
	
	prob = "{:.2f}".format(1-x_min_abs/n) # similarite = 1-dist
	
	G.add_node(pydot.Node(name=name_parent, label=prob))
	G.add_edge(pydot.Edge(name_parent, name_children_1))
	G.add_edge(pydot.Edge(name_parent, name_children_2))
   
   
	print("clustering: {} {} dist: {}/{} prob: {}".format(y[merge[0]], y[merge[1]],x_min_abs,n, prob))
	
	y[merge[0]] = y[merge[0]]+y[merge[1]]
	y.pop(merge[1])

	
	#print("\ny after: {}".format(y))
	# merge the two closest cluster
    
    
	write_file("{}csv_graph.csv".format(filename), [name_parent, name_children_1, prob])
	write_file("{}csv_graph.csv".format(filename), [name_parent, name_children_2, prob])

	return y
	

def clustering(filename:str, matrix: List[List[int]], x: Dict[int, List[str]], y: Dict[int, List[str]])->None:

	create_file("{}csv_graph.csv".format(filename), ['Node Parent', 'Node child', 'Probability'])

	n: int = len(matrix[0])
	m: int = len(matrix)
	
	# compute distance matrix
	dist = distance_matrix(hamming, matrix)		

	clusters = [[i] for i in range(m)]
	print("\nclusters: {}".format(clusters))
	
	
	for cluster in clusters:
		name = "-".join([str(i) for i in cluster])
		label = "{}\nsize: {}\nrights: {}".format(name,len(x[cluster[0]]), len(y[cluster[0]]))
		#label = "{}".format(name)
		G.add_node(pydot.Node(name=name, label=label))

	
	
	
	while 1 < len(clusters) :
		print("\n\n\n ***** NEW STEP ******")
		
		x = linkage(hamming, clusters, matrix)
		
		print("\nMatrix:")
		for a in matrix:
			print(a)
		
		print("\nLinkage:".format(x))
		for a in x:
			print(a)
		
		clusters = merge_clusters(filename, clusters, x,n)
		
	
		print("\n\nNew clusters: {}".format(clusters))
		
		#input()
	
	"""	
	for node in G.get_nodes():
		print("Node {}".format(node.get_name()))

	for node in G.get_edges():
		print("Edge {} {}".format(node.get_source(), node.get_destination()))
	
	"""
	G.write_png("{}clustering.png".format(filename))
	
	return None
		
"""
if __name__ == "__main__" :

	n:int = 6
	m:int = 16			   
	matrix: List[List[int]] = [[random.randint(0,1) for _ in range(n)] for _ in range(m)]
	
	clustering(matrix)
	
"""
		
	# utiliser un pointeur - reference de fonction pour passer la fonction hamming (distance)
	# en parametre de finction pour les fonctions de linkage
	# distance_matrix(), single_linkage(), complete_linkage(), average_linkage(), centroid_linkage
	
	#merge_clusters(hamming, clusters, x)
	
	# ev. linkage()

	
	# Agglomerative clustering - n clusters
	
	#for _ in range(1):
	
		# compute distance matrix - single/complete/average linkage
		
		# merge closest clusters - Merge the two closest clusters
		
		# update distance matrix
		
		# repeat until you get only one cluster
		

