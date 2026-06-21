def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Contar de 1 até um número informado ")
        print("2. Calcular média de notas ")
        print("3. Mostrar a tabuada de um número ")
        print("4. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero = int(input("Digite um número: "))
            for i in range(1, numero + 1):
                print(i)

        elif opcao == "2":
            soma = 0
            contador = 0
            continuar = "s"
            while continuar.lower() == "s":
                nota = float(input("Digite uma nota: "))
                soma += nota
                contador += 1
                continuar = input("Deseja adicionar outra nota? (s/n): ")
            media = soma / contador
            print(f"A média das notas é: {media:.2f}")

        elif opcao == "3":
            numero = int(input("Digite um número para ver a tabuada: "))
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")

        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


menu()
