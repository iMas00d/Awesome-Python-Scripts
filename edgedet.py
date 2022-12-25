#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 19:58:54 2018

@author: masood
"""

from PIL import Image

from PIL import ImageFilter

 

# Open an already existing image

imageObject = Image.open("/path/to/image")

smoothenedImage = imageObject.filter(ImageFilter.SMOOTH)

moreSmoothenedImage = imageObject.filter(ImageFilter.SMOOTH_MORE)

 

# Display the original image and the smoothened Images

#imageObject.show()

#smoothenedImage.show()

moreSmoothenedImage.show()

# Apply edge enhancement filter

#edgeEnahnced = imageObject.filter(ImageFilter.EDGE_ENHANCE)

 

# Apply increased edge enhancement filter

#moreEdgeEnahnced = imageObject.filter(ImageFilter.EDGE_ENHANCE_MORE)

 

# Show original image - before applying edge enhancement filters

#imageObject.show() 

 

# Show image - after applying edge enhancement filter

#edgeEnahnced.show()

 

# Show image - after applying increased edge enhancement filter

#moreEdgeEnahnced.show()