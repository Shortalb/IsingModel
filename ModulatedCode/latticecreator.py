#!/usr/bin/env python

import numpy as np
import totalenergy as Etotal
import getenergychange as Eget

n = 128

def lattice_creator(n): #new function to make lattice
        lattice = np.random.choice([-1,1], [n,n]) 
        return lattice



