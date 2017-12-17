import numpy as np
from prody import *

def shift_structure(oxgs,dx=0,dy=0,dz=0):
    '''
    shifts the structure by by dx, dy, dz
    '''
    # shift by dxyz
    xyz = oxgs.getCoords()
    dxyz = np.zeros(xyz.shape)
    dxyz[:,0] = dx
    dxyz[:,1] = dy
    dxyz[:,2] = dz

    # shifted copy
    oxgs_shifted = oxgs.copy()
    oxgs_shifted.setCoords(xyz+dxyz)

    return oxgs_shifted

def expand_ice(oxgs,n=1,dx=0,dy=0,dz=0):
    '''
    expands ice by along (dx,dy,dz) n times
    '''
    expanded = oxgs.copy()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                expanded += shift_structure(oxgs,dx=i*dx,dy=j*dy,dz=k*dz)

    print 'Crystal expanded: %dA x %dA x %dA '%(dx*n,dy*n,dz*n)
    return expanded


