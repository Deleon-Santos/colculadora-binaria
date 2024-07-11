


def decimal():
    #Converte para decimal 

    binario = input('Entre com o número binário: ')
    lista_binar = [int(digito) for digito in binario]

    valor_decimal = 0
    for i in range(len(lista_binar)):
        valor_decimal += lista_binar[-(i+1)] * (2 ** i)

    print(f"Valor decimal: {valor_decimal}")
def binarios():
#Converte para binario
    binarios = []
    decimal = int(input('digite o valor decimal: '))

    while decimal>1:
        resto = decimal//2
    
        binario = decimal%2
        decimal = resto
        binarios.insert(0,binario)
    if binario <= 1:
        binarios.insert(0,1)
    
    print(binarios)

def hexadecimal_para_decimal():
    # Converte para decimal 
    hexadecimal = input('Entre com o número hexadecimal: ')
    mapa_hexadecimal = {
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    # Converte cada dígito para seu valor numérico
    lista_hexadecimal = []
    for digito in hexadecimal:
        if digito in mapa_hexadecimal:
            lista_hexadecimal.append(mapa_hexadecimal[digito])
        else:
            lista_hexadecimal.append(int(digito))
    
    valor_decimal = 0
    for i in range(len(lista_hexadecimal)):
        valor_decimal += lista_hexadecimal[-(i+1)] * (16 ** i)
    
    print(f"Valor decimal: {valor_decimal}")


print('1-Converter binario para decimal\n2-Converter decimal para binario\n3-Converter hexa para decimal\n')
menu=input("Escolha uma ação")
if menu=='1':
    decimal()
elif menu =='2':
    binarios()
elif menu =='3':
    hexadecimal_para_decimal()
    
