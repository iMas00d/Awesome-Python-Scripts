#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:14:34 2017

@author: masood
"""
from PIL import Image
import os
from PIL import ImageFilter

path = "D:/VPU dataset/train_UT/ann/output/"
dirs = os.listdir( path )
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((320,240), Image.ANTIALIAS)
            #imResize = im.filter(ImageFilter.SMOOTH_MORE)
            #imResize = im.filter(ImageFilter.EDGE_ENHANCE_MORE) 
            imResize.save(f + '.tif', 'TIFF', quality=90)

resize()
