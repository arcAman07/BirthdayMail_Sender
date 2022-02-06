# Reading the csv file
import pandas as pd
import numpy as np
data = pd.read_csv("C:/Users/amans/Downloads/mailingList.csv")
Emails = []
Names = []
for i in range(len(data)):
    Emails.append(data.iloc[i,2])
    Names.append(data.iloc[i,1])
