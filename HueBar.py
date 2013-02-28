# ## ImageBar Function
# 
# Usage: 
# 
#     bar = ImageBar(filename, size)
# 
# 
# TODO: Fix this function to allow for saturation and value.

from imIO  import *
import Image as img
import sys
import skimage.color as color
import numpy as np
import os
import fnmatch

def HueBar(filename='', sz=''):
    
    if filename == '':
        print('File not found');
        return
    else: 
        im = readim(filename)
   
    #Total number of pixels
    tot = np.float(np.size(im,0) * np.size(im,1))
    #Determin the hight of the new bar image
    if sz == '':
        sz = np.size(im,0)
     
    # Convert to HSV color space
    im2 = color.rgb2hsv(im)
    h = im2[:,:,0]
    s = im2[:,:,1]
    v = im2[:,:,2]

    #Remove dark colors
    flag = tuple(i < 0.02 for i in v)
    flag = np.asarray(flag)
    h2 = h[~flag]
    flag = np.double(flag)
    ztot = sum(sum(flag))
    h = np.asarray(h)
    z = np.float(ztot)/tot * sz
    X = np.zeros([z,1])
    Y = np.ones((sz,1))*0.5
    Y[0:z,:] = 0
    
    if np.size(h2) > 0:
        #Calculate histogram on color (H) space
        n, bins = np.histogram(h2, bins=100)
        n = n/tot * sz
        for i in range(0,np.size(bins)-1):
            next = np.ones([round(n[i]),1])*np.average(bins[i]+bins[i+1])
            X = np.append(X, next, axis=0)
                
        if np.size(X,0) < sz:
            X = np.append(X, np.zeros([sz - np.size(X,1),1]), axis=0)
        if np.size(X,0) > sz:
            X= X[0:sz,:]
        
    im3 = np.zeros((np.size(X,0),1, 3))
    im3[:,:,0] = X
    im3[:,:,1] = 1 
    im3[:,:,2] = Y     
        
    return im3,sz

# ## makeVideoBar from directory of images
# 
# TODO: Fix this function and move the HSV integration to the previous funciton to allow for saturation and value.


def makeVideoBar(indir='/Volumes/Documents/colbrydi/Documents/DirksWork/chamview/ChamB/'):
    sz=''
    br=''
    for root, dirs, filenames in os.walk(indir):
        filenames.sort()
        for f in filenames:
            if fnmatch.fnmatch(f,'0*.jpeg'):
                (ib, sz) = HueBar(os.path.join(root,f),sz);
                if br == '':
                    br = ib
                else:
                    br = np.append(br, ib, axis=1)
    bar = color.hsv2rgb(br)
    bar = bar * 255
    return bar

import time
tic = time.time()
im4 = makeVideoBar(sys.argv[1])
toc = time.time()
print(toc-tic)
writeim(im4, sys.argv[1]+'/HueBar.jpeg')
