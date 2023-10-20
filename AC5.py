def imprime_numeros():
    max_num = int(input("Digite o número máximo: "))
    numbers_list = []
    for number in range(max_num):
        numbers_list.append(number+1)
        for item in numbers_list:
            print(item, end="   ")
        print("")

imprime_numeros()

def quantidade_de_digitos():
    numero = input("Digite um número inteiro: ")
    # Como queremos a quantidade de dígitos, manter o número como string nos é vantajoso.
    print(f"O número {numero} possui {len(numero)} dígito(s).")

quantidade_de_digitos()

def divisao():
    resultado = None
    while resultado == None:
        try:
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o segundo valor: "))
            resultado = num1/num2
        except ValueError:
            print("Dados inválidos! Digite um número inteiro!")
        except ZeroDivisionError:
            print("Você não pode dividir um número por zero!")
        finally:
            if resultado:
                print(resultado)

divisao()
