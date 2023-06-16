while True:
    operacao = int(input("\nEscolha o operar que quer usar:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\n Numero: "))

    if operacao > 4:
        print ("O operador escolhido é invalido")
        break
    else:
        try:
            numero_um = int(input("\nDigite o primeiro numero da conta: "))
        except ValueError:
            print("Você digitou um caractere inválido. Por favor, digite um número inteiro.")
            break
        try:
            numero_dois = int(input("Digite o segundo numero da conta:"))
        except ValueError:
            print("Você digitou um caractere inválido. Por favor, digite um número inteiro.")
            break

        if operacao == 1:
                print("A soma dos dois números é ", numero_um + numero_dois)
        elif operacao == 2:
                print("A subtração dos dois números é ", numero_um - numero_dois)
        elif operacao == 3:
                print("A multiplicação dos dois números é ", numero_um * numero_dois)
        elif operacao == 4:
                print("A divisão dos dois números é ", numero_um / numero_dois)
        else:
                print("Foi inserido informações invalidas")

        continuar = int(input("\nDeseja efetuar outra operação matematica?\n1 - Sim\n2 - Não\n \nresposta:"))
        if continuar == 2:
            print ("Programa encerrado")
            break
        elif continuar == 1:
             continue
        else:
            print("Foi inserido informações invalidas")