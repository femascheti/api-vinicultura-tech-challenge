from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

def filtrar_dataframe(df, ano=None, control=None, quantidade_min=None, quantidade_max=None):
    """
    Função auxiliar para filtrar DataFrames de acordo com os parâmetros de consulta.

    Args:
        df (pd.DataFrame): DataFrame a ser filtrado.
        ano (int, optional): Ano para filtrar. Defaults to None.
        control (str, optional): Valor de control para filtrar. Defaults to None.
        quantidade_min (float, optional): Valor mínimo de quantidade. Defaults to None.
        quantidade_max (float, optional): Valor máximo de quantidade. Defaults to None.

    Returns:
        pd.DataFrame: DataFrame filtrado.
    """
    if ano:
        df = df[df['ano'] == int(ano)]
    if control:
        df = df[df['control'] == control]
    if quantidade_min:
        df = df[df['quantidade_litros'] >= float(quantidade_min)]
    if quantidade_max:
        df = df[df['quantidade_litros'] <= float(quantidade_max)]
    return df

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api/v1/producao', methods=['GET'])
def get_producao():
    df_producao = pd.read_csv('data/producao_ready.csv')
    df_producao = filtrar_dataframe(df_producao,
                                     ano=request.args.get('ano'),
                                     control=request.args.get('control'),
                                     quantidade_min=request.args.get('quantidade_min'),
                                     quantidade_max=request.args.get('quantidade_max'))
    producao_json = df_producao.to_json(orient='records')
    return jsonify(producao_json)


@app.route('/api/v1/comercial', methods=['GET'])
def get_comercial():
    df_comercial = pd.read_csv('data/comercial_ready.csv')
    df_comercial = filtrar_dataframe(df_comercial,
                                     ano=request.args.get('ano'),
                                     control=request.args.get('control'),
                                     quantidade_min=request.args.get('quantidade_min'),
                                     quantidade_max=request.args.get('quantidade_max'))
    comercial_json = df_comercial.to_json(orient='records')
    return jsonify(comercial_json)


# Rotas para importação
@app.route('/api/v1/importacao/<tipo>', methods=['GET'])
def get_importacao(tipo):
    """
    Endpoint para consulta de dados de importação de vinho.

    Args:
        tipo (str): Tipo de produto importado (espumantes, frescas, passas, suco, vinho).

    Returns:
        jsonify: JSON com os dados de importação filtrados.
    """
    if tipo not in ['espumante', 'frescas', 'passas', 'suco', 'vinho']:
        return jsonify({'error': 'Tipo de importação inválido'}), 400

    df_importacao = pd.read_csv(f'data/importacao_{tipo}_ready.csv')
    df_importacao = filtrar_dataframe(df_importacao,
                                      ano=request.args.get('ano'),
                                      control=request.args.get('pais'),
                                      quantidade_min=request.args.get('kg_min'),
                                      quantidade_max=request.args.get('kg_max'))
    if request.args.get('dolar_min'):
        df_importacao = df_importacao[df_importacao['quantidade_dolar'] >= float(request.args.get('dolar_min'))]
    if request.args.get('dolar_max'):
        df_importacao = df_importacao[df_importacao['quantidade_dolar'] <= float(request.args.get('dolar_max'))]

    importacao_json = df_importacao.to_json(orient='records')
    return jsonify(importacao_json)

@app.route('/api/v1/exportacao/vinho', methods=['GET'])
def get_exp_vinho():
    df_exp_vinho = pd.read_csv('data/exportacao_vinho_ready.csv')

    ano = request.args.get('ano')
    pais = request.args.get('pais')
    dolar_min = request.args.get('dolar_min')
    dolar_max = request.args.get('dolar_max')
    kg_min = request.args.get('kg_min')
    kg_max = request.args.get('kg_max')

    if ano:
        df_exp_vinho = df_exp_vinho[df_exp_vinho['ano'] == int(ano)]
    if pais:
        df_exp_vinho = df_exp_vinho[df_exp_vinho['pais'] == pais]
    if dolar_min:
        df_exp_vinho = df_exp_vinho[df_exp_vinho['quantidade_dolar'] >= float(dolar_min)]
    if dolar_max:
        df_exp_vinho = df_exp_vinho[df_exp_vinho['quantidade_dolar'] <= float(dolar_max)]
    if kg_min:
        df_exp_vinho = df_exp_vinho[df_exp_vinho['quantidade_kg'] >= float(kg_min)]
    if kg_max:
        df_exp_vinho = df_exp_vinho[df_exp_vinho['quantidade_kg'] <= float(kg_max)]

    export_vinho_json = df_exp_vinho.to_json(orient='records')
    
    return jsonify(export_vinho_json)

@app.route('/api/v1/exportacao/uva', methods=['GET'])
def get_exp_uva():
    df_exp_uva = pd.read_csv('data/exportacao_uva_ready.csv')

    ano = request.args.get('ano')
    pais = request.args.get('pais')
    dolar_min = request.args.get('dolar_min')
    dolar_max = request.args.get('dolar_max')
    kg_min = request.args.get('kg_min')
    kg_max = request.args.get('kg_max')

    if ano:
        df_exp_uva = df_exp_uva[df_exp_uva['ano'] == int(ano)]
    if pais:
        df_exp_uva = df_exp_uva[df_exp_uva['pais'] == pais]
    if dolar_min:
        df_exp_uva = df_exp_uva[df_exp_uva['quantidade_dolar'] >= float(dolar_min)]
    if dolar_max:
        df_exp_uva = df_exp_uva[df_exp_uva['quantidade_dolar'] <= float(dolar_max)]
    if kg_min:
        df_exp_uva = df_exp_uva[df_exp_uva['quantidade_kg'] >= float(kg_min)]
    if kg_max:
        df_exp_uva = df_exp_uva[df_exp_uva['quantidade_kg'] <= float(kg_max)]

    export_uva_json = df_exp_uva.to_json(orient='records')
    
    return jsonify(export_uva_json)

@app.route('/api/v1/exportacao/suco', methods=['GET'])
def get_exp_suco():
    df_exp_suco = pd.read_csv('data/exportacao_suco_ready.csv')

    ano = request.args.get('ano')
    pais = request.args.get('pais')
    dolar_min = request.args.get('dolar_min')
    dolar_max = request.args.get('dolar_max')
    kg_min = request.args.get('kg_min')
    kg_max = request.args.get('kg_max')

    if ano:
        df_exp_suco = df_exp_suco[df_exp_suco['ano'] == int(ano)]
    if pais:
        df_exp_suco = df_exp_suco[df_exp_suco['pais'] == pais]
    if dolar_min:
        df_exp_suco = df_exp_suco[df_exp_suco['quantidade_dolar'] >= float(dolar_min)]
    if dolar_max:
        df_exp_suco = df_exp_suco[df_exp_suco['quantidade_dolar'] <= float(dolar_max)]
    if kg_min:
        df_exp_suco = df_exp_suco[df_exp_suco['quantidade_kg'] >= float(kg_min)]
    if kg_max:
        df_exp_suco = df_exp_suco[df_exp_suco['quantidade_kg'] <= float(kg_max)]

    export_suco_json = df_exp_suco.to_json(orient='records')
    
    return jsonify(export_suco_json)

@app.route('/api/v1/exportacao/espumante', methods=['GET'])
def get_exp_espumante():
    df_exp_espumante = pd.read_csv('data/exportacao_espumante_ready.csv')

    ano = request.args.get('ano')
    pais = request.args.get('pais')
    dolar_min = request.args.get('dolar_min')
    dolar_max = request.args.get('dolar_max')
    kg_min = request.args.get('kg_min')
    kg_max = request.args.get('kg_max')

    if ano:
        df_exp_espumante = df_exp_espumante[df_exp_espumante['ano'] == int(ano)]
    if pais:
        df_exp_espumante = df_exp_espumante[df_exp_espumante['pais'] == pais]
    if dolar_min:
        df_exp_espumante = df_exp_espumante[df_exp_espumante['quantidade_dolar'] >= float(dolar_min)]
    if dolar_max:
        df_exp_espumante = df_exp_espumante[df_exp_espumante['quantidade_dolar'] <= float(dolar_max)]
    if kg_min:
        df_exp_espumante = df_exp_espumante[df_exp_espumante['quantidade_kg'] >= float(kg_min)]
    if kg_max:
        df_exp_espumante = df_exp_espumante[df_exp_espumante['quantidade_kg'] <= float(kg_max)]

    export_espumante_json = df_exp_espumante.to_json(orient='records')
    
    return jsonify(export_espumante_json)

@app.route('/api/v1/processa/americanas_hibridas', methods=['GET'])
def get_americanas_hibridas():
    df_americanas_hibridas = pd.read_csv('data/processa_americanas_hibridas_ready.csv')

    ano = request.args.get('ano')
    control = request.args.get('control')
    quantidade_min = request.args.get('quantidade_min')
    quantidade_max = request.args.get('quantidade_max')

    if ano:
        df_americanas_hibridas = df_americanas_hibridas[df_americanas_hibridas['ano'] == int(ano)]
    if control:
        df_americanas_hibridas = df_americanas_hibridas[df_americanas_hibridas['control'] == control]
    if quantidade_min:
        df_americanas_hibridas = df_americanas_hibridas[df_americanas_hibridas['quantidade_kilos'] >= float(quantidade_min)]
    if quantidade_max:
        df_americanas_hibridas = df_americanas_hibridas[df_americanas_hibridas['quantidade_kilos'] <= float(quantidade_max)]

    export_am_hib_json = df_americanas_hibridas.to_json(orient='records')
    
    return jsonify(export_am_hib_json)

@app.route('/api/v1/processa/uvas_mesa', methods=['GET'])
def get_uvas_mesa():
    df_uvas_mesa = pd.read_csv('data/processa_uvas_mesa_ready.csv')

    ano = request.args.get('ano')
    control = request.args.get('control')
    quantidade_min = request.args.get('quantidade_min')
    quantidade_max = request.args.get('quantidade_max')

    if ano:
        df_uvas_mesa = df_uvas_mesa[df_uvas_mesa['ano'] == int(ano)]
    if control:
        df_uvas_mesa = df_uvas_mesa[df_uvas_mesa['control'] == control]
    if quantidade_min:
        df_uvas_mesa = df_uvas_mesa[df_uvas_mesa['quantidade_kilos'] >= float(quantidade_min)]
    if quantidade_max:
        df_uvas_mesa = df_uvas_mesa[df_uvas_mesa['quantidade_kilos'] <= float(quantidade_max)]

    export_uvas_mesa_json = df_uvas_mesa.to_json(orient='records')
    
    return jsonify(export_uvas_mesa_json)

@app.route('/api/v1/processa/viniferas', methods=['GET'])
def get_viniferas():
    df_viniferas = pd.read_csv('data/processa_viniferas_ready.csv')

    ano = request.args.get('ano')
    control = request.args.get('control')
    quantidade_min = request.args.get('quantidade_min')
    quantidade_max = request.args.get('quantidade_max')

    if ano:
        df_viniferas = df_viniferas[df_viniferas['ano'] == int(ano)]
    if control:
        df_viniferas = df_viniferas[df_viniferas['control'] == control]
    if quantidade_min:
        df_viniferas = df_viniferas[df_viniferas['quantidade_kilos'] >= float(quantidade_min)]
    if quantidade_max:
        df_viniferas = df_viniferas[df_viniferas['quantidade_kilos'] <= float(quantidade_max)]

    export_viniferas_json = df_viniferas.to_json(orient='records')

    return jsonify(export_viniferas_json)


@app.route('/api/v1/processa/sem_classificacao', methods=['GET'])
def get_sem_classificacao():
    df_sem_classificacao = pd.read_csv('data/processa_sem_classificacao_ready.csv')

    ano = request.args.get('ano')
    control = request.args.get('control')
    quantidade_min = request.args.get('quantidade_min')
    quantidade_max = request.args.get('quantidade_max')

    if ano:
        df_sem_classificacao = df_sem_classificacao[df_sem_classificacao['ano'] == int(ano)]
    if control:
        df_sem_classificacao = df_sem_classificacao[df_sem_classificacao['control'] == control]
    if quantidade_min:
        df_sem_classificacao = df_sem_classificacao[df_sem_classificacao['quantidade_kilos'] >= float(quantidade_min)]
    if quantidade_max:
        df_sem_classificacao = df_sem_classificacao[df_sem_classificacao['quantidade_kilos'] <= float(quantidade_max)]

    export_sem_classificacao_json = df_sem_classificacao.to_json(orient='records')
    return jsonify(export_sem_classificacao_json)



if __name__ == '__main__':
    app.run(debug=True)