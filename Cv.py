import numpy as np
import matplotlib.pyplot as plt
from random import randint
import random


T = 1.0 #temp multiplied by kB
n = 150# matrix size
h = 0.0 #external magnetic field value
J = -1 #coupling constant

def lattice_creator(n): #new function to make lattice
        lattice = np.random.choice([-1,1], [n,n]) 
        return lattice
lattice = lattice_creator(n) #globalise the name lattice

def get_energy_change(h,i,j):
    
    #periodic boundary conditions
    top = lattice[(i-1)%n][j] 
    bottom = lattice[(i+1)%n][j] 
    left = lattice[i][(j-1)%n] 
    right = lattice[i][(j+1)%n]
    
    #defining the hamiltonian 
    net_spin = top + bottom + left + right
    chosen_spin = lattice[i][j]
    energy_change = -2*chosen_spin*(net_spin*J+h)
    
    return energy_change




def fin_splipper(T,h): #function to select and flip a random spin

    #generating random variables
    i = randint(0,n-1) #random row
    j = randint(0,n-1) #random column 
    r = random.random()
    
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


def get_mean_square_energy(lattice):
    energy_squared = float(0)
    for i in range(0,n-1):
        for j in range(0,n-1):
            energy_squared = energy_squared + (get_energy_change(h,i,j))**2
    mean_energy = energy_squared/n**2
    return mean_energy
mean_energy = get_mean_square_energy(lattice)
