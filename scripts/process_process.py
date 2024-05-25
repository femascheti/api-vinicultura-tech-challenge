from tools import download_csv, normalize_dataframe
import os
import pandas as pd

def process_csv(csv_path):
    df = pd.read_csv(csv_path, sep='\t')

    # Normaliza o dataframe
    replace_dict = {
        'ti_':'tintas_',
        ' ':'_',
        'br_':'brancaserosadas_',
        '\(':'_', 
        '\"':'',
        '\)': '',
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
    df = df.drop(columns=['id', 'cultivar'])

    # Pivota tabelas
    df_melted = df.melt(id_vars='control', var_name='ano', value_name='quantidade_kilo')

    replace_dict2 = {'__':'_','\"':'',}
    df_melted = normalize_dataframe(df_melted, replace_dict2)

    return df_melted

def main():
    urls = {
        'processa_viniferas': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv',
        'processa_americanas_hibridas': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv',
        'processa_uvas_mesa': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv',
        'processa_sem_classificacao': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv'
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
