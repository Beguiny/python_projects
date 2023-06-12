import csv
import json

def json_to_csv(json_file, csv_file):
    # Abrir o arquivo JSON de origem
    with open(json_file, 'r') as file:
        # Carregar o conteúdo JSON
        json_data = json.load(file)
    
    # Obter as chaves do JSON como cabeçalhos para o CSV
    headers = list(json_data[0].keys())

    # Abrir o arquivo CSV de destino
    with open(csv_file, 'w', newline='') as file:
        # Criar um escritor CSV
        writer = csv.DictWriter(file, fieldnames=headers)

        # Escrever o cabeçalho
        writer.writeheader()

        # Escrever os dados
        writer.writerows(json_data)

# Exemplo de uso
json_to_csv('dados2.json', 'dados2.csv')