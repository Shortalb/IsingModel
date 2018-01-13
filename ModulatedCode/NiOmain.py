#!/usr/bin/env python
"""this script is an adapted version of the latest main.py to run for an NiO lattice. To be used in conjunction with the other modules"""
import numpy as np
import matplotlib.pyplot as plt
import totalenergy as Etotal



import getmeanmag as Mget
import meanesquared as Esquared
import meanmagsquared as Msquared
#import Cv as cv
import magsusc as magsu
T = 0.00001 #temp multiplied by kB
n = 50 # matrix size
h = 0.0 #external magnetic field value


J_1 = 2.3
J_2 = -21

coupling_1 = 1.0
coupling_2 = J_2/J_1
print coupling_2





def lattice_creator(n): #new function to make lattice
        lattice = np.random.choice([-1,1], [n,n]) #for crit temp test set both values to 1 or -1 to get the same start point every time when averaging
        return lattice
lattice = lattice_creator(n)

def get_energy_change(h,i,j):
	#periodic boundary conditions
	top = lattice[(i-1)%n][j]
	bottom = lattice[(i+1)%n][j]
	left = lattice[i][(j-1)%n]
	right = lattice[i][(j+1)%n]

	diagonal_up_left = lattice[(i-1)%n][(j-1)%n]
	diagonal_down_left= lattice[(i+1)%n][(j-1)%n]
	diagonal_up_right = lattice[(i-1)%n][(j+1)%n]
	diagonal_down_right = lattice[(i+1)%n][(j+1)%n]

	#defining the hamiltonian
	net_spin_nearest = top + bottom + left + right 
	net_spin_second_nearest = diagonal_up_left + diagonal_up_right + diagonal_down_left + diagonal_down_right
	chosen_spin = lattice[i][j]
	energy_change = -2*chosen_spin*((net_spin_nearest*coupling_1 + h) + (net_spin_second_nearest*coupling_2 +h))

	return energy_change

def spin_flipper(T): #function to select and flip a random spin

    #generating random variables
    i = np.random.randint(0,n) #changed randint to np.random.randint
    j = np.random.randint(0,n) #
    r = np.random.random()

    #calling get energy change and assigning name to result
    energy_change = get_energy_change(h,i,j)

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



def graph_equilibrium_test():
	mean_mag_list = []
	sweep_size = 1000
	n_steps = 5000

	for i in range(n_steps):
		for iteration in range(sweep_size):
			spin_flipper(T)
		mean_magnetisation = Mget.get_mean_magnetisation(lattice)
		mean_mag_list.append(mean_magnetisation)
		print i
	plt.plot(range(n_steps), mean_mag_list)
	plt.title("Equilibrium Test for 50x50 NiO Lattice")
	plt.xlabel("Number of Steps")
	plt.ylabel("Mean Magnetisation Per Spin")
	plt.grid(True)
	plt.show()
#graph_equilibrium_test()
#plt.imshow(lattice)
#plt.show()

def get_mean_energy(lattice):

    #initialising the energy to zero
    energy = float(0)

    #for loops to run through each row (i) and each element in that row(j)
    for i in range(0,n):
        for j in range(0,n):
            energy = energy + get_energy_change(h,i,j)
    mean_energy = (energy*0.5)/n**2
    return mean_energy

####ground state energy test
def get_ground_state_energy():
	mean_energy_list = []
	temps = np.arange(0.05,5.0,0.05)

	for temp in temps:
		for iteration in range(100000):
			spin_flipper(temp)

		mean_energy = get_mean_energy(lattice)
		mean_energy_list.append(mean_energy)	
		print temp
		print mean_energy

	plt.plot(temps, mean_energy_list)
	plt.title("Plot showing ground state energy")
	plt.xlabel("Temperature")
	plt.ylabel("Mean energy per spin")
	plt.grid(True)
	plt.show()

	f = open("data.py", "w")
	mean_energy_list[-1] = "stop"
	f.write(",".join(map(lambda x: str(x), mean_energy_list)))
	f.close()
#get_ground_state_energy()


####critical temperature test ####
def get_crit_temp_graph():

	mean_mag_list= []
	temps = np.arange(0.05, 5.0,0.05)

	for temp in temps:
		for iteration in range(100000):
			spin_flipper(temp)
		mean_magnetisation = Mget.get_mean_magnetisation(lattice)
		mean_mag_list.append(mean_magnetisation)
		print temp


	plt.plot(temps, mean_mag_list)
	plt.title("Plot showing critical temperature")
	plt.xlabel("Temperature")
	plt.ylabel("Mean magnetisation per spin")
	plt.grid(True)
	plt.show()

	f = open("data.py", "w")
	mean_mag_list[-1] = "stop"
	f.write(",".join(map(lambda x: str(x), mean_mag_list)))
	f.close()
#get_crit_temp_graph()


#########magnetic susc graph####
def get_mag_susc_graph():
	mean_magnetisation = Mget.get_mean_magnetisation(lattice)
	mean_mag_squared = Msquared.get_mean_mag_squared(lattice)
	mag_susc_list = []
	temps = np.arange(0.05,5.0,0.05)
	for temp in temps:
		for iteration in range(100000):
			spin_flipper(temp)
		mag_susc = magsu.get_magnetic_susc(mean_mag_squared, mean_magnetisation)
		mag_susc_list.append(mag_susc)
		print mag_susc

	plt.plot(temps, mag_susc_list)
	plt.title("Plot Showing Magnetic Susceptibility vs Temperature")
	plt.ylabel("Magnetic Susceptibility")
	plt.xlabel("Temperature")
	plt.grid(True)
	plt.show()
#get_mag_susc_graph()
