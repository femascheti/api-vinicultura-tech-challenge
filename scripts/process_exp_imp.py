from scripts.utils import download_csv, normalize_dataframe, remover_acentos
import os
import pandas as pd

def process_csv(csv_path):
    df = pd.read_csv(csv_path, sep=';')

    # Normaliza o dataframe
    replace_dict = {
        '\(':'_', 
        "\)": '', 
        ' ':'_', 
        '\"':'', 
        '-':'_', 
        ',':'_', 
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

    # Separa colunas
    df_kilo_anos = df.iloc[:, 2::2] # anos com valores de kilo 
    df_dolar_anos = df.iloc[:, 3::2] # anos com valores de dolar
    df_paises = df.iloc[:, 1:2] # países

    # Junta colunas de países com valores de anos 
    df_kg_pais = df_paises.join(df_kilo_anos) # kilo
    df_dolar_pais = df_paises.join(df_dolar_anos) # dolar

    # Pivota tabelas
    df_melted = df_kg_pais.melt(id_vars='país', var_name='ano', value_name='quantidade_kg')
    df_melted_dolar = df_dolar_pais.melt(id_vars='país', var_name='ano', value_name='quantidade_dolar')

    # Transforma valores de ano para inteiro
    df_melted_dolar['ano'] = df_melted_dolar['ano'].str[:4].astype('int32')
    df_melted['ano'] = df_melted['ano'].astype('int32')

    # Junta as duas tabelas
    df_final = df_melted.merge(df_melted_dolar)

    # Normalize sem acentos
    df_final = df_final.rename(columns={'país':'pais'})
    df_final['pais'] = df_final['pais'].apply(remover_acentos)

    replace_dict2 = {'__':'_','\"':'',}
    df_final = normalize_dataframe(df_final, replace_dict2)
    
    return df_final

def main():
    urls = {
        'importacao_vinho': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv',
        'importacao_espumante': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv',
        'importacao_frescas': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv',
        'importacao_passas': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv',
        'importacao_suco': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv',
        'exportacao_vinho': 'http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv',
        'exportacao_espumante': 'http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv',
        'exportacao_uva': 'http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv',
        'exportacao_suco': 'http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv'
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
