import base64
import binascii

# Ler o arquivo hexadecimal
with open('hexfile.txt', 'r') as f:
    hexdata = f.read().strip()

# Converter o hexadecimal para binário
bindata = binascii.unhexlify(hexdata)

# Codificar o binário em base64
b64data = base64.b64encode(bindata)

# Salvar o resultado em um arquivo
with open('base64file.txt', 'w') as f:
    f.write(b64data.decode('utf-8'))