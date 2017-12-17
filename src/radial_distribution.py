import numpy as np

def calculate_gr(xyz,nbins,bin_width,density,radius):
    '''
    Calculates the radial distribution g(r) of a given set of coordinates xyz
    over a range of distances, with a given bin width,  normalised to the density.
    In the calculation are included the molecules within a given radius.
    '''

    n_all       = xyz.shape[0]
    histogram   = np.zeros(nbins)
    shell       = np.zeros(nbins)
    distance    = calculate_distance_from_center(xyz)
    n_molecules  = 0

    for i in range(0,n_all-1):
        if distance[i]<radius:
            n_molecules += 1
            for j in range(i+1,n_all):
                dist = np.linalg.norm(xyz[j]-xyz[i])
                index = int(round(dist/bin_width))
                if index<nbins:
                    histogram[index] += 2

    for i in range(nbins):
        shell[i] = 4.0*np.pi*(np.power((i+1)*bin_width,3)-np.power(i*bin_width,3))/3.0

    print n_molecules
    gr = histogram/n_molecules/shell/density
    return gr

def calculate_distance_from_center(xyz):
    '''
    Calculates the distance from the center of mass
    '''
    center   = np.average(xyz,axis=0)
    distance = np.zeros(xyz.shape[0])
    for i in range(xyz.shape[0]):
        distance[i] = np.linalg.norm(center-xyz[i])
    return distance
