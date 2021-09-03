import pandas as pd
import numpy as np
data1 = pd.read_csv("symptom_precaution.csv")
data2 = pd.read_csv("symptom_Description.csv")
print(data1.head())
print(data2.head())
print(data1.shape)
print(data2.shape)
disease = data2.iloc[0,0]
print(disease)