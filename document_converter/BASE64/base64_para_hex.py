import binascii

# Ler a string hexadecimal do arquivo
with open('base64file.txt', 'r') as f:
    hexdata = f.read()

# Converter a string hexadecimal de volta para bytes
bindata = binascii.unhexlify(hexdata)

# Salvar os bytes em um arquivo binário
with open('file.txt', 'wb') as f:
    f.write(bindata)