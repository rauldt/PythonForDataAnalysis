# -*- coding: utf-8 -*-
"""
Author: Raul Torres Aragon
Class: Python for Data Analysis
Professor: Alex Iliev
Assigment: Final Project

"""

import numpy as np
import pandas as pd
import pylab as plb
import statsmodels.api as sm
import os


# load housing data as pandas dataframe
os.chdir("C:/Users/rtorres/desktop/Development Local/Python")
mydata = pd.read_csv('houses.csv')
print(mydata.shape) #show dimensions of dataframe
print(mydata.columns) #shows column names
print(mydata.head(5)) # print the first 5 lines


# define function to inspect some of the features
def my_summary(var, bins = 24, title = "No title", xlab = "", addspace = 0.01):
    
    # print summary statistics
    print(mydata[[var]].describe())
    
    # print a histogram to inspect distribution
    min = int(np.array(mydata[[var]].describe())[3])
    max = int(np.array(mydata[[var]].describe())[7])
    plb.figure(1)
    n, bins, patches = plb.hist(np.array(mydata[[var]]).flatten(), normed = True, bins=24, histtype = "stepfilled", color = "orange")
    plb.xlabel(xlab)
    plb.title(title)
    plb.grid(axis = "y", linestyle=':')
    plb.axis([min, max, 0.0, n.max() + addspace])
    plb.show()
    
    # print a scatterplot to inspect relationship to dependent variable
    plb.cla()
    plb.scatter(np.array(mydata[[var]]).flatten(), np.array(mydata[["price"]]).flatten())  
    plb.xlabel(xlab)
    plb.ylabel("price")
    

# ~~~~~~~~~~~~~~~~~~~~~~~ #
# inspecting key features #
# ~~~~~~~~~~~~~~~~~~~~~~~ #
    
my_summary("age", title = "Home age", xlab = "years")    
my_summary("rooms", title = "Number of rooms", xlab = "number of rooms")
my_summary("area", title = "Square footage", addspace = 0.0001, xlab = "square feet")
my_summary("baths", title = "Number of bathrooms", xlab = "number of bathrooms")
my_summary("inst", title = "Distance to Interstate", addspace = 0.00001, xlab = "yards")


# ~~~~~~~~~~~~~~ #
# OLS regression #
# ~~~~~~~~~~~~~~ #

# set apart X matrix and y vector
X = pd.DataFrame(mydata, columns=['age','rooms','area','baths','inst'])
y = pd.DataFrame(mydata, columns=['price'])

# fit linear regresion
model = sm.OLS(y, X).fit()
model.summary()


# ~~~~~~~~~~~~~~~~~ #
# residual analysis #
# ~~~~~~~~~~~~~~~~~ #

# obtain predicted y values
yhat = model.predict(X)

# construct residuals by subtracting predicted y values from actual y values
residuals = np.array(y).flatten() - np.array(yhat).flatten()

# plot residuals against y values
plb.scatter(residuals, np.array(y).flatten())
plb.xlabel("residuals")
plb.ylabel("yhat")

  




### house age
#print(mydata[["age"]].describe())
#min = int(np.array(mydata[["age"]].describe())[3])
#max = int(np.array(mydata[["age"]].describe())[7])
#plb.figure(1)
#n, bins, patches = plb.hist(np.array(mydata[["age"]]).flatten(), normed = True, bins=24, histtype = "stepfilled", color = "gray")
#plb.xlabel('Age')
#plb.title("Histogram of house age")
#plb.axis([min, max, 0.0, n.max() + .01])
#plb.show()



