import pickle

# Carregue o arquivo pickle
with open('modelo_xgboost.pickle', 'rb') as f:
    data = pickle.load(f)

# colocando o modelo na variável modelo
modelo = data['modelo']
# colocando as colunas utilizadas na variável colunas_utilizadas
colunas_utilizadas = data['colunas']

# Exemplo de predição com os modelos
# X_test precisa existir e ser um dataframe com as colunas corretas.
# predição da classe alvo: 0 ou 1
y_pred = modelo.predict(X_test)
# predição da probabilidade de cada classe: exemplo: [0.1, 0.9]
y_proba = modelo.predict_proba(X_test)
