import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read file csv and take in input specific columns
dati_citta=pd.read_csv('directory / of / file.csv', usecols = ['denominazione_regione','ricoverati_con_sintomi',"terapia_intensiva","deceduti"])

#check data
#print(dati_citta)

#create a table
df=pd.DataFrame(dati_citta,columns=["denominazione_regione","ricoverati_con_sintomi","terapia_intensiva"]
)
df.plot(x="denominazione_regione",y=["ricoverati_con_sintomi","terapia_intensiva"],kind="bar",figsize=(9,8))
plt.show()
