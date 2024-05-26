from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth
import pandas as pd

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

basic_auth = BasicAuth(app)

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

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

# Rota produção
@app.route('/api/v1/producao', methods=['GET'])
@basic_auth.required
def get_producao():
    df_producao = pd.read_csv('data/producao_ready.csv')
    df_producao = filtrar_dataframe(df_producao,
                                     ano=request.args.get('ano'),
                                     control=request.args.get('control'),
                                     litros_min=request.args.get('litros_min'),
                                     litros_max=request.args.get('litros_max'))
    producao_json = df_producao.to_json(orient='records')
    
    return jsonify(producao_json)

# Roda comercial
@app.route('/api/v1/comercial', methods=['GET'])
@basic_auth.required
def get_comercial():
    df_comercial = pd.read_csv('data/comercial_ready.csv')
    df_comercial = filtrar_dataframe(df_comercial,
                                     ano=request.args.get('ano'),
                                     control=request.args.get('control'),
                                     litros_min=request.args.get('litros_min'),
                                     litros_max=request.args.get('litros_max'))
    comercial_json = df_comercial.to_json(orient='records')
    
    return jsonify(comercial_json)

# Rotas para importação
@app.route('/api/v1/importacao/<tipo>', methods=['GET'])
@basic_auth.required
def get_importacao(tipo):
    
    if tipo not in ['espumante', 'frescas', 'passas', 'suco', 'vinho']:
        return jsonify({'error': 'Tipo de importação inválido'}), 400

    df_importacao = pd.read_csv(f'data/importacao_{tipo}_ready.csv')
    df_importacao = filtrar_dataframe(df_importacao,
                                      ano=request.args.get('ano'),
                                      pais=request.args.get('pais'),
                                      dolar_max=request.args.get('dolar_max'),
                                      dolar_min=request.args.get('dolar_min'),
                                      kg_max=request.args.get('kg_max'),
                                      kg_min=request.args.get('kg_min'),
                                      )
    importacao_json = df_importacao.to_json(orient='records')
    
    return jsonify(importacao_json)

# Rotas para exportação
@app.route('/api/v1/exportacao/<tipo>', methods=['GET'])
@basic_auth.required
def get_exportacao(tipo):
    
    if tipo not in ['espumante', 'suco', 'uva', 'vinho']:
        return jsonify({'error': 'Tipo de exportação inválido'}), 400

    df_exportacao = pd.read_csv(f'data/exportacao_{tipo}_ready.csv')
    df_exportacao = filtrar_dataframe(df_exportacao,
                                      ano=request.args.get('ano'),
                                      pais=request.args.get('pais'),
                                      dolar_max=request.args.get('dolar_max'),
                                      dolar_min=request.args.get('dolar_min'),
                                      kg_max=request.args.get('kg_max'),
                                      kg_min=request.args.get('kg_min'),
                                      )
    exportacao_json = df_exportacao.to_json(orient='records')
    
    return jsonify(exportacao_json)

# Rotas processamento
@app.route('/api/v1/processa/<tipo>', methods=['GET'])
@basic_auth.required
def get_processa(tipo):
    if tipo not in ['americanas_hibridas','sem_classificacao', 'uvas_mesa', 'viniferas']:
        return jsonify({'error':'tipo de processamento inválido'}), 400

    df_processa = pd.read_csv(f'data/processa_{tipo}_ready.csv')

    df_processa = filtrar_dataframe(df_processa,
                                    ano=request.args.get('ano'),
                                    control=request.args.get('control'),
                                    kg_min=request.args.get('kg_min'),
                                    kg_max=request.args.get('kg_max'))
   
    processa_json = df_processa.to_json(orient='records')

    return jsonify(processa_json)

if __name__ == '__main__':
    app.run(debug=True)