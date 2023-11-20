# 1. Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.

def ler_lista(numero):
    lista = []
    soma = 0
    multiplicacao = 1
    for i in range(numero):
        numeros = int(input())
        lista.insert(i,numeros)
        soma += numeros
        multiplicacao *= numeros

    return lista, soma, multiplicacao    

def main():
    lista, soma, multiplicacao = ler_lista(10)

    print(f'{lista}\n{soma}\n{multiplicacao}')

if __name__ == "__main__":
    main()