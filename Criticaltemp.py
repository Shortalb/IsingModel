#!/usr/bin/env python

import numpy as np
import matplotlib.pylab as plt

T = 0.0001
n = 20
h = 0.0
J = 1.0

def lattice_creator(n):
	lattice = np.random.choice([-1,1] , [n,n] )
	return lattice
lattice = lattice_creator(n)

def get_energy_change(h,i,j):
	#periodic boundary conditions
	top = lattice[(i-1)%n][j]
	bottom = lattice[(i+1)%n][j]
	left = lattice[i][(j-1)%n]
	right = lattice[i][(j+1)%n]


	#defining the hamiltonian
	net_spin = top + bottom + left + right 
	
	chosen_spin = lattice[i][j]
	energy_change = -2*chosen_spin*(net_spin*J + h) 
	return energy_change

def spin_flipper(T):
	i = np.random.randint(0,n)
	j = np.random.randint(0,n)
	r = np.random.random()

	energy_change = get_energy_change(h,i,j)

	flip_clause = np.exp(energy_change/T)
	flip_clause = float(flip_clause)

	if energy_change >= 0:
		lattice[i][j] = -lattice[i][j]

	elif r < flip_clause:
		lattice[i][j] = -lattice[i][j]

	return lattice

def get_mean_magnetisation(lattice):
	#intialising value of total magnetisation
	total_magnetisation = float(0)
	
	for i in range(0,n-1):
		for j in range(0, n-1):
			total_magnetisation += lattice[i][j]

	mean_magnetisation = total_magnetisation/n**2
	return mean_magnetisation

temps = np.arange(0.1,5.0,0.1)
mean_mag_list = []
plt.title("Initial Lattice")
plt.imshow(lattice)
plt.show()

for temp in temps:
	print temp

	for iteration in range(1000000):
		spin_flipper(temp)
	mean_mag = get_mean_magnetisation(lattice)
	mean_mag_list.append(mean_mag)
plt.plot(temps, mean_mag_list)
plt.title("Plot Showing Critical Temperature")
plt.xlabel("Temperature")
plt.ylabel("Mean Magnetisation Per Spin")
plt.show()
plt.imshow(lattice)
plt.title("Final Lattice")
plt.show()
plt.show()

