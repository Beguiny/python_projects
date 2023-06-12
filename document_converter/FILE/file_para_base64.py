import base64

# Ler o arquivo binário
with open('giga.txt', 'rb') as f:
    bindata = f.read()

# Converter os bytes para uma string base64
base64data = base64.b64encode(bindata).decode('utf-8')

# Salvar a string base64 em um arquivo
with open('base64file.txt', 'w') as f:
    f.write(base64data)