# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:20:45 2015

@author: Vivian Shen
percolation module
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

def copy_site_vacancy(in_file):
    """Create a site vacancy matrix from a text file.

    infile_name is the name (a string) of the
    text file to be read. The method should return 
    the corresponding site vacancy matrix represented
    as a numpy array
    """
 
    f = open(infile_name, 'r') #opens the file
    d = f.readline() #reads the first line of the file, the dimension
    size = int(d)
    sites = np.ones(size*size) #creates an temp array of ones
    sites.shape = (size,size) #resizes the array into correct dimensions
    
    for i in range(size):
        row = f.readline().split()  #splits each line into a list
        for j in range(len(row)):
            sites[i,j] = row[j] #fills up the numpy array with values
    
    f.close()
    return sites



def write_site_vacancy(out_file,sites):
    """Write a site vacancy matrix to a file.

    filename is a string that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """
    
    out = open(outfile_name, 'w') #creates out file
    dimensions = np.shape(sites) #finds dimensions of file
    rows = dimensions[0] #finds number of rows in file
    out.write(str(rows) + "\n") #writes the header (the number of rows)
    
    for i in range(0, rows):
        for j in range(0, rows):
            out.write(str(sites[i,j]) + " ") #writes out the numpy array
        out.write("\n")
    
    out.close()



def return_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through directed percolation
    """
    
    n = np.shape(sites)[0] #finds the dimension of sites
    flow = np.zeros(n*n) #creates a new array of zeros with same dimensions
    flow.shape = (n, n)
    
    for i in range(0,n): #runs flow_from for every index in first row
        flow_from(sites, flow, 0, i) 
    
    return flow #returns flow matrix
    

def flow_site(sites,full,i,j):
    """Adjusts the full array for flow from a single site

    This method does not return anything. It changes the array full
    Notice it is not side effect free
    """
    
    n = np.shape(sites)[0] #finds dimensions of sites
    
    if(i<0 or i>=n): #if rows out of bound, exit 
        return
    if(j<0 or j>=n): #if columns out of bound, exit
        return
    if(sites[i,j] != 1): #if the site isn't vacant, exit
        return
    if(full[i,j] != 0): #if it's already full, exit
        return
    
    full[i,j] = 1 #fill the site
    flow_from(sites, full, i+1, j) #check the site above
    flow_from(sites, full, i-1, j) #check the site below
    flow_from(sites, full, i, j+1) #check the site to the right
    flow_from(sites, full, i, j-1) #check the site to the left


def percolation(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """

    rows = np.shape(flow_matrix)[0] #number of rows/cols in flow_matrix
    last = 0
    
    for i in range(0, rows):
        last += flow_matrix[rows-1][i] #sums up the last row of 1s and 0s
    
    return not(last == 0) #if there is a vacant space in last row, returns true
    
    

def create_site_vacancy(n,p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """

    if(p<0 or p>1): #checks against negative or >100% probabilities
        return "Invalid probablity"
    
    sites = np.random.rand(n,n) #creates an nxn array of random floats

    for i in range(0, n):
        for j in range(0, n):
            if(sites[i,j]<=p):
                sites[i,j] = 1 #if random number is <= probability, vacant spot
            else:
                sites[i,j] = 0 #else, it's a blocked spot
    
    return sites



def visual_perc(sites):
    """Displays a matrix using three colors for vacant, blocked, full
    
    Used to visualize undirected flow on the matrix sites.
    """
    
    full = undirected_flow(sites) #creates the flow matrix for sites
    rows = np.shape(sites)[0]
    a = np.zeros(rows*rows) #creates an array of zeros
    a.shape = (rows,rows)
    for i in range(0, rows):
        for j in range(0, rows):
            if(full[i,j] == 1): 
               a[i,j] = 1 #if the flow is full, set a to 1
            else:
                if(sites[i,j] == 1):
                    a[i,j] = 2 #if the site is vacant, set a to 2
                else:
                    a[i,j] = 0 #if the site is blocked, set a to 0

    #creates a display with full, vacant, and blocked sites as diff colors  
    plt.matshow(a)
    plt.show()      



def graph_perc(n,trials):
    """generates and displays a graph of percolation p vs. vacancy p

    estimates percolation probability on an nxn grid for directed 
    percolation by running a Monte Carlo simulation using the variable trials number
    of trials for each point. 
    """

    p1 = np.linspace(0, .2, num = 4) #has 4 probabilities between 0 and .2
    p2 = np.linspace(.3, .8, num = 90) #has 100 probahbilities between .2 and .8
    p3 = np.linspace(.9, 1, num = 3) #has 2 probabilities between .9 and 1
    
    p = np.concatenate([p1, p2, p3]) #creates 1 array from previous 3
    probs = [] 
    i = 0
    while i < len(p):
        num_perc = 0
        two_trials = []
        for j in range(2):
            num_perc = 0
            for k in range(trials): #for the number of trials
                temp_plot = make_sites(n, p[i]) #create a site vacancy array
                temp = undirected_flow(temp_plot) #run the flow through it
                if (percolates(temp)):
                    num_perc += 1 #if it percolates, increment the total number
            two_trials.append(num_perc/float(trials)) #add to temp array
        if(m.fabs(two_trials[0] - two_trials[1]) < .01):
            #if two vacancy probabilities have < .01% diff, add to final array
            probs.append(two_trials[0]) 
            i += 1 #only increment if above is true, else run again
    
    plt.xlabel('Vacancy Probability')
    plt.ylabel('Percolation Probability')
    plt.title('Undirected Percolation')
    plt.plot(p, probs, 'r-')
    plt.show()
