from os import getenv
import requests as re
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

# Carrengando as variaveis do arquivo .env
load_dotenv()

lista_ceps  = ['08598690', '08598680','08598500' '04101300','23575460']

def request_api_via_cep():
    try:
        data = []  # criando uma lista para retornar os resultados do response
        for cep in lista_ceps:
            response = re.get(f"{getenv('HOST')}/{cep}/json/")
            if response.status_code == 200:
                logging.info(f"Requisição realizada com sucesso para o cep: {cep}")
                logging.info(f"Response: {response.text}")
                data.append(response.json()) # Adicionando o response a lista casso tenha sucesso
        return data
    except Exception as e:
        logging.error(f"Ocorreu um erro ao realizar a requisição: {e}")
        return (e)



if __name__ == "__main__":
    data = request_api_via_cep()   # Resgatando informações da lista de ceps retornada 
    # print(len(data))
    # print(data[0]['cep'])

    # Percorrendo a lista de ceps retornada
    for i in range(len(data)):
        print(f"Dados de localidade do indice '{i + 1}'")
        print('='*33)
        print(f"cep: {data[i]['cep']}") if data[i]['cep'] else None
        print(f"Logradouro: {data[i]['logradouro']}") if data[i]['logradouro'] else None
        print(f"Complement: {data[i]['complemento']}") if data[i]['complemento'] else None
        print(f"Bairro: {data[i]['bairro']}") if data[i]['bairro'] else None
        print(f"Localidade: {data[i]['localidade']}") if data[i]['localidade'] else None
        print(f"UF: {data[i]['uf']}") if data[i]['uf'] else None
        print(f"IBGE: {data[i]['ibge']}") if data[i]['ibge'] else None
        print(f"GIA: {data[i]['gia']}") if data[i]['gia'] else None
        print(f"DDD: {data[i]['ddd']}") if data[i]['ddd'] else None
        print(f"SIAFI: {data[i]['siafi']}") if data[i]['siafi'] else None
        print('='*33)

# Criando o cabecalho do arquivo
cabecalho = 'cep;logradouro;complemento;bairro;localidade;uf;ibge;gia;ddd;siafi\n'

# Criando um arquivo.csv para armazenar os dados retornados
with open('dados.csv', 'w') as file:  # Caso o arquivo não exista ele cria um novo devido ao parametro x
    file.write(cabecalho)  # Escrevendo o cabeçalho no arquivo
    for i in range(len(data)):
        file.write(f"{data[i]['cep']};" \
                   f"{data[i]['logradouro']};" \
                   f"{data[i]['complemento']};" \
                   f"{data[i]['bairro']};" \
                   f"{data[i]['localidade']};" \
                   f"{data[i]['uf']};" \
                   f"{data[i]['ibge']};" \
                   f"{data[i]['gia']};" \
                   f"{data[i]['ddd']};" \
                   f"{data[i]['siafi']};\n")  # Escreve o conteúdo no arquivo .csv