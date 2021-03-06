# -*- coding: utf-8 -*-
import os
import sys
from imIO import *
import Image as img
import fnmatch
import numpy as np
import subprocess

def AverageBar(indir='/Volumes/Documents/colbrydi/Documents/DirksWork/chamview/ChamB/'):
    tot = 0.0;
    R = np.array([0,0,0]);
    G = np.array([0,0,0]);
    B = np.array([0,0,0]);
    for root, dirs, filenames in os.walk(indir):
        filenames.sort()
        for f in filenames:
            if fnmatch.fnmatch(f,'0*.jpeg'):
                im = readim(os.path.join(root,f))
                sz = im.shape[0]
                #print(im.shape)
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
    if tot==0:
        print('ERROR - No files found in '+indir)
        return '' 
    im3 = np.zeros((R.shape[0],R.shape[1], 3))
    im3[:,:,0] = R
    im3[:,:,1] = G
    im3[:,:,2] = B 
    return im3

import time
tic = time.time()
im4 = AverageBar(sys.argv[1])
toc = time.time()
print(toc-tic)
writeim(im4, sys.argv[1]+'/AverageBar.jpeg')

#x = '/Volumes/Documents/colbrydi/Documents/DirksWork/2013 iCER VIdeos/GlobusOnline/media/GlobusOnline.mp4'
#im = AverageBar('./GlobusOnline/')

#x = '/Volumes/Documents/colbrydi/Documents/DirkArchive/2012/2012 Break Videos/HPCCUSB/media/HPCCUSB.mp4'
#im = AverageBar('./HPCCUSB/')


# <codecell>
