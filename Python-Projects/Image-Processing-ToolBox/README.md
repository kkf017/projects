# Image Processing
Command line tool to perform image processing.

### Libraries
* Requires python>=3.5.
* Install numpy, scipy, matplotlib, pillow.

### Manual
* Install package:
```bash
pip3 install imgmagic
```

* Or use the tool with the command:
```python
python3 main.py /path/input-image.jpeg /path/output-image.jpeg [OPT] [ARGS]
```
 
```python
python3 main.py --help
```

## IMGMagic toolbox

```python
import numpy
import matplotlib.image as mpimg
from PIL import Image
import imgmagic

if __name__ == "__main__":
	
	filename = "img.jpeg"
	img1 = mpimg.imread(filename)
	img2 = numpy.copy(img1)

	img2 = imgmagic.display.greyscale(img1)
		
	im = Image.fromarray(img2)
	if len(img2.shape) == 2:
		im = im.convert('L')
	im.save("new.jpeg")
```

### Documentation

#### Display
This module contains functions to **display** an image.

###### Example 1
```python
img2 = imgmagic.display.greyscale(img1)
```

#### Geometric
This module contains functions to apply **geometric transforms** on an image.

###### Example 1
```python

img2 = imgmagic.geometric.crop(img1, (520,520), 75,75)
	
```

###### Example 2
```python
img2 = imgmagic.geometric.rotate(img1, 65)
	
```

###### Example 3
```python
img2 = imgmagic.geometric.flipping(img1)
```

###### Example 4
```python
img2 = imgmagic.geometric.reverse(img1)
```
###### Example 5
```python
img2 = imgmagic.geometric.scaling(img1, 0.25)
img2 = imgmagic.geometric.scaling(img1, 1.25)
```

#### Histogram
This module contains functions to perform **histogram enhancement** .

###### Example 1
```python
img2 = imgmagic.histogram.adjustContrast(img1)
```
###### Example 2
```python
imgmagic.histogram.equalization(img1)
```
###### Example 3
```python
imgmagic.histogram.negative(img1)
```


#### Filter
This module contains functions to perform **filtering**.

###### Example 1
```python
img2 = imgmagic.filter.GaussianNoise(img1, 125,0)
img2 = imgmagic.filter.SaltnPepperNoise(img1, 0.01)
```

###### Example 3
```python
filters =  {"lowpass", "highpass", "avg", "gauss"}
padding = {"reflect", "constant", "nearest", "mirror", "wrap"}

imgmagic.filter.filtering(img1, "lowpass", "reflect")
imgmagic.filter.filtering(img1, "avg", "wrap", 9)
```
###### Example 4
```python
filters =  {"laplacian", "sobel", "roberts"}
padding = {"reflect", "constant", "wrap"}

imgmagic.filter.sharpening(img1, "sobel", "wrap")
```
###### Example 5
```python
sub1 =  mpimg.imread("sub1.jpeg")
sub2 =  mpimg.imread("sub2.jpeg")

filters = {"laplacian", "sobel", "roberts"}

img2 = imgmagic.filter.crosscorrelation(sub1, "sobel", sub2)
```

#### Filter
This module contains functions to perform **FT filtering**.

###### Example 1
```python
img2 = imgmagic.fourier.ftfiltering(img1, "highpass", 145)
```
###### Example 2
```python
img2 = imgmagic.fourier.UnsharpMasking(img1, 145, 1)
```
###### Example 3
```python
img2 = imgmagic.fourier.HighFreqEmph(img1, 145, 1, 5)
```







