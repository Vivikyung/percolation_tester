# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:43:52 2015

@author: Vivian Shen
percolation tester
"""

import percolation as perc

def main():
    A=perc.make_sites(20,0.6)
    perc.write_grid('sites.txt',A)
    
    B=perc.read_grid('sites.txt')
    
    C=perc.undirected_flow(B)

    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')

    
    #visualize flow
    perc.show_perc(B)

    #generate percolation probability graph
    perc.make_plot(10, 5000)


main()
