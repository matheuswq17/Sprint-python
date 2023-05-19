# Cria uma lista vazia para armazenar os itens
itens = []

# Define uma função para adicionar um novo item à lista
def adicionar_item():
    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade do item: "))
    itens.append({"nome": nome, "quantidade": quantidade})
    print("Item adicionado com sucesso!")

# Define uma função para buscar um item na lista
def buscar_item():
    nome = input("Digite o nome do item que deseja buscar: ")
    for item in itens:
        if item["nome"] == nome:
            print("Item encontrado:")
            print("Nome:", item["nome"])
            print("Quantidade:", item["quantidade"])
            return
    print("Item não encontrado.")

# Define uma função para listar todos os itens da lista
def listar_itens():
    if len(itens) == 0:
        print("Não há itens na lista.")
    else:
        print("Lista de itens:")
        for item in itens:
            print("Nome:", item["nome"])
            print("Quantidade:", item["quantidade"])

# Define uma função para exibir o menu de opções
def exibir_menu():
    print("Selecione uma opção:")
    print("1 - Adicionar um novo item")
    print("2 - Buscar um item")
    print("3 - Listar todos os itens")
    print("4 - Sair do programa")

# Utiliza um loop para exibir o menu e processar as escolhas do usuário
while True:
    exibir_menu()
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        adicionar_item()
    elif escolha == 2:
        buscar_item()
    elif escolha == 3:
        listar_itens()
    elif escolha == 4:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
