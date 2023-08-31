# AC2 (1)

def salario_mes(sal_hr, hrs_trab):
    return sal_hr * hrs_trab

def descobrir_salario():
    salario_hora = float(input("Quanto você ganha por hora? R$"))
    horas_trabalhadas = float(input("Quantas horas você trabalhou esse mês? "))
    salario = salario_mes(sal_hr=salario_hora, hrs_trab=horas_trabalhadas)
    print("Seu salário este mês será de R$", salario)

#Demonstração:
descobrir_salario()



# AC2 (2)

def operacoes(a, b, c):
    # Matematicamente, a expressão numérica abaixo poderia ser simplificada para "a*b",
    # porém coloquei exatamente como o exercício pediu.
    print(2*a*b/2)
    print(3*a+c)
    print(c**3)

#Demonstração:
operacoes(3,4,5)



# AC2 (3)

def operacoes(a, b, c):
    # Matematicamente, a expressão numérica abaixo poderia ser simplificada para "a*b",
    # porém coloquei exatamente como o exercício pediu.
    res1 = 2*a*b/2
    res2 = 3*a+c
    res3 = c**3
    return res1, res2, res3

#Demonstração:
resultados = operacoes(3,4,5)
print(resultados)


# AC2 (4)

def calc_bis(ano):
    bis = (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0))
    return bis


def bissexto():
    ano = int(input("Digite um ano: "))
    resultado = calc_bis(ano)
    print("O ano digitado é bissexto? ", resultado)
    

#Demonstração:

bissexto()
