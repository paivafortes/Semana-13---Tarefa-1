#Escreva um programa que leia um número n. Considere uma lista com n posições, e então: a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais. b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal. c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.

def cria_lista_inversa(n):

    lista = []
    if (n):
        for i in range(n):
            numeros = float(input())
            numeros = f'{numeros:.4f}'
            lista.insert(i, float(numeros))
        lista.reverse()
    return lista

def cria_lista(n):

    lista = []
    contador = 0
    soma = 0
    media = 0
    for i in range(n):
        notas = float(input())
        notas = f'{notas:.1f}'
        lista.insert(i, float(notas))
        soma += float(notas)
        contador += 1
    media = soma / contador
    return lista, media

def imprimi_vogais_consoantes(n):

    valor = ''
    vogais = 0
    lista_consoantes = []
    if (n):
        for i in range(n):
            valor = input()[0]

            if (valor in ('aeiouAEIOU')):
                vogais += 1
            elif (valor not in ('aeiou')):
                lista_consoantes.append(valor)
    return vogais, lista_consoantes

def main():
    n = int(input())
    if (n != 0):
        lista_inversa = cria_lista_inversa(n)
        lista_notas, media_notas = cria_lista(n)
        vogais, consoante = imprimi_vogais_consoantes(n)
        print(lista_inversa)
        print(f'{lista_notas}\n{media_notas:.1f}')
        print(f'{vogais}\n{consoante}')
    elif (n == 0):
        print(f'[]\n[]\nSEM NOTAS\n0\n[]')

if __name__ == "__main__":
    main()