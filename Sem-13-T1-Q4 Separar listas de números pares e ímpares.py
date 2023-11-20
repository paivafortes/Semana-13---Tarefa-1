#Leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas

def criar_lista(numero):
    lista = []
    pares = []
    inpares = []

    for i in range(numero):
        numeros = int(input())

        lista.insert(i, numeros)
        if (numeros % 2 == 0):
            pares.append(numeros)

        elif (numeros % 2 != 0):
            inpares.append(numeros)
    return lista, pares, inpares

def main():
    lista, lis_pares, lista_impares = criar_lista(20)
    print(f'{lista}\n{lis_pares}\n{lista_impares}')

if __name__ == "__main__":
    main()