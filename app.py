from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_basicauth import BasicAuth
from scripts.utils import filtrar_dataframe
import pandas as pd
import os

load_dotenv(os.path.join(os.path.dirname(__file__), 'config', '.env'))

load_dotenv()
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

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
                                     litros_max=request.args.get('litros_max')
                                     )
    producao_json = df_producao.to_json(orient='records')
    
    return jsonify(producao_json)

# Rota comercial
@app.route('/api/v1/comercial', methods=['GET'])
@basic_auth.required
def get_comercial():
    df_comercial = pd.read_csv('data/comercial_ready.csv')
    df_comercial = filtrar_dataframe(df_comercial,
                                     ano=request.args.get('ano'),
                                     control=request.args.get('control'),
                                     litros_min=request.args.get('litros_min'),
                                     litros_max=request.args.get('litros_max')
                                     )
    comercial_json = df_comercial.to_json(orient='records')
    
    return jsonify(comercial_json)

# Rota para importação
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

# Rota para exportação
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

# Rota processamento
@app.route('/api/v1/processa/<tipo>', methods=['GET',])
@basic_auth.required
def get_processa(tipo):
    if tipo not in ['americanas_hibridas','sem_classificacao', 'uvas_mesa', 'viniferas']:
        return jsonify({'error':'tipo de processamento inválido'}), 400

    df_processa = pd.read_csv(f'data/processa_{tipo}_ready.csv')

    df_processa = filtrar_dataframe(df_processa,
                                    ano=request.args.get('ano'),
                                    control=request.args.get('control'),
                                    kg_min=request.args.get('kg_min'),
                                    kg_max=request.args.get('kg_max')
                                    )
   
    processa_json = df_processa.to_json(orient='records')

    return jsonify(processa_json)

if __name__ == '__main__':
    app.run(debug=True)