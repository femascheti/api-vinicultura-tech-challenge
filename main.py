from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

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
        df = df[df['quantidade_kilo'] >= float(kg_min)]
    if kg_max:
        df = df[df['quantidade_kilo'] <= float(kg_max)]

    return df

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Rota produção ok
@app.route('/api/v1/producao', methods=['GET'])
def get_producao():
    df_producao = pd.read_csv('data/producao_ready.csv')
    df_producao = filtrar_dataframe(df_producao,
                                     ano=request.args.get('ano'),
                                     control=request.args.get('control'),
                                     litros_min=request.args.get('litros_min'),
                                     litros_max=request.args.get('litros_max'))
    producao_json = df_producao.to_json(orient='records')
    return jsonify(producao_json)

# Roda comercial ok
@app.route('/api/v1/comercial', methods=['GET'])
def get_comercial():
    df_comercial = pd.read_csv('data/comercial_ready.csv')
    df_comercial = filtrar_dataframe(df_comercial,
                                     ano=request.args.get('ano'),
                                     control=request.args.get('control'),
                                     litros_min=request.args.get('litros_min'),
                                     litros_max=request.args.get('litros_max'))
    comercial_json = df_comercial.to_json(orient='records')
    return jsonify(comercial_json)

# Rotas para importação TODO adicionar filtrar_dataframe com parametros
@app.route('/api/v1/importacao/<tipo>', methods=['GET'])
def get_importacao(tipo):
    
    if tipo not in ['espumante', 'frescas', 'passas', 'suco', 'vinho']:
        return jsonify({'error': 'Tipo de importação inválido'}), 400

    df_importacao = pd.read_csv(f'data/importacao_{tipo}_ready.csv')
    if request.args.get('dolar_min'):
        df_importacao = df_importacao[df_importacao['quantidade_dolar'] >= float(request.args.get('dolar_min'))]
    if request.args.get('dolar_max'):
        df_importacao = df_importacao[df_importacao['quantidade_dolar'] <= float(request.args.get('dolar_max'))]
    if request.args.get('kg_min'):
        df_importacao = df_importacao[df_importacao['quantidade_kilo'] >= float(request.args.get('kg_min'))]
    if request.args.get('kg_max'):
        df_importacao = df_importacao[df_importacao['quantidade_kilo'] <= float(request.args.get('kg_max'))]
    importacao_json = df_importacao.to_json(orient='records')
    if request.args.get('pais'):
        df_importacao = df_importacao[df_importacao['pais'] == pais]

    return jsonify(importacao_json)

# Rotas exportação TODO adicionar filtrar_dataframe com parametros
@app.route('/api/v1/exportacao/<tipo>', methods=['GET'])
def get_exportacao(tipo):
    if tipo not in ['vinho', 'uva', 'suco', 'espumante']:
        return jsonify({'error': 'Tipo de exportação inválido'}), 400

    df_exportacao = pd.read_csv(f'data/exportacao_{tipo}_ready.csv')
    df_exportacao = filtrar_dataframe(df_exportacao,
                                       ano=request.args.get('ano'),
                                       control=request.args.get('pais'),
                                       quantidade_min=request.args.get('kg_min'),
                                       quantidade_max=request.args.get('kg_max'))
    if request.args.get('dolar_min'):
        df_exportacao = df_exportacao[df_exportacao['quantidade_dolar'] >= float(request.args.get('dolar_min'))]
    if request.args.get('dolar_max'):
        df_exportacao = df_exportacao[df_exportacao['quantidade_dolar'] <= float(request.args.get('dolar_max'))]

    exportacao_json = df_exportacao.to_json(orient='records')
    return jsonify(exportacao_json)

# Rotas processamento TODO adicionar filtrar_dataframe com parametros
@app.route('/api/v1/processa/<tipo>', methods=['GET'])

def get_processa(tipo):
    if tipo not in ['americanas_hibridas','sem_classificacao', 'uvas_mesa', 'viniferas']:
        return jsonify({'error':'tipo de processamento inválido'}), 400

    df_processa = pd.read_csv(f'data/processa_{tipo}_ready.csv')

    df_processa = filtrar_dataframe(df_processa,
                                    ano=request.args.get('ano'),
                                    control=request.args.get('control'),
                                    quantidade_min=request.args.get('quantidade_min'),
                                    quantidade_max=request.args.get('quantidade_max'))
    if request.args.get('quantidade_min'):
        df_processa = df_processa[df_processa['quantidade_kilo'] >= float(request.args.get('quantidade_min'))]
    if request.args.get('quantidade_max'):
        df_processa = df_processa[df_processa['quantidade_kilo'] <= float(request.args.get('quantidade_max'))]
    
    export_processa_json = df_processa.to_json(orient='records')

    return jsonify(export_processa_json)

if __name__ == '__main__':
    app.run(debug=True)