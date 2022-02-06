# Reading the csv file
import pandas as pd
import numpy as np
import os
import requests
from dotenv import load_dotenv
load_dotenv()
data = pd.read_csv("C:/Users/amans/Downloads/mailingList.csv")
Emails = []
Names = []
for i in range(len(data)):
    Emails.append(data.iloc[i,2])
    Names.append(data.iloc[i,1])
# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/sandbox3e39c00b2df245ef80fc8053ef1e0cd6.mailgun.org/messages",
# 		auth=("api", os.getenv("API_KEY")),
# 		data={"from": "Excited User <amananytime07@gmail.com>",
# 			"to": ["amananytime07@gmail.com"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"})
def add_mailing_list(name, email):
    Names.append(name)
    Emails.append(email)


def remove_mailing_list(name, email):
    Names.remove(name)
    Emails.remove(email)

# send_simple_message()
print(os.getenv("API_KEY"))