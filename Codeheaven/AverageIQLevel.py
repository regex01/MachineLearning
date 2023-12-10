import pandas as pd
import numpy as np
import sklearn as sk
import seaborn as sns
import matplotlib.pyplot as plt 


df = pd.read_csv(r'C:\Users\aciftcioglu\Downloads\AI\datasets\IQ_level.csv')

#print(df.head())
#print(df.tail())
#print(df.describe())
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#print(df['country'].unique())
#print(df['country'].duplicated)
#print('Average IQ level of the world is: ', df['IQ'].mean())
#world avg iq level is 85.97 
#print(df.isnull())
#sns.heatmap(df.isnull())
#plt.show()

#visuaulization
#sns.pairplot(df)
#plt.show()

#note: df.corr() functon for corrolation matrix is only works for numeric values

#correlation matrix
#correlation_matrix = df.select_dtypes(include =[np.number]).corr()

#visualization of correlation matrix
#sns.heatmap(correlation_matrix, annot = True, cmap='coolwarm')
#plt.title('Correlation Matrix')
#plt.show()
#print(df.corr())










