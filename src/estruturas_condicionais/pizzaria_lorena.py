# Sistema de pedidos da Pizzaria da Lorena Carmo
# Projeto desenvolvido em Python


# Mensagem inicial de boas-vindas

print("=" * 45)
print("🍕  BEM-VINDO(A) À PIZZARIA DA LORENA  🍕")
print("=" * 45)
print("Sua pizza favorita está aqui")
print("Confira nosso cardápio e monte seu pedido.")
print("=" * 45)



# Cadastro dos sabores separados por categoria

pizzas_salgadas = {
    1: "Calabresa",
    2: "Frango com Catupiry",
    3: "Portuguesa"
}


pizzas_doces = {
    1: "Brigadeiro",
    2: "Banana com Mussarela e Canela"
}



# Variável para armazenar o valor total do pedido

total_pedido = 0



# LOOP PRINCIPAL DO PEDIDO
# Permite adicionar várias pizzas ao pedido

while True:


    # Escolha do tipo da pizza

    while True:

        print("\nEscolha o tipo de pizza:")
        print("1 - Pizza Salgada")
        print("2 - Pizza Doce")

        try:
            tipo_pizza = int(input("Digite a opção desejada: "))

            if tipo_pizza in [1, 2]:
                break

            else:
                print("Opção inválida. Escolha 1 ou 2.")

        except ValueError:
            print("Digite apenas números.")



    # Exibe sabores conforme o tipo escolhido

    if tipo_pizza == 1:

        cardapio_atual = pizzas_salgadas
        nome_tipo = "Pizza Salgada"

    else:

        cardapio_atual = pizzas_doces
        nome_tipo = "Pizza Doce"



    # Escolha do sabor

    while True:

        print("\nEscolha o sabor:")

        for numero, sabor in cardapio_atual.items():
            print(f"{numero} - {sabor}")


        try:

            opcao_sabor = int(input("Digite a opção desejada: "))


            if opcao_sabor in cardapio_atual:
                break

            else:
                print("Sabor inválido. Escolha uma opção do cardápio.")


        except ValueError:

            print("Digite apenas números.")



    sabor_escolhido = cardapio_atual[opcao_sabor]



    # Escolha do tamanho

    while True:

        print("\nEscolha o tamanho:")
        print("P - Pequena")
        print("M - Média")
        print("G - Grande")


        tamanho = input("Digite o tamanho desejado: ").upper()


        if tamanho in ["P", "M", "G"]:
            break

        else:
            print("Tamanho inválido. Digite P, M ou G.")



    # Definição do preço conforme tipo e tamanho

    if tipo_pizza == 1:  # Pizza salgada

        if tamanho == "P":
            preco = 30

        elif tamanho == "M":
            preco = 45

        else:
            preco = 60


    else:  # Pizza doce

        if tamanho == "P":
            preco = 34

        elif tamanho == "M":
            preco = 48

        else:
            preco = 66



    # Exibe resumo da pizza escolhida

    print("\n🍕 Pizza adicionada ao pedido:")
    print(f"Tipo: {nome_tipo}")
    print(f"Sabor: {sabor_escolhido}")
    print(f"Tamanho: {tamanho}")
    print(f"Valor: R$ {preco},00")



    # Soma o valor ao total do pedido

    total_pedido += preco



    # Pergunta se deseja adicionar outra pizza

    mais_pizza = input("\nDeseja adicionar outra pizza? (S/N): ").upper()


    if mais_pizza == "S":

        print("Vamos adicionar outra pizza ao seu pedido.")


    elif mais_pizza == "N":

        print("\n" + "=" * 60)
        print(f"TOTAL DO PEDIDO: R$ {total_pedido},00")
        print("Obrigado pela preferência! Volte sempre. 🍕")
        print("=" * 60)

        break


    else:

        print("Opção inválida. Finalizando pedido.")

        print(f"TOTAL DO PEDIDO: R$ {total_pedido},00")

        break