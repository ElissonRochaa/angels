import os
import pickle
import numpy as np
import pandas as pd
import re


class Model:

    def __init__(self, dados):
        self.load_models()
        self.dados = dados
        
    def load_models(self):
        with open("AdaBoost_basic.pkl", "rb") as f:
            results = pickle.load(f)
            self.basic_model = results['model']
            self.basic_columns = results['columns']
            print("model basico carregado com sucesso")

        with open("Random_complementary.pkl", "rb") as f:
            results = pickle.load(f)
            self.complementary_model = results['model']
            self.comp_columns = results['columns']
            print("model complementary carregado com sucesso")

        self.basic_columns = self.remove_numbers_from_list(self.basic_columns)
        self.comp_columns = self.remove_numbers_from_list(self.comp_columns)

        print(self.basic_columns)
        print(self.comp_columns)
    
    def remove_numbers_from_list(self, list_of_strings):
        new_list = []
        for string in list_of_strings:
            new_string = re.sub(r'_+\d+.+\d', '', string)
            new_list.append(new_string)
        
        list_without_duplicates = set(new_list)
        return list_without_duplicates
    
    def predict(self, dados):
        print("Entrou no predict")
        print(dados)
        data = self.read_json(dados)
        self.classification = self.model.predict(data)[0]
        self.classification_proba = self.model.predict_proba(data)[0]
        print(self.classification)
        print(self.classification_proba)
        
        exp_df = self.explainer_function(dados)
        
        return self.outputs[self.classification], self.classification_proba, exp_df

    def check_data(self, columns):
        # Verifique se há dados a mais
        results = ""
        for key in self.dados:
            if key not in columns:
                results += 'O campo '+key+' não é válido.\n'

        # Verifique se há dados faltantes
        for key in columns:
            if key not in self.dados:
                results += 'O campo '+key+' é obrigatório.\n'

        if results == "":
            return True
        else:
            return results
    
    def verificar_dados(self):

        return 0

    def ajustar_dados(self):     
        return 0   
