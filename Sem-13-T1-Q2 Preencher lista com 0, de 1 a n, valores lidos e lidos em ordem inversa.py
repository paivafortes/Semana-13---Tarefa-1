#Escreva um programa que leia um número n. Considere uma lista com n posições, e então: a) preencha com 0 (zero) e imprima a lista; b) preencha com os números de 1 a n e imprima a lista; c) preencha com valores lidos pelo teclado e imprima a lista; d) preencha na ordem inversa com valores lidos pelo teclado e imprima a lista; dica: use insert para sempre incluir os elementos no início da lista;

def cria_lista_com_zeros(numero):
    lista = []

    for i in range(numero):

        lista.insert(i, 0)
    return lista

def cria_lista_de_um_a_numero(numero):
    lista = []
    numeros = 1
    for i in range(numero):

        lista.insert(i, numeros)
        numeros += 1
    return lista

def cria_lista(numero):
    lista = []
    for i in range(numero):
        numeros = int(input())
        lista.insert(i, numeros)
    return lista

def cria_lista_inversa(numero):
    lista = []
    for i in range(numero):
        numeros = int(input())
        lista.insert(i, numeros)
    lista.reverse()
    return lista

def main():
    n = input()
    n = int(n)

    lista_com_zeros = cria_lista_com_zeros(n)
    lista_numero_ate_numero = cria_lista_de_um_a_numero(n)
    cria_uma_lista = cria_lista(n)
    criar_lista_inversa = cria_lista_inversa(n)

    print(f'{lista_com_zeros}\n{lista_numero_ate_numero}\n{cria_uma_lista}\n{criar_lista_inversa}')

if __name__ == "__main__":
    main()