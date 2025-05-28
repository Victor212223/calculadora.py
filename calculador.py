while True:
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")
    operador = input("Digite o operador (+ - * /): ")

    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
    except:
        print("Digite um número válido.")
        continue

    if operador == "-":
        resultado = num_1 - num_2

    elif operador == "+":
        resultado = num_1 + num_2

    elif operador == "/":
        if num_2 == 0:
            print("Não é possível dividir por zero.")
            continue
        resultado = num_1 / num_2

    elif operador == "*":
        resultado = num_1 * num_2

    else:
        print("Operador inválido. Digite apenas + - * ou /.")
        continue

    print(f"O resultado é: {resultado}")

    sair = input("Deseja sair? [s]im ou [n]ão: ").lower()
    if sair.startswith("s"):
        print("Encerrando a calculadora...")
        break