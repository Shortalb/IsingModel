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


def spin_flipper(T): #function to select and flip a random spin

    #generating random variables
    i = np.random.randint(0,n) #changed randint to np.random.randint
    j = np.random.randint(0,n) #
    r = np.random.random()

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
def graph_equilibrium_test():
	mean_mag_list = []
	steps = range(1000)
	for iteration in steps:
		spin_flipper(T)
		mean_magnetisation = Mget.get_mean_magnetisation(lattice)
		mean_mag_list.append(mean_magnetisation)
	plt.plot(steps, mean_mag_list)
######add labels#####
	plt.show()

def get_crit_temp_graph():
	mean_mag_list= []
	temps = np.arange(0.05, 5.0,0.05)

	for temp in temps:
		print temp
		for iteration in range(50):
			spin_flipper(temp)
		mean_mag = Mget.get_mean_magnetisation(lattice)
		mean_mag_list.append(mean_mag)

	plt.plot(temps, mean_mag_list)
	plt.title("Plot showing critical temperature")
	plt.xlabel("Temperature")
	plt.ylabel("Mean magnetisation per spin")
	plt.grid(True)
	plt.show()
get_crit_temp_graph()
