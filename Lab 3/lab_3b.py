import math 
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from sympy import *
np.random.seed()

def AcceptReject(a, b):
    while True:
        u = random.uniform(0, a)
        y = random.uniform(0, b)

        # Check range from [0, 1]
        if u <= 1:
            fxu = 0.5 * u
        # Check range from [1, 4]
        elif u <= 4:  
            fxu = (4 - u) / 6
        if y <= fxu:
            z = u
            break
    return z
        

def PartB():
    # Variables for Part B
    trials = 10000
    a = 4
    b = 0.6

    # Limits of the graph
    yLim = b  # Limit of y-axis
    plt.ylim(0, yLim)  # Set y-axis range for plot
    xLim = a + 1   # Limit of x-axis
    plt.xlim(0, xLim)  # Set x-axis range for plot

    # Get points to draw the triangle
    triangle = []
    for x in range(0, xLim):
        if x <= 1: y = 0.5 * x
        else: y = (4 - x) / 6
        # Add the points to the triangle data
        triangle.append(y)
    
    # Using random variable X, get the pdf
    data = []
    for x in range(trials):
        data.append(AcceptReject(a, b))

    bins = np.arange(0, 500, 0.15)
    plt.hist(data, bins=bins, density=True, alpha = 0.75)
    plt.plot(triangle)
    plt.show()
        
PartB()