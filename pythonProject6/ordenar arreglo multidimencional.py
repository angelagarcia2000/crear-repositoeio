# Ordenación de Arreglo Multidimensional

matriz = [[3, 5, 1],
          [4, 7, 8],
          [7, 2, 6]]

print("imprimir matriz sin ordenar", matriz)

#Ordenar matriz
matriz.sort(key=lambda fila: min (fila))

#resultado
print("matriz ordenada de mayor a menor en su respectiva fila:")
for fila in matriz:
    print(fila)