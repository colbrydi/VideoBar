# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# ## Make an Average Image from a directory of images

# <codecell>

import os
import fnmatch
import matplotlib.image as img
import matplotlib.pyplot as plt
import skimage.color as color
import numpy as np

def AverageImage(indir='/Volumes/Documents/colbrydi/Documents/DirksWork/chamview/ChamB/'):
    tot = 0.0;
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if fnmatch.fnmatch(f,'*.png'):
                im = img.imread(os.path.join(root,f))
                if tot==0:
                    R = im[:,:,0]
                    G = im[:,:,1]
                    B = im[:,:,2]
                else:
                    R = R+im[:,:,0]
                    G = G+im[:,:,1]
                    B = B+im[:,:,2]
                tot=tot+1
    im[:,:,0] = R/tot
    im[:,:,1] = G/tot
    im[:,:,2] = B/tot
        
    return im

# <codecell>

import time
tic = time.time()
im4 = AverageImage()
toc = time.time()
print(toc-tic)

# <codecell>

plt.imshow(im4)

# <codecell>

x = '/Volumes/Documents/colbrydi/Documents/DirksWork/2013 iCER VIdeos/GlobusOnline/media/GlobusOnline.mp4'
im = AverageImage('./GlobusOnline/')
plt.imshow(im)

# <codecell>

x = '/Volumes/Documents/colbrydi/Documents/DirkArchive/2012/2012 Break Videos/HPCCUSB/media/HPCCUSB.mp4'
im = AverageImage('./HPCCUSB/')
plt.imshow(im)

# <codecell>


