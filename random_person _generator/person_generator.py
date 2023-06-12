import requests

url_api = 'https://api.invertexto.com/v1/faker?token=3733|r7kjURkcZ74Nwwqwae3QIg1EEXCl8wIg&fields=name%2Ccpf%2Ccnpj%2Cemail%2Cusername%2Cphone_number%2C&locale=pt_BR'
headers = {'Content-Type': 'application/json'}

try:
    response = requests.get(url_api, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    nome = response_data['name']
    cpf = response_data['cpf']
    cnpj = response_data['cnpj']
    email = response_data['email']
    usuario = response_data['username']
    telefone = response_data['phone_number']
    
except requests.exceptions.HTTPError as erro:
    if erro.response.status_code != 200:
        print("Erro ao consultar os dados na API")
    else:
        raise erro