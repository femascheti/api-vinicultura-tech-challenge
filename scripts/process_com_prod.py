from scripts.utils import download_csv, normalize_dataframe, remover_acentos
from unicodedata import normalize
import os
import pandas as pd


def process_csv(csv_path):
    df = pd.read_csv(csv_path, sep=';')

    # Normaliza o dataframe
    replace_dict = {
        'vm_': 'vinho_mesa_', 
        've_': 'vinho_especial_', 
        'su_': '', 
        'ou_': 'outros_', 
        'es_':'',
        '_de_':'_',
        'espumantes_':'espumantes_',
        '\(':'_', 
        "\)": '', 
        ' ':'_',
        '\"':'', 
        '-':'_',
        ',':'_',
        'vv_':'vinho_viniferas_',
        '__': '_', 
        'de_':'derivados_',
        'à':'a',
        'á':'a',
        'ç':'c',
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u',
        'ã':'a',
        'õ':'o'
    }
    df = normalize_dataframe(df, replace_dict)
    df = df.drop(columns=['id', 'produto'])
    
    # Pivota tabelas
    df_melted = df.melt(id_vars='control', var_name='ano', value_name='quantidade_litros')
    
    df_melted['control'] = df_melted['control'].apply(remover_acentos)

    return df_melted

def main():
    urls = {
        'comercial': 'http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv',
        'producao': 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'
    }

    save_dir = 'data'
    
    for name, url in urls.items():
        csv_name = f'{name}_down.csv'
        csv_path = download_csv(url, save_dir, csv_name)
        df_tosave = process_csv(csv_path)
        
        filepath_output = os.path.join(save_dir, f'{name}_ready.csv')
        df_tosave.to_csv(filepath_output, index=False)
        print(f'Processed data saved for {name} in: {filepath_output}')

if __name__ == "__main__":
    main()