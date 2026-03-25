import operacoes

print("--CALCULADORA FATEC--")

while True:
    print("Insira o número da operação desejada:")
    print("1 - Soma")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    escolha = int(input())
    if escolha not in (1, 2, 3):
        print("Inválido, tente novamente.")
        continue

    print("Escolha o primeiro número: ")
    a = int(input())

    print("Escolha o segundo número: ")
    b = int(input())
    

    if escolha == 1:
        print(f"O resultado da soma é : {operacoes.somar(a, b)}")

    if escolha == 2:
        print(f"O resultado da subtração é : {operacoes.subtrair(a, b)}")
    
    if escolha == 3:
        print(f"O resultado da multiplacaçao é : {operacoes.multiplicar(a, b)}")

        
