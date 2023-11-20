#Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos, cujos elementos sejam a intercalação dos elementos de A e B.

def cria_lista(numero):
    lista = []

    for i in range(numero):
        numero = int(input())
        lista.insert(i, numero)
    return lista


def intercalar_lista(lista_um, lista_dois):
    lista_intercalada = []
    if (isinstance(lista_um, list) and isinstance(lista_dois, list)):
        for i in range(25):
            lista_intercalada.append(lista_um[i])
            lista_intercalada.append(lista_dois[i])
    return lista_intercalada

def main():
    lista_um = cria_lista(25)
    lista_dois = cria_lista(25)
    resultado = intercalar_lista(lista_um, lista_dois)
    print(lista_um)
    print(lista_dois)
    print(resultado)

if __name__ == '__main__':
    main()