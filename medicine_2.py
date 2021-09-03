import pandas as pd
import numpy as np
data1 = pd.read_csv("symptom_precaution.csv")
data2 = pd.read_csv("symptom_Description.csv")
desc = data2.iloc[:,1]
def searcher(symptoms):
    found=False
    index=0
    findindex=[]
    for i in item:
        for j in symptoms:
            if j.lower() in i.lower():
                found=True
            else:
                found=False
                break
        if found:
            findindex.append(index)
        index+=1
    display(findindex)

def display(findindex):
    for i in findindex:
        print(disease.iloc[i],end=": ")
        print(data2.iloc[i,1])
item=[]
for i in range(41):
    item.append(desc.iloc[i])
    disease = data2.iloc[:,0]
symptoms=[]
while True:
    x=input("Enter symptoms of ailment or 0 to exit ")
    if x=='0':
        searcher(symptoms)
        break
    else:
        symptoms.append(x)
