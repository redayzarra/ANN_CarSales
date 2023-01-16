"""
Car Sales - Regression ANN

This project utilizes an artificial neural network to perform a regression task, 
which means the model will predict a value based on the features. In this case, 
the model will have eight features to predict the purchasing amount for each 
customer.This project showcases a step-by-step implementation of the model as 
well as in-depth notes to customize the model further for higher accuracy.

We can begin by importing some classic libraries that will help us read and 
analyze data. Pandas is a library used for data frame manipulations. NumPy is a 
package used for numerical analysis.
"""
# Importing the libraries
import pandas as pd
import numpy as np

# Data visualization and plotting
import matplotlib.pyplot as plt
import seaborn as sns


"""
Importing the dataset with the .read_csv method from Pandas to load the dataset 
and storing it in the car_data variable. However, we will need to change to 
encoding for the data file because it contains characters (such as '@') that 
Pandas can't read. We specify the ISO-8859-1 encoding for the datafile to be 
imported.
"""
car_data = pd.read_csc('Car_Purchasing_Data.csv', encoding = "ISO-8859-1") # The .read_csv method from Pandas accepts a parameter called encoding which allows us to specify that we want to use the ISO-8859-1 encoding method.

car_data.head() # The .head() method is used to show the first five rows of the dataframe.


"""

"""