import csv
import json

def csv_to_json(csv_file, json_file):
    # Abrir o arquivo CSV de origem
    with open(csv_file, 'r') as file:
        # Ler as linhas do arquivo CSV
        csv_data = csv.DictReader(file)
        # Converter as linhas para uma lista de dicionários
        data_list = list(csv_data)

    # Escrever os dados em formato JSON para o arquivo de destino
    with open(json_file, 'w') as file:
        file.write(json.dumps(data_list, indent=4))

# Exemplo de uso
csv_to_json('dados.csv', 'dados.json')
