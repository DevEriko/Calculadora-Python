'''Implementação de um código simples de uma calculadora em Python que permite escolher operações matematicas simples, utilizei 
o "try" e "except" para garantir que o código não quebre caso o Cabeçudo coloque dados inválidos.'''

def calculadora_basica():
    # Exibição para o usuário fazer a escolha das operações da calculadora
    print("Bem-vindo à Calculadora do Ériko!")
    print("Escolha a operação: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    while True: # Aqui é o laço de repetição até o usuário fornecer uma escolha que dê para ser realizada.
        try:
            escolha = int(input("Digite o número da operação (1/2/3/4): ")) # Adicionei o "int" para converter o número para inteiro.
            if escolha not in [1, 2, 3, 4]:
                raise ValueError("Escolha inválida.") # Se o usuário da calculadora escolher um número que não seja inteiro, mensagem de erro aparecerá!
            break # Sai do laço quando for digitado o número correto.
        except ValueError as e:
            print(f"Erro: {e} Por gentileza, escolha uma opção válida.") # Aqui é pro cabeçudo escolher a opção válida kkkk...
    
    try:
        # Aqui eu coloquei o "float" para converter a entrada dos números para decimais, única opção! Números decimais.
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida. Por gentileza, insira números válidos.") # Aqui mais uma vez, CABEÇUDO... uma opção válida.
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
        if numero2 == 0: # Se o usuário digitar zero para dividir, o programa imprime uma mensagem de erro.
            print("Erro: Divisão pelo número zero não é permitido pra você, DIDITE A PALAVRA MÁGICA!") # A palavra mágica é zoeira kkk...
            return
        resultado = numero1 / numero2
        operação = "Divisão"
    
    print(f"{operação} de {numero1} e {numero2} é: {resultado}") # O programa no terminal irá apresentar a exibição do resultado.

if __name__ == "__main__":
    calculadora_basica()