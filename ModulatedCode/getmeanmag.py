#!/usr/bin/env python
n = 128
h = 0.0

import getenergychange as Eget
import numpy as np
import latticecreator as LatticeGet


#####mean magnetisation per spin

def get_mean_magnetisation(lattice):
	total_magnetisation = float(0)

	for i in range(0,n):
		for j in range(0,n):
			total_magnetisation += lattice[i][j]
	mean_magnetisation = total_magnetisation/n**2
	return mean_magnetisation
