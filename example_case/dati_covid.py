import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dati_citta=pd.read_csv('/home/enk/Scrivania/covid.csv', usecols = ['denominazione_regione','ricoverati_con_sintomi',"terapia_intensiva","deceduti"])

print(dati_citta)
df=pd.DataFrame(dati_citta,columns=["denominazione_regione","ricoverati_con_sintomi","terapia_intensiva"]
)
df.plot(x="denominazione_regione",y=["ricoverati_con_sintomi","terapia_intensiva"],kind="bar",figsize=(9,8))
plt.show()