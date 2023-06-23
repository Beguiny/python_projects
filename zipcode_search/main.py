import requests

cep = input("Digite o Cep do endereço desejado: ")

url_api = f'https://viacep.com.br/ws/{cep}/json/'

try:
    response = requests.get(url_api)
    response.raise_for_status()
    retorno = response.json()

    print(retorno)

except requests.exceptions.RequestException as e:
    print("Ocorreu um erro na requisição:", e)
