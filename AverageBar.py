# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# ## Make an Average bar from a directory of images

# <codecell>

import os
import sys
import Image as img
import fnmatch
import numpy as np
import subprocess

def video2img(infile='/Volumes/Documents/colbrydi/Documents/DirksWork/2013 iCER VIdeos/GlobusOnline/media/GlobusOnline.mp4'):
    path, ext = os.path.splitext(infile)
    dir, filename = os.path.split(path)
    subprocess.call(['mkdir', '-p', filename])
    subprocess.check_output(['ffmpeg', '-i', infile, '-r', '1', '-f', 'image2', './'+filename+'/image-%6d.png'])
    return filename

def writeim(im,filename):
    #size = (im.shape[0], im.shape[1])
    #im = im.reshape(im.shape[0]*im.shape[1],im.shape[2])
    #im2 = img.frombuffer('RGB', size, im, 'raw', 'RGB', 0,1)
    im2 = img.fromarray(np.uint8(im))
    im2.save(filename)

def readim(filename):
    print(filename)
    im = img.open(filename) 
    im2 = np.asarray(im)
    #im2 = np.array(im.getdata()).reshape(im.size[0], im.size[1], 3)
    return im2;
    
def AverageBar(indir='/Volumes/Documents/colbrydi/Documents/DirksWork/chamview/ChamB/'):
    tot = 0.0;
    R = np.array([0,0,0]);
    G = np.array([0,0,0]);
    B = np.array([0,0,0]);
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            if fnmatch.fnmatch(f,'*.jpeg'):
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
