"""
=============
This script uses the 1.1 to to create and flip a lattice
Additionally it plots both the initial and flipped lattices 
Black and White are dependent on 1 or 0 values at each site
=============
"""


import numpy as np
from PIL import Image
n = 50 #number of rows
m = 50 #number of columns

A = np.random.random_sample(n*m)
B = np.rint(A) #will use this array in the display as has to be 1 x (n*m)
lattice = np.reshape(B, (n,m))
#making and reshaping random lattice

init_img = Image.new('1', (n,m))
init_img.putdata(B)
init_img.show() #displaying initial lattice


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
            
#for loop to flip each lattice site
flip_lattice = np.reshape(new_lattice,(n,m)) 


string_flip_lattice = np.reshape(flip_lattice, (1, n*m)) #reshaping the lattice 
# because the image only takes a 1 x n array and assigns them in sequence
printer_lattice = []
for p in string_flip_lattice[0]:
    printer_lattice.append(p)
#need for loop as string flip is an array within an array
#for loop removes the outer brackets


img = Image.new('1', (n, m))
img.putdata(printer_lattice)
img.show() #this displays the flipped lattice