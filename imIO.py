# -*- coding: utf-8 -*-

import os
import sys
import Image as img
import numpy as np

def video2img(infile='/Volumes/Documents/colbrydi/Documents/DirksWork/2013 iCER VIdeos/GlobusOnline/media/GlobusOnline.mp4'):
    path, ext = os.path.splitext(infile)
    dir, filename = os.path.split(path)
    subprocess.call(['mkdir', '-p', filename])
    subprocess.check_output(['ffmpeg', '-i', infile, '-r', '1', '-f', 'image2', './'+filename+'/image-%6d.png'])
    return filename

def writeim(im,filename):
    im2 = img.fromarray(np.uint8(im))
    im2.save(filename)

def readim(filename):
    print(filename)
    im = img.open(filename) 
    im2 = np.asarray(im)
    return im2;
    
