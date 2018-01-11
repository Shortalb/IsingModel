#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import totalenergy as Etotal
import getenergychange as Eget
import latticecreator as LatticeGet
import getmeanmag as Mget
import meanesquared as Esquared
import meanmagsquared as Msquared 
T = 2.0 #temp multiplied by kB
n = 128 # matrix size
h = 0.0 #external magnetic field value

lattice = LatticeGet.lattice_creator(n)
mean_magnetisation = Mget.get_mean_magnetisation(lattice)
mean_mag_squared = Msquared.get_mean_mag_squared(lattice)

def get_magnetic_susc(mean_mag_squared, mean_magnetisation):
    mag_susc = (mean_mag_squared - mean_magnetisation)
    return mag_susc

