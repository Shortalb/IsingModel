#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import totalenergy as Etotal
import getenergychange as Eget
import latticecreator as LatticeGet
import getmeanmag as Mget
T = 2.0 #temp multiplied by kB
n = 128 # matrix size
h = 0.0 #external magnetic field value

####mean energy square per spin

def get_mean_energy_squared(lattice):

	energy_squared = float(0)

	for i in range(0,n):
		for j in range(0,n):
			energy_squared += (Eget.get_energy_change(h,i,j))*2
	mean_energy_squared = energy_squared/n**2
	return mean_energy_squared
