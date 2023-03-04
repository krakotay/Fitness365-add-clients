import requests
from base64 import b64encode
import json
import pandas as pd

def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

username = ""
password = ""

headers = { 'Authorization' : basic_auth(username, password) }


data = pd.read_csv('file1.csv')

#Сам код

print(data.head())
i = 0
data['phone'] = data['phone'].astype(str)
while i < data.shape[0] - 1:
    name = data['Last Name'][i]
    surname =data['First Name'][i]
    orgId = ''
    phone = data['phone'][i]
    data2 = {'firstName' : name, 'lastName' : surname, 'organizationId' : orgId , 'phone' : phone}
    send_user = requests.post(" https://w.fitness365.ru/api/v1/client", json=data2, headers=headers)
    print(send_user.text)
    i = i + 1