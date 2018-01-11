#!/usr/bin/env python
n = 128
h = 0.0
####### total energy
import getenergychange as Eget
import numpy as np
import latticecreator as LatticeGet

def get_total_energy(lattice):
    
    #initialising the energy to zero
    energy = float(0)    
    
    #for loops to run through each row (i) and each element in that row(j)
    for i in range(0,n-1):
        for j in range(0,n-1):
            energy = energy + Eget.get_energy_change(h,i,j)
    return energy*0.5
