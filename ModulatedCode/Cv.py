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
mean_energy_squared = Esquared.get_mean_energy_squared(lattice)
mean_energy = (Etotal.get_total_energy(lattice))/n**2

def Cv(mean_energy_squared, mean_energy):
	Cv = (mean_energy_squared - mean_energy)
	return Cv






