"""Aplicação desenvolvida para facilitar o entendimento e ajudar nas atividades de matematica aplicada a computação"""




def decimal():
    binario = input('Entre com o número binário: ')
    lista_binar = [int(digito) for digito in binario]#converte a string em inteiros individuais
    
    valor_decimal = 0
    for i in range(len(lista_binar)):#para as iterações no tamanho da lista 
        valor_decimal += lista_binar[-(i+1)] * (2 ** i)#iterador  de [-1]*2**iterador

    print(f"Valor decimal: {valor_decimal}")


def binarios():
    binarios = []
    decimal = int(input('digite o valor decimal: '))

    while decimal>1:
        resto = decimal//2 # resto recebe a divisao inteira do input pela base binaria "2".
    
        binario = decimal%2 # o binario deve receber o resto da divisao,
        decimal = resto
        binarios.insert(0,binario)# o binario e inserido sepre ana primeira posição da lista
        if binario <= 1:#quando o binario for =< 1 significa que ele não podera ser um divisor e sera então acrecentado a lista
            binarios.insert(0,1)
    
    print(binarios)


def hexadecimal_para_decimal():
    hexadecimal = input('Entre com o número hexadecimal: ')
    mapa_hexadecimal = {
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }#possui os numeros e a representação em letras
    
    
    lista_hexadecimal = []
    for digito in hexadecimal:
        if digito in mapa_hexadecimal:
            lista_hexadecimal.append(mapa_hexadecimal[digito])# Converte cada dígito para seu valor numérico
        else:
            lista_hexadecimal.append(int(digito))# considera o decimal de 0 a 9
    
    valor_decimal = 0
    for i in range(len(lista_hexadecimal)):
        valor_decimal += lista_hexadecimal[-(i+1)] * (16 ** i)#Calcula e soma os valores 
    
    print(f"Valor decimal: {valor_decimal}")


def decimal_para_hexadecimal():
    decimal=int(input('Entre com o número hexadecimal: '))
    r=hex(decimal)[2:]#aqui usaremos uma solução nativa do python para trasformar em hexadecimal
    print(r)

#Inicio do programa
while True:
    print('\n0-Sair\n1-Converter binario para decimal\n2-Converter decimal para binario\n3-Converter hexadecimal para decimal\n4-Converter decimal para hexadecimal')
    menu=input("Escolha uma acao: ")
    if menu=='1':
        decimal()
    elif menu =='2':
        binarios()
    elif menu =='3':
        hexadecimal_para_decimal()
    elif menu == '4':
        decimal_para_hexadecimal()
    elif menu == "0":
        break

    

