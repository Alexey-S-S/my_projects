import pandas as pd
import numpy as np
import json

df_url = 'C:\\Users\\Алексей Савелов\\student\\practikum\\pet\\df.csv'

# обработка json
def purch(name):
    df = pd.read_csv(df_url, sep='\t')
    
    file_name = name
    with open(file_name, 'r', encoding='utf-8') as f:
        x = json.load(f)
    
    purch = pd.json_normalize(x, record_path =['items'])
    purch['check'] = x['requestNumber']
    purch['date'] = x['localDateTime'].replace('T', ' ')
    purch['date'] = pd.to_datetime(purch['date'])
    purch['shop'] = x['user']
    purch['price'] = purch['price']/100
    purch['sum'] = purch['sum']/100
    purch.reset_index(drop=True)
    df = pd.concat([df, purch], axis=0)
    df.reset_index()
    df.to_csv('df.csv', sep='\t', index=False)

    # обработка приветствия
def hello():
    h = ['Dzien dobry', 'Гамарджоба', 'Hello', 'Hola', 
         'Aloha',  'Здравствуйте','Shalom', 'Привет', 'Buenas dias', 'Guten Tag', 'Здраво', 'Namaste']
    i = np.random.randint(0,12)
    return h[i]