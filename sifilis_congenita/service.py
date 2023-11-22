from model import Model

def basic_service(dados):
    #Verificar os dados que chegaram se estão corretos

    #Carregar model
    model = Model(dados)
    result = model.check_data(model.basic_columns)

    return result

    #Fazer predição

    
    #Return (verificar se antes, vamos salvar no banco um log de todas as predições)

def complementary_service(dados):
    #Verificar os dados que chegaram se estão corretos

    #Carregar model

    #Fazer predição

    #Return (verificar se antes, vamos salvar no banco um log de todas as predições)
    return 0



def adjust_reponse(status, predict):
    return 0
