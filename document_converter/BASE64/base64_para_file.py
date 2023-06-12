import base64

# Ler a string base64 do arquivo
with open('base64file.txt', 'r') as f:
    base64data = f.read()

# Converter a string base64 de volta para bytes
bindata = base64.b64decode(base64data)

# Salvar os bytes em um arquivo binário
with open('file2.txt', 'wb') as f:
    f.write(bindata)