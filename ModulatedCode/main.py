#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import totalenergy as Etotal
import getenergychange as Eget
import latticecreator as LatticeGet
import getmeanmag as Mget
import meanesquared as Esquared
import meanmagsquared as Msquared 
import Cv as cv
import magsusc 
T = 2.0 #temp multiplied by kB
n = 128 # matrix size
h = 0.0 #external magnetic field value


lattice = LatticeGet.lattice_creator(n) #globalise the name lattice
mean_energy_squared = Esquared.get_mean_energy_squared(lattice)
mean_energy = (Etotal.get_total_energy(lattice))/n**2
mean_mag_squared = Msquared.get_mean_mag_squared(lattice)
mean_magnetisation = Mget.get_mean_magnetisation(lattice)

def spin_flipper(T): #function to select and flip a random spin

    #generating random variables
    i = np.random.randint(0,n) #changed randint to np.random.randint
    j = np.random.randint(0,n) #
    r = numpy.random.random()
    
    #calling get energy change and assigning name to result
    energy_change = Eget.get_energy_change(h,i,j)

    #defining the finite probability flip clause
    flip_clause = np.exp(energy_change/(T)) 
    flip_clause = float(flip_clause)

    #if hamiltonian is >= 0 flip spin 
    if energy_change >= 0:
        lattice[i][j] = -lattice[i][j]
        
    #implementing finite probability clause
    elif r < flip_clause:
        lattice[i][j] = -lattice[i][j]
    
    return lattice

print Etotal.get_total_energy(lattice)
print Mget.get_mean_magnetisation(lattice)
print Esquared.get_mean_energy_squared(lattice)
print Msquared.get_mean_mag_squared(lattice)
print cv.Cv(mean_energy_squared, mean_energy)
print magsusc.get_magnetic_susc(mean_mag_squared, mean_magnetisation)
