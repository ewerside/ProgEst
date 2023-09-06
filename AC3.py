'''
AC3
1) Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa
que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo a tabela a
seguir, baseado no salário atual. Após o aumento ser realizado, informe na tela:

O salário antes do reajuste;
O percentual de aumento aplicado;
O valor do aumento;
O novo salário, após o aumento.
 Salários até R$ 280,00 (incluindo)      Aumento de 20%
 Salários entre R$ 280,00 e R$ 700,00    Aumento de 15%
 Salários entre R$ 700,00 e R$ 1500,00   Aumento de 10%
 Salários de R$ 1500,00 em diante        Aumento de 5%
'''

def novo_salario():
    salario = float(input("Digite o seu salário atual: R$"))
    salario_antigo = salario
    percentual = 0
    if salario <= 280:
        percentual = 20
        salario *= (1 + percentual/100)
    elif salario < 700:
        percentual = 15
        salario *= (1 + percentual / 100)
    elif salario < 1500:
        percentual = 10
        salario *= (1 + percentual / 100)
    else:
        percentual = 5
        salario *= (1 + percentual / 100)
    aumento = salario - salario_antigo
    print(f"\nSeu salário antigo é de: R${salario_antigo:.2f}")
    print(f"Parabéns! Você recebeu {percentual}% de aumento.")
    print(f"Isso representa R${aumento:.2f} de aumento em seu salário.")
    print(f"Seu novo salário é de: R${salario:.2f}\n\n")

# Testando a função:

novo_salario()


'''
2) Implementa uma função que receba um número e exiba o dia correspondente da semana (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido.
'''

def dia_da_semana():
    dia = int(input("Digite o dia da semana: "))
    if dia == 1:
        print("\nDomingo")
    elif dia == 2:
        print("\nSegunda")
    elif dia == 3:
        print("\nTerça")
    elif dia == 4:
        print("\nQuarta")
    elif dia == 5:
        print("\nQuinta")
    elif dia == 6:
        print("\nSexta")
    elif dia == 7:
        print("\nSábado")
    else:
        print("\nDia inválido")
    print("\n\n")

# Testando:

dia_da_semana()


'''
3) Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax^2 + bx + c. O programa deverá 
receber os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de a igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os 
demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.
'''

def segundo_grau():
    a = float(input("Digite o coeficiente a: "))
    if a == 0:
        print("\nSua função não é do segundo grau!")
        return None
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    delta = b*b - 4*a*c
    if delta < 0:
        print("\nSua função não possui raízes reais.")
        return None
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    if delta == 0:
        print(f"\nSua função possui apenas uma raiz real: x={x1}")
        return None
    x2 = (-b - delta ** (1/2))/(2*a)
    print(f"\nA primeira raiz da sua função é x1 = {x1}")
    print(f"A segunda raiz da sua função é x2 = {x2}")

# Testando

segundo_grau()

