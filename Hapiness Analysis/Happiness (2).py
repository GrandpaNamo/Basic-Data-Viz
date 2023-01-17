import pandas as pd  
import csv 
import requests
from matplotlib import pyplot as plt 
import excel


path_to_file = "C:\\Users\\Uncle Namo\\Downloads\\happiness.csv"
happiness_data = pd.read_csv(path_to_file)


#Print the first 5 columns  
print(happiness_data.head())

#Print the dimensions 
print(happiness_data.shape) 

#Print the data types 
print(happiness_data.dtypes)


#Plot Line Graph 
plt.bar(happiness_data['Mean'],happiness_data['N='])
plt.show()