from math import floor, ceil

# E_PRIMO
def divisores(num):
    lista_divisores = []
    for divisor in range(2, ceil(num/2)+1):
        if num % divisor == 0:
            lista_divisores.append(divisor)
    return lista_divisores

# Decidi separar a função de encontrar os divisores dos não primos da função que
# descobre se o número é primo. Fiz isso pois é mais eficiente buscar por
# divisores apenas de 2 até a raiz do número "n" testado. Isso porque,
# considerando √n * d, se d < √n, já foi testado se n é divisível por d. Já se
# d > √n, √n * d já é maior que o número "n" a ser testado.
def e_primo(num):
    for divisor in range(2, floor(num**(1/2))+1):
        if num % divisor == 0:
            print(f"Divisores: {divisores(num)}")
            return "Não é primo!"
    return "É primo"

numero = int(input("Número: "))

print(e_primo(numero)+"\n")


# DÍVIDA
def parcelamento(divida):
    tabela_final = ("Quantidade de Parcelas  % de Juros sobre o valor inicial "
                    "da dívida\n1                       0\n")
    tabela_parcelas = (f'Valor dos Juros Valor Total     Quantidade de Parcelas'
                       f'  Valor da Parcela\n0               R$ {divida}'
                       f'{(13-len(str(divida)))*" "}1                       R$'
                       f'  {divida}\n')
    juros = 10

    for parcelas in range(3, 13, 3):
        tabela_final += f'{parcelas}{(24-len(str(parcelas)))*" "}{juros}\n'

        acrescimo = juros/100 * divida
        valor_total = round(divida+acrescimo, 2)
        valor_parcela = round(valor_total / parcelas, 2)

        tabela_parcelas += (f'{juros}{(16-len(str(juros)))*" "}R$ {valor_total}'
                            f'{(13-len(str(valor_total)))*" "}{parcelas}'
                            f'{(24-len(str(parcelas)))*" "}R$  '
                            f'{valor_parcela}\n')

        juros += 5
    tabela_final += "\n" + tabela_parcelas
    print(tabela_final)

parcelamento(2500)


# INTERVALOS
def intervalos():
    intervalo_0_25 = 0
    intervalo_26_50 = 0
    intervalo_51_75 = 0
    intervalo_76_100 = 0
    numeros = []
    num = int(input("Digite um número positivo: "))
    while num >= 0:
        if num not in numeros:
            numeros.append(num)
            if num <= 25:
                intervalo_0_25 += 1
            elif num <= 50:
                intervalo_26_50 += 1
            elif num <= 75:
                intervalo_51_75 += 1
            elif num <= 100:
                intervalo_76_100 += 1
        num = int(input("Digite um número positivo: "))
    print(numeros)
    print(f"Intervalo [0-25]: {intervalo_0_25} números")
    print(f"Intervalo [26-50]: {intervalo_26_50} números")
    print(f"Intervalo [51-75]: {intervalo_51_75} números")
    print(f"Intervalo [76-100]: {intervalo_76_100} números")

intervalos()





