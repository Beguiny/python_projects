def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Trocar os elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Exemplo de uso
lista = [3654, 3448, 2571, 1296, 2234, 1148, 9096]
bubble_sort(lista)
print("Lista ordenada:")
print(lista)