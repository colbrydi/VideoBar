# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# ## Make an Average Image from a directory of images

# <codecell>

import os
import sys
import fnmatch
import Image as img
import numpy as np
from imIO import *


def AverageImage(indir='/Volumes/Documents/colbrydi/Documents/DirksWork/chamview/ChamB/'):
    tot = 0.0;
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if fnmatch.fnmatch(f,'0*.jpeg'):
                im = readim(os.path.join(root,f))
                if tot==0:
                    R = np.double(im[:,:,0])
                    G = np.double(im[:,:,1])
                    B = np.double(im[:,:,2])
                else:
                    R = R+np.double(im[:,:,0])
                    G = G+np.double(im[:,:,1])
                    B = B+np.double(im[:,:,2])
                tot=tot+1
    im = np.zeros((R.shape[0],R.shape[1], 3))
    im[:,:,0] = (R/tot)
    im[:,:,1] = (G/tot)
    im[:,:,2] = (B/tot)
    return im

# <codecell>

import time
tic = time.time()
im = AverageImage(sys.argv[1])
toc = time.time()
print(toc-tic)
writeim(im, sys.argv[1]+'/AverageImage.jpeg')

