import os
import requests
import pandas as pd
from unicodedata import normalize

def download_csv(url, save_dir, save_name):
    os.makedirs(save_dir, exist_ok=True)
    csv_path = os.path.join(save_dir, save_name)
    response = requests.get(url)
    
    if os.path.exists(csv_path):
        os.remove(csv_path)
        print(f'Arquivo existente {csv_path} removido.')

    if response.status_code == 200:
        with open(csv_path, 'wb') as file:
            file.write(response.content)
        print(f'Arquivo salvo em: {csv_path}')
    else:
        print(f'Erro. Status code: {response.status_code}')
    
    return csv_path

def normalize_dataframe(df, replace_dict):
    df = df.apply(lambda x: x.astype(str).str.lower())
    df.columns = map(str.lower, df.columns)
    df = df.replace(to_replace=replace_dict, regex=True)
    return df

def remover_acentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')