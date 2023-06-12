import binascii

# Abre o arquivo de entrada com dados hexadecimais
with open('hexfile.txt', 'r') as input_file:
    hex_data = input_file.read().strip()

# Converte os dados hexadecimais em binários
bin_data = binascii.unhexlify(hex_data)

# Grava os dados binários em um arquivo de saída
with open('giga.txt', 'wb') as output_file:
    output_file.write(bin_data)