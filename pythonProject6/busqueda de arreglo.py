# Búsqueda en Arreglo Multidimensional

#Matriz bidimencional.

matrbidi = [[6, 9, 6],
            [3, 6, 2],
            [4, 7, 2]]

# valor a buscar.
valorbus= 3

# Variables.
enctfila = -1
encontcolumna = -1

#Buscamos el valor dentro de la matriz.
for fila in range(len(matrbidi)):
    for columna in range(len(matrbidi[fila])):
        if matrbidi[fila][columna] == valorbus :
            enctfila = fila
            encontcolumna = columna
            break

#Mensaje que demuestra si se encontro o no se encontro el valor dentro de la matriz.

if enctfila != -1:
    print("se encontro el valor", valorbus)
    print("en la fila", enctfila,)
    print("y en la columna", encontcolumna)