#!/usr/bin/env python
import numpy as np
import totalenergy as Etotal
import latticecreator as LatticeGet

n = 128
h = 0.0
lattice = LatticeGet.lattice_creator(n)
def get_energy_change(h,i,j):
    
    #periodic boundary conditions
    top = lattice[(i-1)%n][j] 
    bottom = lattice[(i+1)%n][j] 
    left = lattice[i][(j-1)%n] 
    right = lattice[i][(j+1)%n]
    
    #defining the hamiltonian 
    net_spin = top + bottom + left + right
    chosen_spin = lattice[i][j]
    energy_change = -2*chosen_spin*(net_spin+h)
    
    return energy_change


