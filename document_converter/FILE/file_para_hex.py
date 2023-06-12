import binascii

# Ler o arquivo binário
with open('giga.txt', 'rb') as f:
    bindata = f.read()

# Converter os bytes para uma string hexadecimal
hexdata = binascii.hexlify(bindata).decode('utf-8')

# Salvar a string hexadecimal em um arquivo
with open('hexfile.txt', 'w') as f:
    f.write(hexdata)