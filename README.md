# percolation_tester
Finds percolation probabilities for nxn sized grids with a p% site vacancy probability.

Vivian Shen 

2 files: percolation and perc_tester.

Percolation contains functions read_grid, write_grid, make_sites, and percolates, which read a grid from a file, write a grid to a file, create a new nxn grid with p% site vacancy probability, and check if it percolates, respectively. The important functions are flow_from, undirected_flow, show_perc, and make_plot.

    flow_from takes in two arrays, one of the vacancy sites (sites) and another of zeroes (full) (initiated in undirected_flow). 
      It also takes in indices i and j. 
      This method then checks four conditions: 
        1) the row index isn’t out of bounds
        2) the column index isn’t out of bounds
        3) the site is vacant (sites[i][j] = 1) 
        4) the position in the full array hasn’t already been filled (full[i][j] = 0). 
      Then it fills that site (full[i][j] = 1) and using recursion, calls the method on 
        every adjacent position (up, down, left, and right).

    undirected_flow takes in a single site vacancy matrix. 
      It creates a new array of zeroes with the same dimensions. 
      Then, it calls the flow_from method using the site vacancy matrix
        and the flow matrix of zeroes at every index in the first row. 
      It returns the new matrix of vacant/full sites. 
      This flow can go in all directions, not just down!

    show_perc creates a matrix of 3 colors that represent vacant, blocked, and full sites. 
      It takes in a site vacancy matrix, and runs undirected flow on it, saving it to a new flow matrix. 
      Then it creates a new matrix of zeroes of the same size, and checks between the two matrices. 
      If the flow matrix has a full position, the new matrix has a 1. 
      If the flow matrix is empty, it checks the sites matrix. If the sites matrix has a vacant position, 
        the new matrix has a 2. 
      If the sites matrix has a blocked position, the new matrix has a 0. 
      Using matplotlib.pyplot.matshow on this array automatically maps a color to a number, 
        so since the array is composed of 0s, 1s and 2s, the percolation is shown with 3 colors.

    make_plot takes in a dimension n and an integer number of trials. 
      It creates its own array of probabilities, less values of p for low and high site vacancies, and more in the middle. 
      Then, for all the probability values, it runs undirected flow and checks if it percolates. 
      If it does percolates, it adds it to the total percolated value, and at the end of the number of trials 
        it finds the percolation percentage and adds that to a temporary list. 
      It does this twice, and then it checks if the percolation percentages are less than .01% difference. 
      If yes, it appends that to a final percolation probability list and goes on to the next vacancy probability. 
      If no, it does it over. 
      In the end, it creates a pyplot plot graph with the x axis being the list of vacancy probabilities, 
      the y axis being the percolation probabilities, and the title being Undirected Percolation.

perc_tester is a main method that tests all the above functions.
