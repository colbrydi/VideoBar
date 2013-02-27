# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# ## ImageBar Function
# 
# Usage: 
# 
#     bar = ImageBar(filename, size)
# 
# 
# TODO: Fix this function to allow for saturation and value.

# <codecell>

import matplotlib.image as img
import matplotlib.pyplot as plt
import skimage.color as color
import numpy as np

def ImageBar(filename='', sz=''):
    
    if filename == '':
        print('File not found');
        return
    if filename != '':
        #print(filename)
        im = img.imread(filename)
    #plt.imshow(im)
    
    #Total number of pixels
    tot = float(size(im,0) * size(im,1))
 
    #Determin the hight of the new bar image
    if sz == '':
        sz = size(im,0)
     
    # Convert to HSV color space
    im2 = color.rgb2hsv(im)
    h = im2[:,:,0]
    s = im2[:,:,1]
    v = im2[:,:,2]
    #plt.imshow(v)
    #plt.colorbar()
       
    #Remove dark colors
    flag = tuple(i < 0.2 for i in v)
    flag = np.asarray(flag)
    ztot = sum(flag)
    h = np.asarray(h)
    h2 = h[~flag]
    z = float(ztot)/tot * sz
    X = zeros([z,1])
    Y = ones((sz,1))
    Y[0:z,:] = 0
    
    #print(tot)
    #print(ztot)
    
    #Calculate histogram on color (H) space
    n, bins = np.histogram(h2, bins=100)
    n = n/tot * sz
    for i in range(0,size(bins)-1):
        next = np.ones([round(n[i]),1])*bins[i]
        X = np.append(X, next, axis=0)
        
        
    if size(X,0) < sz:
        X = np.append(X, zeros([sz - size(X,1),1]), axis=0)
    if size(X,0) > sz:
        X = X[0:sz,:]
        
    im3 = zeros((size(X,0),1, 3))
    im3[:,:,0] = X
    im3[:,:,1] = 1
    im3[:,:,2] = Y     

        
    return im3;
    

# <codecell>

def extrapolatebar(ib):
    vsz = 800
    hsz = 40
    br = zeros([vsz,hsz,3])
    for c in range((0,hsz)):
       br[:,c,:] = ib
    bar = color.hsv2rgb(br)
    return bar

# <codecell>

ib = ImageBar('/Volumes/Documents/colbrydi/Documents/DirksWork/chamview/ChamB/img-000339.png')

# <codecell>

bar = extrapolatebar(ib)
plt.imshow(bar)

# <markdowncell>

# ## makeVideoBar from directory of images
# 
# TODO: Fix this function and move the HSV integration to the previous funciton to allow for saturation and value.

# <codecell>

import os
import fnmatch

def makeVideoBar(indir='/Volumes/Documents/colbrydi/Documents/DirksWork/chamview/ChamB/'):
    sz = 800
    br = zeros([sz,1,3])
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if fnmatch.fnmatch(f,'*.png'):
                ib = ImageBar(os.path.join(root,f), sz);
                br = np.append(br, ib, axis=1)
    bar = color.hsv2rgb(br)
    return bar

# <codecell>

import time
tic = time.time()
im4 = makeVideoBar()
toc = time.time()
print(toc-tic)

# <codecell>

plt.imshow(im4)

# <codecell>

import subprocess
def video2img(infile='/Volumes/Documents/colbrydi/Documents/DirksWork/2013 iCER VIdeos/GlobusOnline/media/GlobusOnline.mp4'):
    path, ext = os.path.splitext(x)
    dir, filename = os.path.split(path)
    subprocess.call(['mkdir', '-p', filename])
    subprocess.check_output(['ffmpeg', '-i', infile, '-r', '1', '-f', 'image2', './'+filename+'/image-%6d.png'])
    return filename

# <codecell>

import subprocess
def makeBarFromVideo(infile='/Volumes/Documents/colbrydi/Documents/DirksWork/2013 iCER VIdeos/GlobusOnline/media/GlobusOnline.mp4'):
    folder=video2img(infile)
    tic = time.time()
    im4 = makeVideoBar(folder)
    toc = time.time()
    print(toc-tic)
    plt.imshow(im4)
    return im4
    

# <codecell>

x = '/Volumes/Documents/colbrydi/Documents/DirksWork/2013 iCER VIdeos/GlobusOnline/media/GlobusOnline.mp4'
im = makeBarFromVideo(x)

# <codecell>

x = '/Volumes/Documents/colbrydi/Documents/DirkArchive/2012/2012 Break Videos/HPCCUSB/media/HPCCUSB.mp4'
im = makeBarFromVideo(x)

# <codecell>


# <codecell>

x = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

# <codecell>

print(x)

# <codecell>

f = tuple( i < 5 for i in x)

# <codecell>

print(f)

# <codecell>

true + false

# <codecell>

True + False

# <codecell>

True + True

# <codecell>


