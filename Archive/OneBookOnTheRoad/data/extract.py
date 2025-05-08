import os
import copy
from urllib.request import urlopen
import bs4

# pip install beautifulsoup4
# pip install regex

FOLDER = "/home/ksys/Documents/Project3/data/"
EXCEPT = []



def get_departments(url):
	url = "https://www.boites-a-livres.fr/departements"
	page = urlopen(url)
	html = page.read()
	html = html.decode("utf-8")
	
	# get list of departments
	soup = bs4.BeautifulSoup(html)
	for link in soup.findAll("a"):
		print(link.get("href"))
		

def get_municipality(filename):
	def link(url):
		page = urlopen(url)
		html = page.read()
		html = html.decode("utf-8")

		name = url.split("/")[-1][:-1]
		if not name in EXCEPT:
			os.mkdir(f"{FOLDER}{name}")
			print(f"\n\n\n{name}")
			soup = bs4.BeautifulSoup(html)
			with open(f"{FOLDER}{name}/{name}-link.txt", 'w') as f:
				i = 0
				for link in soup.findAll("a"):
					x = link.get("href")
					if not (i==0 or i == 1 or "https://www.boites-a-livres.fr/ajout/" in x or x in ["https://openstreetmap.org/copyright", "https://library.love/@boitesalivres", "https://www.facebook.com/profile.php?id=61551465693450"]):
						f.write(x+"\n")
					i+=1
			print("End.")
		
	with open(filename, 'r') as f:
		for line in f.readlines():
			link(line) # deparments-link.txt
	


def get_place(filename):
	def link(filename):
		def get_text_1(html):
			soup = bs4.BeautifulSoup(html) 
			for li in soup.findAll('ul'):
				if not li == None:
					for x in soup.findAll('li'):
						if "Adresse approximative" in x.text:
							return x.text.split(":")[1][1:]
			return None
		
		def finditall(msg):	
			def findit(sub):
				first = sub.find('.bindPopup("<small><a href=')
				last =  sub.find(">Voir la fiche détaillée</a></small>")
				if first == -1:
					return (None, None)
				#print(sub[first+len('.bindPopup("<small><a href=')+1: last][:-1])
				return (first+len('.bindPopup("<small><a href=')+1, last)
			
			res = []
			while 1:
				x, y = findit(msg)
				if x == None and y == None:
					break
				res.append(msg[x:y][:-1])
				msg = copy.copy(msg[y+len(">Voir la fiche détaillée</a></small>"):])
			return res
			
		with open(f"{FOLDER}{filename}/{filename}.txt", 'w') as writer:	
			with open(f"{FOLDER}{filename}/{filename}-link.txt", 'r') as f:
				for line in f.readlines():
					print(f"\n\n--->\033[34m{line}\033[00m")
					
					if not line in EXCEPT:
						page = urlopen(line)
						html = page.read()
						html = html.decode("utf-8")
					
						x = get_text_1(html)
						if not x == None:
							print(x)
							writer.write(x+"\n")
						else:
							soup = bs4.BeautifulSoup(html) 
							for li in soup.findAll('script', {"type": "text/javascript"}):
								res = finditall(li.text)
								for i in res:
									page = urlopen(i)
									html = page.read()
									html = html.decode("utf-8")
									x = get_text_1(html)
									print(x)
									writer.write(x+"\n")
				
				
	with open(filename, 'r') as f:
		for line in f.readlines():
			print(f"\033[35m\n\n\n************************************************************\033[00m")
			print(f"\033[35m {FOLDER}{line[:-1]}/{line[:-1]}-link.txt\033[00m")
			print(f"\033[35m************************************************************\033[00m")
			link(line[:-1]) #f"{FOLDER}{line[:-1]}/{line[:-1]}-link.txt")
			#input()


def special_case_1(): # dordogne
	def finditall(msg):	
		def findit(sub):
			first = sub.find('<li><a href=')
			last =  sub.find(">")
			if first == -1:
				return (None, None)
				#print(sub[first+len('.bindPopup("<small><a href=')+1: last][:-1])
			return (first+len('<li><a href=')+1, last)
			
		res = []
		while 1:
			x, y = findit(msg)
			if x == None and y == None:
				break
			res.append(msg[x:y][:-1])
			print()
			msg = copy.copy(msg[y+len(">"):])
		return res

	url = "https://www.boites-a-livres.fr/departement/dordogne"
	page = urlopen(url)
	html = page.read()
	html = html.decode("utf-8")
	#print(html)
	
	soup = bs4.BeautifulSoup(html)
	i = 0
	for u in soup.findAll("li"):#, {"class": "list"}):
		print(f"\n\n{u[14:]}")
			
	#for link in soup.findAll("a"):
		#x = link.get("href")
		#if not (i==0 or i == 1 or "https://www.boites-a-livres.fr/ajout/" in x or x in ["https://openstreetmap.org/copyright", "https://library.love/@boitesalivres", "https://www.facebook.com/profile.php?id=61551465693450"]):
		#print(f"\n{x}")
			#i+=1
			
			
			
def get_place(filename):
	def link(filename):
		def get_text_1(html):
			soup = bs4.BeautifulSoup(html) 
			for li in soup.findAll('ul'):
				if not li == None:
					for x in soup.findAll('li'):
						if "Adresse approximative" in x.text:
							return x.text.split(":")[1][1:]
			return None
		
		def finditall(msg):	
			def findit(sub):
				first = sub.find('.bindPopup("<small><a href=')
				last =  sub.find(">Voir la fiche détaillée</a></small>")
				if first == -1:
					return (None, None)
				#print(sub[first+len('.bindPopup("<small><a href=')+1: last][:-1])
				return (first+len('.bindPopup("<small><a href=')+1, last)
			
			res = []
			while 1:
				x, y = findit(msg)
				if x == None and y == None:
					break
				res.append(msg[x:y][:-1])
				msg = copy.copy(msg[y+len(">Voir la fiche détaillée</a></small>"):])
			return res
			
		with open(f"{FOLDER}{filename}/{filename}.txt", 'w') as writer:	
			with open(f"{FOLDER}{filename}/{filename}-link.txt", 'r') as f:
				for line in f.readlines():
					print(f"\n\n--->\033[34m{line}\033[00m")
					
					if not line in EXCEPT:
						page = urlopen(line)
						html = page.read()
						html = html.decode("utf-8")
					
						x = get_text_1(html)
						if not x == None:
							print(x)
							writer.write(x+"\n")
						else:
							soup = bs4.BeautifulSoup(html) 
							for li in soup.findAll('script', {"type": "text/javascript"}):
								res = finditall(li.text)
								for i in res:
									page = urlopen(i)
									html = page.read()
									html = html.decode("utf-8")
									x = get_text_1(html)
									print(x)
									writer.write(x+"\n")
									
	link("dordogne")
				
				
	
	

if __name__ == "__main__":

	#get_municipality("deparments.txt")
	#get_place("deparments.txt")
	get_place("dordogne")
