import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('C:/Users/elkha/OneDrive/Desktop/DSM_project/CleanData.csv')

e=data[['budget','revenue']]
ds=e.head(100)
sns.lineplot(data=ds,x='budget',y='revenue',linewidth=3,color='crimson',marker='o')

plt.show()