
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint




T = 2.7  #temp in kelvin
n = 180 # matrix size

h = 0


def lattice_creator(n): #new function to make lattice
    A = lattice = np.random.choice([-1,1], [n,n]) #random n*m long list, reshape to n,m matrix

    return lattice

lattice = lattice_creator(n) #assign the lattice name to the output of function



def spin_flipper(T): #function to select and flip a random spin
    i = randint(0,n-1) #random row
    j = randint(0,n-1) #random column
    #print i,j
    r = random.random()

    energy = 0.0

    top = lattice[(i-1)%n][j] #assigning name to above neighbour
    bottom = lattice[(i+1)%n][j] #assigning name to below neighbour
    left = lattice[i][(j-1)%n]
    right = lattice[i][(j+1)%n]

    net_spin = top + bottom + left + right
    chosen_spin = lattice[i][j]
    energy_change = -2*chosen_spin*(net_spin+h)
    energy_change = float(energy_change)
    #print energy_change
    flip_clause = np.exp(energy_change/(T))
    flip_clause = float(flip_clause)
    #print flip_clause , "flip clause", r, "random no"
    #print flip_clause
    if energy_change >= 0:
        lattice[i][j] = -lattice[i][j]

        energy += energy_change
        return energy


    elif r < flip_clause:
        lattice[i][j] = -lattice[i][j]
        energy += energy_change
        return energy
    return lattice
    return energy
        #print "spin flipped randomly"

spin_flipper(T)
print lattice
