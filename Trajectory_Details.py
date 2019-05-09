# MDAnalysis Script to print the trajectory details
#
# Authour: Anji Babu Kapakayala
# 	    IIT KANPUR, India.
# 
#
#------------------------------------#
# Import required libraries
import numpy as np
import sys, os
import math as math
import MDAnalysis as MDA

# Pass xtc and Gro files AS arguments to the script
#gro = sys.argv[1]
#xtc = sys.argv[2]

# Trajectory file names
gro = "prod.gro"
xtc = "pbc.xtc"

print ("Given Input files are:\n\n",gro, "and", xtc,"\n")

# Read the Trajectory and get Number of frames
u = MDA.Universe(gro,xtc)
num_frames = len(u.trajectory)
num_atoms = len(u.atoms)
residues = len(u.atoms.residues)

# Atom Selection
protein = u.select_atoms("protein")
protein_atoms =len(protein)
water = u.select_atoms("resname WAT")
water_atoms = len(water)
protein_residues = len(protein.residues)
water_residues = len(water.residues)

# BOX dimensions
box = u.dimensions

# Print Details
print ("No. of Frams : ",num_frames,"\nNo. of Atoms : ",num_atoms, "\nNo. of Residues: ",residues,"\nNo. of Protein Atoms:",protein_atoms, "\nNo. of Water Atoms: ",water_atoms,"\nNo. of Protein Residues",protein_residues,"\nNo. of Water Residues:", water_residues,"\n BOX Size: ",box[:3],"\n")
#---------------------------------------------------#
#          Anji Babu Kapakayala   		    #
#---------------------------------------------------#
#
