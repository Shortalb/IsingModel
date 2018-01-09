
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

def spin_flipper(): #function to select and flip a random spin
    i = randint(1,n-2) #random row
    j = randint(1,m-2) #random column
    print "Row :", i , "Column :" , j #printing which site is chosen
    top = lattice[i-1][j] #assigning name to above neighbour
    bottom = lattice[i+1][j] #assigning name to below neighbour
    left = lattice[i][j-1]
    right = lattice[i][j+1]
    if (top + bottom + left + right) > 0: #if nearest neighbours are net up
        lattice[i][j] = 1 #flip to a 1
        print "flip up"

    elif (top + bottom + left + right) < 0:
        lattice[i][j] = -1 #else flip to down
        print "flip down"
    else:
        print "sum is 0!"
spin_flipper()
print lattice
#testing testing 1,2
