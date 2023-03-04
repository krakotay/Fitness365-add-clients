import requests
from base64 import b64encode
import pandas as pd
from tabulate import tabulate
import json

def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

#Необходимо ввести данные, я их из соображений безопасности уберу
username = ""
password = ""

headers = { 'Authorization' : basic_auth(username, password) }


data = pd.read_csv('file.csv')

#Сам код

print(data.head())
i = 0
data['phone'] = data['phone'].astype(str)
while i < data.shape[0]:
    name = data['First Name'][i]
    surname =data['Last Name'][i]
    #Необходимо ввести ID фитнес-клуба
    orgId = ''
    phone = data['phone'][i]
    data2 = {'firstName' : name, 'lastName' : surname, 'organizationId' : orgId , 'phone' : phone}
    send_user = requests.post(" https://w.fitness365.ru/api/v1/client", json=data2, headers=headers)
    print(tabulate(json.loads(send_user.text)['data']['items'], headers="keys"))    
    i = i + 1
