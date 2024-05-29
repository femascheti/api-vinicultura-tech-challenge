from unicodedata import normalize
from flask import Flask, jsonify, request
import os
import requests
import pandas as pd

def filtrar_dataframe(df, ano=None, control=None, pais=None, dolar_min=None, dolar_max=None, kg_min=None, kg_max=None, litros_max=None, litros_min=None):
    ano = request.args.get('ano')
    pais = request.args.get('pais')
    dolar_min = request.args.get('dolar_min')
    dolar_max = request.args.get('dolar_max')
    kg_min = request.args.get('kg_min')
    kg_max = request.args.get('kg_max')
    control = request.args.get('control')
    litros_max = request.args.get('litros_max')
    litros_min = request.args.get('litros_min')

    if ano:
        df = df[df['ano'] == int(ano)]
    if control:
        df = df[df['control'] == control]
    if pais:
        df = df[df['pais'] == pais]
    if litros_min:
        df = df[df['quantidade_litros'] >= float(litros_min)]
    if litros_max:
        df = df[df['quantidade_litros'] <= float(litros_max)]
    if dolar_min:
        df = df[df['quantidade_dolar'] >= float(dolar_min)]
    if dolar_max:
        df = df[df['quantidade_dolar'] <= float(dolar_max)]
    if kg_min:
        df = df[df['quantidade_kg'] >= float(kg_min)]
    if kg_max:
        df = df[df['quantidade_kg'] <= float(kg_max)]

    return df

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