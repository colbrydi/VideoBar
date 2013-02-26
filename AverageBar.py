# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# ## Make an Average bar from a directory of images

# <codecell>

import os
import fnmatch
import skimage.color as color
import numpy as np

def AverageBar(indir='/Volumes/Documents/colbrydi/Documents/DirksWork/chamview/ChamB/'):
    tot = 0.0;
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if fnmatch.fnmatch(f,'*.png'):
                im = img.imread(os.path.join(root,f))
                sz = im.shape[0]
                r = np.zeros((sz,1))
                g = np.zeros((sz,1))
                b = np.zeros((sz,1))
                r[:,0] = np.average(im[:,:,0],1)
                g[:,0] = np.average(im[:,:,1],1)
                b[:,0] = np.average(im[:,:,2],1)
                if tot==0:
                    R = r
                    G = g
                    B = b
                else:
                    R = np.append(R, r, axis=1)
                    G = np.append(G, g, axis=1)
                    B = np.append(B, b, axis=1)
                tot=tot+1
    im3 = np.zeros((R.shape[0],R.shape[1], 3))
    im3[:,:,0] = R
    im3[:,:,1] = G
    im3[:,:,2] = B 
    return im3

# <codecell>

import time
tic = time.time()
im4 = AverageBar()
toc = time.time()
print(toc-tic)

# <codecell>

plt.imshow(im4)

# <codecell>

x = '/Volumes/Documents/colbrydi/Documents/DirksWork/2013 iCER VIdeos/GlobusOnline/media/GlobusOnline.mp4'
im = AverageBar('./GlobusOnline/')
plt.imshow(im)

# <codecell>

x = '/Volumes/Documents/colbrydi/Documents/DirkArchive/2012/2012 Break Videos/HPCCUSB/media/HPCCUSB.mp4'
im = AverageBar('./HPCCUSB/')
plt.imshow(im)

# <codecell>


# <codecell>


