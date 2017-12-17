import numpy as np

def iceIh_parameters():
    # taken from http://www1.lsbu.ac.uk/water/hexagonal_ice.html
    file_name = 'ice1h'
    density_Ih = 0.917
    density = density_Ih*10**(-24)/((2*1.0079+15.999)/(6.022*10**23))

    dOOa = 4.5181
    dOOb = np.sqrt(3.)*dOOa
    dOOc = 7.3560

    dx = dOOb*3
    dy = dOOc*3
    dz = 6*dOOa

    return file_name, density, dx, dy, dz
