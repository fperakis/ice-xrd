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

def iceXII_parameters():
    # taken from Nature 391, 268 (1998) https://www.nature.com/articles/34622
    file_name = 'ice12'
    density_XII = 1.4665
    density = density_XII*10**(-24)/((2*1.0079+15.999)/(6.022*10**23))

    dOOa = 8.304
    dOOc = 4.024

    dx = dOOa
    dy = dOOa
    dz = 2*dOOc

    return file_name, density, dx, dy, dz

def iceIV_parameters():
    # taken from http://www1.lsbu.ac.uk/water/ice_iv.html
    file_name = 'ice4'
    density_IV = 1.272

    density = density_IV*10**(-24)/((2*1.0079+15.999)/(6.022*10**23))

    dOOa = 7.60
    angle = 70.1
    dx = 6.9122#dOOa*np.sin(angle * np.pi / 180.)
    dy = 1.8569#dOOa*np.cos(angle * np.pi / 180.)
    #dx = 2*dOOa*np.cos((90-angle) * np.pi / 180.)
    #dy = 2*dOOa*np.sin(angle * np.pi / 180.)
    dz = 2*dOOa

    return file_name, density, dx, dy, dz

