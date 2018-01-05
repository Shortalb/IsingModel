import numpy as np

n = 5 #number of rows
m = 5 #number of columns
#create a 5x5 matrix of random 1's and 0's
A = np.random.random_sample(n*m).reshape(n,m)

lattice = np.rint(A)
print lattice
#trying to flip each spin to opposite value as a test
#n is a number not a list, must rename each array?

new_lattice = []
for i in range(m):
    k = lattice[i]
    for j in k:
        if j == 0:
            j = 1
            new_lattice.append(j)
        else:
            j = 0
            new_lattice.append(j)
newer_lattice = np.reshape(new_lattice,(n,m)) #reshapes new_lattic from 1x25 to 5x5
print newer_lattice


