import pandas as pd 
import csv 
import requests 
from matplotlib import pyplot as plt 
import excel 
import os 
import numpy as np 
from sklearn import linear_model

print(os.getcwd())
path_to_file = "C:\\Users\\Uncle Namo\\Desktop\\Python\\StudyingHours\\score.csv"
studying_file = pd.read_csv(path_to_file)
print(studying_file)

#printing headers 
print(studying_file.columns)


mean_hours = studying_file.groupby('Hours').Scores.mean().reset_index()
print(mean_hours)

X = mean_hours['Hours']
X = X.values.reshape(-1,1)
Y = mean_hours["Scores"]

#Regression Model 
regr = linear_model.LinearRegression()
regr.fit(X,Y)
print(regr.coef_)
print(regr.intercept_)

#Regression Line 
y_predict = regr.predict(X)
print(y_predict)


#Titles and Names 
plt.title("Correlation of Number of Hours Studied and Predicted Score", fontsize = 15)
plt.ylabel("Score", fontsize = 10)
plt.xlabel("Hours", fontsize = 10)


#Plotting 
plt.scatter(X,Y)
plt.plot(X,y_predict, color = 'green', linestyle= '--')
plt.show()