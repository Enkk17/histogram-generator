import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read file csv and take in input specific columns
data_city=pd.read_csv('directory / of / file.csv', usecols = ['enter_column_name',enter_column_name2])

#check data
#print(data)

#create a table
df=pd.DataFrame(data,columns=["enter_column_name",enter_column_name2"]
)
df.plot(x="Name_under_bar",y=["enter_column_name","enter_column_name2"],kind="bar",figsize=(9,8))
plt.show()
