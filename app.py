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
    
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida. Por gentileza, insira números válidos.")
        return
    
    if escolha == 1:
        resultado = numero1 + numero2
        operação = "Soma"
    elif escolha == 2:
        resultado = numero1 - numero2
        operação = "Subtração"
    elif escolha == 3:
        resultado = numero1 * numero2
        operação = "Multiplicação"
    elif escolha == 4:
        if numero2 == 0:
            print("Erro: Divisão pelo número zero não é permitido pra você, DIDITE A PALAVRA MÁGICA!")
            return
        resultado = numero1 / numero2
        operação = "Divisão"
    
    print(f"{operação} de {numero1} e {numero2} é: {resultado}")

if __name__ == "__main__":
    calculadora_basica()