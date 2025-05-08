import os

from typing import Dict

from services.IMGToolbox import main


def FruitJuiceMagic(img1:str, img2:str, opts:Dict[str,str])->None:
	match opts["FruitJuiceImg"]:
		case "nachi":
			argv = ["main.py", img1, img2, "-g"]
		case "blueberry":
			argv = ["main.py", img1, img2, "-n", "gauss", float(opts['blueberry1']), float(opts['blueberry2'])]
		case "lemon":
			argv = ["main.py", img1, img2, "-n", "snp", float(opts["lemon"])]
		case "apple":
			argv = ["main.py", img1, img2, "-rgb", "r"]
		case _:
			argv = ["main.py"]
	argc = len(argv)
	main(argv, argc)
	return None


def StrawberryMagic(img1:str, img2:str, opts:Dict[str,str])->None:
	match opts["StrawberryImg"]:
		case "cupcake":
			argv = ["main.py", img1, img2, "-sh", "laplacian", "reflect"]
		case "cerealscrisps":
			argv = ["main.py", img1, img2, "-sh", "sobel", "reflect"]
		case "morning":
			argv = ["main.py", img1, img2, "-sh", "roberts", "reflect"]
		case "cupoftea":
			argv = ["main.py", img1, img2, "-corr", "sobel", opts["cupoftea"]] # "laplacian/sobel/roberts"
		case _:
			argv = ["main.py"]
	argc = len(argv)
	main(argv, argc)
	return None


def CherryMagic(img1:str, img2:str, opts:Dict[str,str])->None:
	match opts["CherryImg"]:
		case "cherry1":
			argv = ["main.py", img1, img2, "-c", float(opts["cherry1x"]), float(opts["cherry1y"]), float(opts["cherry1width"]), float(opts["cherry1height"])]
		case "cherry2":
			argv = ["main.py", img1, img2, "-r", float(opts["cherry2angl"])]
		case "cherry3":
			argv = ["main.py", img1, img2, "-z", float(opts["cherry3z"])]
		case "cherry4":
			argv = ["main.py", img1, img2, "-m"]
		case "cherry5":
			argv = ["main.py", img1, img2, "-f"]
		case _:
			argv = ["main.py"]		
	argc = len(argv)
	main(argv, argc)
	return None

def MuffinMagic(img1:str, img2:str, opts:Dict[str,str])->None:
	match opts["MuffinImg"]:
		case "raspberry":
			argv = ["main.py", img1, img2, "-filt", "lowpass", "wrap"]
		case "mugcake":
			argv = ["main.py", img1, img2, "-filt", "highpass", "wrap"]
		case "yogurt":
			argv = ["main.py", img1, img2, "-filt", "avg", "wrap", opts["yogurt"]]
		case "vanilla":
			argv = ["main.py", img1, img2, "-filt", "gauss", "wrap" ]
		case _:
			argv = ["main.py"]		
	argc = len(argv)
	main(argv, argc)
	return None
	

def AvocadoMagic(img1:str, img2:str, opts:Dict[str,str])->None:
	match opts["AvocadoImg"]:
		case "avocado1":
			argv = ["main.py", img1, img2, "-adj"]
		case "avocado2":
			argv = ["main.py", img1, img2, "-gamma", opts["avocado21"], opts["avocado22"]]
		case "avocado3":
			argv = ["main.py", img1, img2, "-eq"]
		case "avocado4":
			argv = ["main.py", img1, img2, "-neg"]
		case _:
			argv = ["main.py"]		
	argc = len(argv)
	main(argv, argc)
	return None

def CookieMagic(img1:str, img2:str, opts:Dict[str,str])->None:
	match opts["CookieImg"]:
		case "donut":
			argv = ["main.py", img1, img2, "-ftfilt", "lowpass", float(opts["donut"])]
		case "crunchy":
			argv = ["main.py", img1, img2, "-ftfilt", "blowpass", float(opts["crunchy1"]), float(opts["crunchy2"])]
		case "choconuts":
			argv = ["main.py", img1, img2, "-ftfilt", "glowpass", float(opts["choconuts"])]
		case "candypop":
			argv = ["main.py", img1, img2, "-ftfilt", "highpass", float(opts["candypop"])]
		case "cheesecake":
			argv = ["main.py", img1, img2, "-ftfilt", "bhighpass", float(opts["cheesecake1"]), float(opts["cheesecake2"])]
		case "sugar":
			argv = ["main.py", img1, img2, "-ftfilt", "ghighpass", float(opts["sugar"])]
		case "rainbow":
			argv = ["main.py", img1, img2, "-ftfilt", "bandreject", opts["rainbow3"], float(opts["rainbow1"]),  float(opts["rainbow2"]), float(opts["rainbow4"])]	
		case "icecream":
			argv = ["main.py", img1, img2, "-ftfilt", "bandpass",  opts["icecream3"], float(opts["icecream1"]),  float(opts["icecream2"]), float(opts["icecream4"])]
		case "cone":
			argv = ["main.py", img1, img2, "-ftfilt", "homomorphic", float(opts["cone1"]),  float(opts["cone2"]), float(opts["cone3"]), float(opts["cone4"])]	
		case _:
			argv = ["main.py"]		
	argc = len(argv)
	main(argv, argc)
	return None
	

def CoffeeMagic(img1:str, img2:str, opts:Dict[str,str])->None:
	match opts["CoffeeImg"]:
		case "coffee1":
			argv = ["main.py", img1, img2, "-fsh", -1]
		case "coffee2":
			argv = ["main.py", img1, img2, "-umask", float(opts["coffee21"]), float(opts["coffee22"])]
		case "coffee3":
			argv = ["main.py", img1, img2, "-hfe", float(opts["coffee31"]), 1, float(opts["coffee32"])] #, float(opts["coffee33"])]
		case _:
			argv = ["main.py"]		
	argc = len(argv)
	main(argv, argc)
	return None
	

def imgProcessing(img1:str, img2:str, opts:Dict[str,str])->None:
	if "FruitJuiceImg" in opts.keys():
		FruitJuiceMagic(img1, img2, opts)
	if "StrawberryImg" in opts.keys():
		StrawberryMagic(img1, img2, opts)
	if "CherryImg" in opts.keys():
		CherryMagic(img1, img2, opts)
	if "MuffinImg" in opts.keys():
		MuffinMagic(img1, img2, opts)
	if "AvocadoImg" in opts.keys():
		AvocadoMagic(img1, img2, opts)
	if "CookieImg" in opts.keys():
		CookieMagic(img1, img2, opts)
	if "CoffeeImg" in opts.keys():
		CoffeeMagic(img1, img2, opts)
	return None
