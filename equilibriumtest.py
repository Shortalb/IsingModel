"""
=====
main.py code altered to run tests to find number of steps to reach equilirbium
=====
"""
import numpy as np
import matplotlib.pyplot as plt





T = 0.0001#temp in kelvin
n = 100 # matrix size

h = 0


def lattice_creator(n): #new function to make lattice
    lattice = np.random.choice([-1,1], [n,n]) #random n*m long list, reshape to n,m matrix

    return lattice

lattice = lattice_creator(n) #assign the lattice name to the output of function



def spin_flipper(T): #function to select and flip a random spin
    i = np.random.randint(0,n-1) #random row
    j = np.random.randint(0,n-1) #random column
    #print i,j
    r = np.random.random()

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

    #### mean magnetisation per spin
def get_mean_magnetisation(lattice):
    #initialising value of total magnetisation    
    total_magnetisation = float(0)

    for i in range(0,n-1):
        for j in range(0,n-1):
            total_magnetisation += lattice[i][j]
    
    mean_magnetisation = total_magnetisation/n**2
    return mean_magnetisation


step = 1000000 #change this in accordance with lattice size n.
mean_mag_list = []
n_steps = range(step)
for iteration in range(step):
    spin_flipper(T)
    mean_magnetisation = get_mean_magnetisation(lattice)
    mean_mag_list.append(mean_magnetisation)

plt.plot(n_steps, mean_mag_list)
plt.show()

