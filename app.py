def calculadora_basica():
    print("Bem-vindo à Calculadora do Ériko!")
    print("Escolha a operação: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    while True:
        try:
            escolha = int(input("Digite o número da operação (1/2/3/4): "))
            if escolha not in [1, 2, 3, 4]:
                raise ValueError("Escolha inválida.")
            break
        except ValueError as e:
            print(f"Erro: {e} Por gentileza, escolha uma opção válida.")
    