import pandas as pd 
import csv 
import requests 
from matplotlib import pyplot as plt
import excel  
import os 

#Chaning Directory
os.chdir("C:\\Users\\Uncle Namo\\Desktop\\Python")
print(os.getcwd())


path_to_file = "C:\\Users\\Uncle Namo\\Desktop\\Python\\pokemon.csv"
pokemon_file = pd.read_csv(path_to_file)
print(pokemon_file.head(13))

#Read Headers(Name,Type 1 ,Type 2, Hp, and etc)
print(pokemon_file.columns)


#Calling Data In our dataset 
print(pokemon_file['Name'][0:13])
print(pokemon_file['HP'][0:13])



#Establishing Bar Graph 
Starters = pokemon_file['Name'][0:13]
HP = (pokemon_file['HP'][0:13])

#Establishing Bar Labels 
ax = plt.subplot()
ax.set_xticks(range(len(Starters)))
ax.set_xticklabels(["Bulbasaur","Ivysaur","Venusaur","VenusaurMega Venusaur","Charmander","Charmeleon","Charizard","CharizardMega Charizard X","CharizardMega Charizard Y","Squirtle","Wartortle","Blastoise","BlastoiseMega Blastoise"],rotation = 60, fontsize = 7.5)




plt.bar(range(len(Starters)),HP)
plt.bar(range(len(Starters)),pokemon_file['Attack'][0:13],bottom = HP)
plt.bar(range(len(Starters)),pokemon_file['Defense'][0:13],bottom = HP)
plt.legend(["HP","Attack","Defense"])

plt.show()