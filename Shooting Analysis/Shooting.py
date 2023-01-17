import pandas as pd 
import csv 
import requests 
from matplotlib import pyplot as plt
import excel  
import os 
from sklearn import linear_model

os.chdir("C:\\Users\\Uncle Namo\\Desktop\\Python")
print(os.getcwd())

path_to_file = "C:\\Users\\Uncle Namo\\Desktop\\Python\\History_of_Mass_Shootings_in_the_USA.csv"
Shooting_Data = pd.read_csv(path_to_file)


#Columns available 
#print(Shooting_Data.columns)


num_deaths = Shooting_Data.sort_values(['Dead'])
print(num_deaths)
#Filtering the Date Column
Year_2022 = Shooting_Data.loc[Shooting_Data['Date'].str.contains("2022")]
print(Year_2022)

#Modifiying the Datset into a new CSV 
Shooting_Data.to_csv ('modified.csv')


#Adding a years column 
Shooting_Data['Years'] = Shooting_Data['Date'].str[0:4]
#print(Shooting_Data.head())



#Add titles and axis names 
plt.title("Deaths from School Shootings 1924-2022 ", fontsize = 20)
plt.ylabel("States", fontsize = 20)
plt.xlabel("Deaths", fontsize = 20)
plt.yticks(fontsize = 12)

#Finding the mean number of deaths per state 
Deaths_Mean = Shooting_Data.groupby('State').Dead.mean().reset_index()
print(Deaths_Mean)




#Regression Model (Most likely not gonna work because we can't convert stastes into str dumbass)
regr = linear_model.LinearRegression()




#Vertical Barts 
plt.barh(Shooting_Data['State'],Shooting_Data['Dead'], color = ["red"])
plt.tight_layout()
plt.legend(["Deaths","Year"])
plt.show()

