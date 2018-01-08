"""
=============
Only changes made to 1.2 version is changing the zeros in the lattice to negative one
=============
This version doesnt allow for imaging of the lattice due to the picture format taking 0's not -1's
=============
Will solve this problem in later version. Possibly just need to change back to 0/1 format
=============
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint



n = 10 #number of rows
m = 10 #number of columns

def lattice_creator(n,m): #new function to make lattice
    A = np.random.random_sample(n*m) #random n*m long list, reshape to n,m matrix
    lattice = np.rint(A)
    return lattice

lattice = lattice_creator(n,m) #assign the lattice name to the output of function

for k in range(len(lattice)):
    if lattice[k] == 0:
        lattice[k] = -1
    else:
        lattice[k] = 1
lattice = np.reshape(lattice, (n,m)) #have to leave reshape til here due to 0/-1 conundrum

print lattice

def spin_flipper(lattice): #function to select and flip a random spin
    i = randint(0,n-1) #random row
    j = randint(0,m-1) #random column 

    if lattice[i][j] == -1: #if site is a 0
        lattice[i][j] = 1 #flip to a 1
    else:
        lattice[i][j] = -1 #else flip to a zero


