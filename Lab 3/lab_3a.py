"""
Lexzander Saplan - 014177252
David Ibarra - 
EE 381 - Sam Jalali
Lab Project 3
"""
import math 
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# from sympy import *
np.random.seed()

""" 
Part A
Generate exponentially distributeed random variable X
with the mean of lambda = 3 from the continuous and uniformly
distributed random variable, U is an element in range [0, 1]
"""
# Number of trials
trials = 10000
# Lambda
mean = 1/3
# Data to store all the simRV
data = []
# Transform method for simRV
for x in range(trials):
    u = random.uniform(0, 1)
    simRV = -(1 / mean) * np.log(u)
    data.append(simRV)

# Plots the line using points found
curve = []  # Stores all points
yLim = mean  # Limit of y-axis
plt.ylim(0, yLim)  # Set y-axis range for plot
xLim = 15    # Limit of x-axis
plt.xlim(0, xLim)  # Set x-axis range for plot

# Loop for the range of the x-axis (graph gets smaller)
for x in range(0, xLim):
    # expRV is derivative of simRV (I think...?)
    expRV = mean * np.power(math.e, -mean * x)
    # Add the point to the curve
    curve.append(expRV)

# Specify the range for the bins
bins = np.arange(0, 500, 0.25)
# Plot the histograms
plt.hist(data, bins=bins, density=True, alpha = 0.75)
# Plot the curve consisting of expRV
plt.plot(curve)
plt.show()