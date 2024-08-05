import os
# Definição das matrizes onde serão armazenados todos os vetores do sistema
products = []
clients = []
cart = []

def clear():
  os.system("cls" if os.name == "nt" else "clear")

def codeBar(vTotal):
    codigo_barras = "1234567890123456789012345678901234567890"
    valor_boleto = vTotal

    with open("boleto.txt", "w") as arquivo:
        arquivo.write(f"Código de Barras: {codigo_barras}\n")
        arquivo.write(f"Valor do Boleto: R${valor_boleto:.2f}\n")

    print("BOLETO GERADO\n".center(50))
    print(f"Código de Barras: {codigo_barras}")
    print(f"Valor do Boleto: R${valor_boleto:.2f}\n")
    print("As informações do boleto foram salvas no arquivo 'boleto.txt'")
    input("Pressione Enter...")
    clear()


def login():
    clear()
    print("Login\n".center(50))
    print("1. Login Gerente")
    print("2. Login Funcionário")
    office = int(input("\nEscolha a opção:"))
    return office


def password():
    clear()
    password = int(input("Informe a senha:"))
    if password == 123:
        input("Senha correta, Pressione Enter... ")
        clear()
        manager()
    else:
        print("Senha incorreta ")
        input("\nTente Novamente, Pressione Enter...")


def newProduct():
    id = int(input("Informe o ID do produto: "))
    name = str(input("Digite o nome do produto: "))
    price = float(input("Digite o preço do produto: "))
    addProduct(id, name, price)


def addProduct(id, name, price):
    newProd = [id, name, price]
    products.append(newProd)
    print("Produto ", newProd[1], "adicionado")
    input("Pressione Enter...")
    clear() 


def changeProducts():
    id_p = int(input("Qual é o Id ou nome do produto que você quer alterar? "))
    for prod in products:
        if prod[0] == id_p:
            id = int(input("Informe o novo ID do produto: "))
            name = str(input("Digite o novo nome do produto: "))
            price = float(input("Digite o novo preço do produto: "))
            prod[0] = id
            prod[1] = name
            prod[2] = price
            print("Produto atualizado! ")
            input("Pressione Enter...")
            clear()
        else:
            print("Produto não encontrado")


def deleteProducts():
    id_d = int(input("Qual é o Id do produto que deseja excluir?"))
    for prod in products:
        if prod[0] == id_d:
            products.remove(prod)
            print("Produto excluído")
            input("Pressione Enter...")
            clear()


def cartAdd():
    while True:
        addP = str(input("Qual produto deseja adicionar? (Digite '1' para sair):"))
        if addP == "1":
            break
        product_found = False
        for prod in products:
            if prod[1].lower() == addP.lower():
                cart.append(prod)
                print(prod[1], "adicionado")
                product_found = True
        if not product_found:
            print("Produto não cadastrado no sistema, tente novamente ou feche o programa")
            input("Pressione Enter...")
            clear()



def addClient(name, age, cpf):
    client = [name, age, cpf]
    clients.append(client)
    input("Novo Cliente Adicionado com Sucesso, Aperte Enter...")
    clear()


def newClient():
    name = str(input("Informe o nome do cliente? \n"))
    age = int(input("Informe a idade do cliente \n"))
    cpf = str(input("Informe o CPF do cliente \n"))
    addClient(name, age, cpf)


def cartSum(cart):
    sumC = 0
    for i in cart:
        sumC += i[2]
    return sumC


def discount(cart):
    sumC = cartSum(cart)
    if sumC <= 100:
        vDiscount = sumC * 0.05
    elif sumC <= 500:
        vDiscount = sumC * 0.07
    elif sumC <= 1000:
        vDiscount = sumC * 0.10
    elif sumC <= 2000:
        vDiscount = sumC * 0.14
    else:
        vDiscount = sumC * 0.19
    total = sumC - vDiscount
    return total


def showCart(cart, vTotal):
    clear()
    print("Carrinho de Compras\n".center(50))
    print("Valor total: ", vTotal)
    print("Itens do Carrinho:\n ")
    for prod in cart:
        print(prod[1])


def checkClient():
    vTotal = cartSum(cart)  # Começamos com o valor total do carrinho
    name = str(input("\nQual o nome do cliente? \n"))
    client_found = False
    for c in clients:
        if c[0].lower() == name.lower():
             print("Cliente cadastrado, desconto será aplicado\n")
             vTotal = discount(cart)  # Se o cliente é encontrado, aplicamos o desconto
             client_found = True
             break
    if not client_found:
        print("Cliente não cadastrado!\n")
    return vTotal  # Retornamos o valor total (com ou sem desconto)


def employee():
    finalize_purchase_done = False
    while True:
      if not finalize_purchase_done:
        clear()
      else:
        finalize_purchase_done = False
      print("Menu Funcionário\n".center(50))
      print("1. Adicionar produto no carrinho")
      print("2. Cadastrar Clientes")
      print("3. Finalizar compra")
      print("4. Fechar o menu funcionário")
      optional = int(input())
      if optional == 1:
          cartAdd()
      elif optional == 2:
          newClient()
      elif optional == 3:
          vTotalWithoutDiscount = cartSum(cart)  # Valor sem desconto
          showCart(cart, vTotalWithoutDiscount)  # Mostrar carrinho sem desconto
          vTotalWithPossibleDiscount = checkClient() # Aqui pode alterar o valor com base no desconto
          codeBar(vTotalWithPossibleDiscount)  # Gerar boleto com o valor final
          finalize_purchase_done = True
      elif optional == 4:
          print("Fechando o menu funcionário")
          break



def manager():
    while True:
        print("\nMenu Gerente\n".center(50))
        print("1. Criar Produtos ")
        print("2. Alterar Produtos")
        print("3. Deletar Produtos")
        print("4. Fechar o menu gerente")
        option = int(input())
        if option == 1:
            newProduct()
        elif option == 2:
            changeProducts()
        elif option == 3:
            deleteProducts()
        elif option == 4:
            print("Saindo do menu de gerente...")
            break


if __name__ == "__main__":
    while True:
        opcao = login()
        if opcao == 1:
            password()
        elif opcao == 2:
            employee()
        else:
            print("Opção inválida, tente novamente")
