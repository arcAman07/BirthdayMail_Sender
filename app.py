# Reading the csv file
import pandas as pd
import numpy as np
import os
import requests
from dotenv import load_dotenv
import csv
import asyncio
load_dotenv()
data = pd.read_csv("C:/Users/amans/Downloads/mailingList.csv")
Emails = []
Names = []
currentLength = data.shape[0]
for i in range(len(data)):
    Emails.append(data.iloc[i,2])
    Names.append(data.iloc[i,1])

def send_simple_message(name,email):
    return requests.post(
		"https://api.mailgun.net/v3/sandbox3e39c00b2df245ef80fc8053ef1e0cd6.mailgun.org/messages",
		auth=("api", os.getenv("API_KEY")),
		data={"from": "Excited User <amananytime07@gmail.com>",
			"to": [email],
			"subject": "Your Birthday Wishes",
			"text": "Happy Birthday "+name+"!. Have a great day ahead!"})

def add_mailing_list(name, email):
    Names.append(name)
    Emails.append(email)
    currentLength += 1
    # Need to add data to the csv
    data['Name'].iloc[currentLength] = name
    data['Email'].iloc[currentLength] = email

def remove_mailing_list(name, email):
    Names.remove(name)
    Emails.remove(email)
    currentLength -= 1
    # Need to remove data from the csv
    # data = data.drop(data[data['Email'] == email].index)
    data = data.drop(data[data['Name'] == name].index)

def addList_mailing_list(name, email):
    for i in range(0,len(name)):
        sendName = name[i]
        sendEmail = email[i]
        Names.append(sendName)
        Emails.append(sendEmail)
        data['Name'].iloc[currentLength] = sendName
        data['Email'].iloc[currentLength] = sendEmail
        currentLength += 1
def removeList_mailing_list(name, email):
    for i in range(0,len(name)):
        sendName = name[i]
        sendEmail = email[i]
        Names.remove(sendName)
        Emails.remove(sendEmail)
        data = data.drop(data[data['Name'] == sendName].index)
        # data = data.drop(data[data['Email'] == sendEmail].index)
        currentLength -= 1
for i in range(0,len(Emails)):
    name = Names[i]
    email = Emails[i]
    send_simple_message(name,email)