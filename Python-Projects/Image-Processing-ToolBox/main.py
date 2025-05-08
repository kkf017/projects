import sys
import os
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image

from IMGMagic.display import *
from IMGMagic.geometric import *
from IMGMagic.histogram import *
from IMGMagic.filter import *
from IMGMagic.fourier import *


from typing import List, Union



def main(argv:List[str], argc:int)->int:

	def check(argv:List[str])->Tuple[Union[str, List[str]]]:
		def exists(filename:str)->bool:
			filename =  os.path.abspath(filename)
			if not os.path.exists(filename):
				return False
			return True
			
		WARNINGPARSING = "\n\033[{}mWarning: Unvalid command.\n\n\033[{}mUse --help to list all available options.".format("0;33", "1;30")
		
		filename1 = None
		filename2 = None
		opt = None
		args = []
		
		
		if len(argv) < 3:
			sys.exit("\n\033[{}mWARNING: Syntax error.\n\n\033[{}mUse --help to list all available options.".format("0;31", "1;30"))
				
		if not exists(argv[1]):
			sys.exit("\n\033[{}mWARNING: {} does not exist.\n\n\033[{}mUse --help to list all available options.".format("0;31", argv[1], "1;30"))
		
		
		filename1 = argv[1]
		filename2 = argv[2]

		if len(argv) > 3:
			opt = argv[3]
			if len(argv) > 4:
				args = argv[4:]
				     
		return filename1, filename2, opt, args    

	if argc==1:
		return 0
	
	if argc==2 and argv[-1]:
		_help_()
		return 1
       
	filename1, filename2, opt, args = check(argv)
	
	img1 = mpimg.imread(filename1)
	img2 = numpy.copy(img1)
	
	if opt:
		match opt:
			case "-g":
				img2 = greyscale(img1)
			case "-rgb":
				img2 = numpy.zeros(img1.shape)
				R, G, B = img1[:, :, 0], img1[:, :, 1], img1[:, :, 2]
				img2[:,:,0] = R
				img2 = numpy.clip(img2, 0, 255).astype(numpy.uint8)
			case "-n":
				match args[0]:
					case "gauss":
						img2 = GaussianNoise(img1,float(args[1]),float(args[2]))
					case "snp":
						img2 = SaltnPepperNoise(img1, float(args[1]))
			case "-u":
				img2 = downsampling(img1, int(args[0]))
			case "-c":
				img2 = crop(img1, (int(args[0]),int(args[1])), int(args[2]), int(args[3]))
			case "-r":
				img2 = rotate(img1, float(args[0]))
			case "-f":
				img2 = flipping(img1)
			case "-m":
				img2 = reverse(img1)
			case "-z":
				img2 = scaling(img1, float(args[0]))
			case "-filt":
				n = None
				if len(args) > 2:
					n = float(args[2])
				img2 = filtering(img1, args[0], args[1], n)
			case "-sh":
				c = 1
				#img1 = greyscale(img1)
				img2 = sharpening(img1, args[0], args[1])
				#img2 = img1 + c*img2
			case "-corr":
				sub = mpimg.imread(args[1])
				img2 = crosscorrelation(img1, args[0], sub) 
			case "-h":
				histogram(img1, False)
			case "-adj":
				img2 = adjustContrast(img1) 
			case "-eq":
				img2 = equalization(img1)
			case "-gamma":
				img1 = greyscale(img1)
				img2 = correctionGamma(img1, 1, 1/2)
			case "-neg":
				#img1 = greyscale(img1)
				img2 = negative(img1) 
			case "-th":
				img2 = hardthresholding(img1, float(args[0]))
			case "-ftfilt":
				if args[0] in ["lowpass", "glowpass", "highpass", "ghighpass"]:
					img2 = ftfiltering(img1, args[0], float(args[1]))
				if args[0] in ["blowpass","bhighpass"]:
					img2 = ftfiltering(img1, args[0], float(args[1]), float(args[2]))
				if args[0] in ["bandreject", "bandpass"]:
					if args[1] in ["butterworth"]:
						img2 = ftfiltering(img1, args[0], args[1], float(args[2]), float(args[3]), float(args[4]))
					else:
						img2 = ftfiltering(img1, args[0], args[1], float(args[2]), float(args[3]))
				if args[0] in ["homomorphic"]:
						img2 = ftfiltering(img1, args[0], float(args[1]), float(args[2]), float(args[3]), float(args[4]))
			case "-umask":
				#img1 = greyscale(img1)
				img2 = UnsharpMasking(img1, float(args[0]), float(args[1]))
			case "-hfe":
				#img1 = greyscale(img1)
				img2 = HighFreqEmph(img1, float(args[0]), float(args[1]), float(args[2]))
			case "-fsh":
				img1 = greyscale(img1)
				img2 = LaplacianFilter(img1,-1)#float(args[0]))
				

	"""
	plt.axis('off')
	match len(img2.shape):
		case 2:
			plt.imshow(img2,  cmap='gray')
		case 3:
			plt.imshow(img2)
		case _:
			raise Exception("\n\033[{}m[-]Warning: Unknown size of image.".format("0;33")) 
	
	plt.savefig(filename2)
	"""
	
	im = Image.fromarray(img2)
	if len(img2.shape) == 2:
		im = im.convert('L')
	im.save(filename2)
	
	return 1



def _help_()->None:
    print("\n\033[{}mCommand:- imgmagic img1 img2 [OPTION] [ARGS]".format("0;34"))
    print("\033[{}m\t with img1 img2 path of input/output image.".format("0;34"))
    print("\n\033[{}m-g \tConvert RGB image to greyscale.".format("0;37"))
    print("\n\033[{}m-n [noise] [args] \tAdd noise to image. \n\twith \t[noise]: type of noise (gauss, snp).\n\t\t[args]: arguments. \n\t\t\t\tmean, sigma for gaussian noise \n\t\t\t\tprob for salt and pepper noise".format("0;37"))
    print("\n\033[{}m-u [fact] \tPerform downsampling on image. \n\twith \t[fact]: factor of downsampling.".format("0;37"))
    print("\n\033[{}m-c [x0] [y0] [width] [height]  \tCrop the image. \n\twith \t[x0],[y0]: Coordiante of starting point.\n\t\t[width],[height]: width and height of cropped image.".format("0;37"))
    print("\n\033[{}m-r [deg] \tRotate the image. \n\twith \t[deg]: angle of rotation.".format("0;37"))
    print("\n\033[{}m-z [scale] \tScale the image. \n\twith \t[scale]: factor of scaling.".format("0;37"))
    print("\n\033[{}m-m \tReverse the image.".format("0;37"))
    print("\n\033[{}m-f \tFlip the image.".format("0;37"))
    print("\n\033[{}m-filt [filter] [padding] [args] \tPerform filtering on image. \n\twith \t[filter]: type of filter (lowpass, highpass, avg, gauss).\n\t\t[padding]: type of padding (reflect, constant, nearest, mirror, wrap). \n\t\t[args]: arguments for each type of filter.".format("0;37"))
    print("\n\033[{}m-sh [filter] [padding]\tPerform sharpening on image. \n\twith \t[filter]: type of filter (laplacian, sobel, roberts).\n\t\t[padding]: type of padding (reflect, constant, wrap).".format("0;37"))
    print("\n\033[{}m-corr [filter] [sub] \tPerform cross correlation. \n\twith \t[filter]: type of filter (laplacian, sobel, roberts). \n\t\t[sub]: subimage to find in the main image.".format("0;37"))
    print("\n\033[{}m-h \tCompute histogram of the image.".format("0;37"))
    print("\n\033[{}m-adj \tPerform contrast adjustment of the image.".format("0;37"))
    print("\n\033[{}m-eq \tPerform image equalization.".format("0;37"))
    print("\n\033[{}m-neg \tCompute negative of the image.".format("0;37"))
    print("\n\033[{}m-gamma [c] [gamma] \tPerform gamma correction. \n\twith \t[c], [gamma]: parameters of gamma correction.".format("0;37"))
    print("\n\033[{}m-th \tPerform thresholding with Fourier transform.".format("0;37"))
    print("\n\033[{}m-ftfilt [filter] [args] \tPerform FT filtering on image. \n\twith \t[filter]: type of filter (lowpass, blowpass, glowpass, highpass, bhighpass, ghighpass, bandreject, bandpass, homomorphic). \n\t\t[args]: arguments for each type of filter.".format("0;37"))
    print("\n\033[{}m-umask [cutoff] [k] \tPerform unsharp masking. \n\twith \t[cutoff],[k]: parameters.".format("0;37"))
    print("\n\033[{}m-hfe [cutoff] [k1] [k2] \tPerform high frequency emphasis. \n\twith \t[cutoff],[k1],[k2]: constant.".format("0;37"))
    print("\n\033[{}m-fsh [c] \tCompute FT laplacian. \n\twith \t[c]: constant.".format("0;37"))


 
if __name__ == "__main__":
	print("\033[{}mIMGMagic 1.0.".format("1;35"))
	
	main(sys.argv, len(sys.argv))
	
	print("\n\033[{}mUse --help to list all available options.".format("1;30"))






