import os

# Definição das matrizes onde serão armazenados todos os vetores do sistema
products = []
clients = []
cart = []


def login():
    # Função principal, onde o funcionário e/ou gerente fará login em seu devido sistema
    print("Login\n".center(50))
    print("1. Login Gerente")
    print("2. Login Funcionário")
    office = int(input("\nEscolha a opção"))
    match (office):
        case 1:
            password()    
        case 2:
            employee()

def password():
    # Senha do gerente
    password = int(input("Informe a senha"))
    match (password):
        case 123:
            print("Senha correta, entrando no sistema... ")
            manager()
        case _:
            print("Senha incorreta ")


def newProduct():
    # Cadastrar novo produto na loja, encaminhará para função que adicionará esse produto a matriz de produtos 
    id = int(input("Informe o ID do produto: "))
    name = str(input("Digite o nome do produto: "))
    price = float(input('Digite o preço do produto: '))
    addProduct(id, name, price)


def addProduct(id, name, price):
    # Onde o produto é devidamente adicionado a matriz, função criada para deixar código mais limpo
    newProd = [id, name, price]
    products.append(newProd)
    print("Produto ", newProd[1], "adicionado")


def changeProducts():
    # Em caso de mudança de preço, ou mesmo produto, mas de marca diferente, está função fará a mudança através do ID do produto
    # Por isso é bom o gerente ter uma tabela em excel com os produtos e seu ID
    id_p = int(input("Qual é o Id ou nome do produto que você quer alterar? "))
    for prod in products:
        if prod[0] == id_p:
            id = int(input("Informe o novo ID do produto: "))
            name = str(input("Digite o novo nome do produto: "))
            price = float(input('Digite o novo preço do produto: '))
            prod[0] = id
            prod[1] = name
            prod[2] = price
            print("Produito atualizado! ")
        else:
            print("Produto não encontrado")


def deleteProducts():
    # Esta função apagará o produto que o gerente desejar através de seu ID
    id_d = int(input("Qual é o Id do produto que deseja excluir?"))
    for prod in products:
        if prod[0] == id_d:
            products.remove(prod)
            print("Produto excluído")

def cartAdd():
    # Aqui o funcionário um item ao carrinho
    while True:
        addP = str(input(
            "Qual produto deseja adicionar? (Por favor, digite sem acentuação, por exemplo: 'Feijao')"))
        # Quando tiver acab
        if addP == "exit":
            print("Finalizando o programa ...")
            break

        product_found = False  # Variável para verificar se o produto foi encontrado

        for prod in products:
            if prod[1].lower() == addP.lower():
                cart.append(prod)
                print(prod[1], "adicionado")
                product_found = True  # Define como True se o produto for encontrado

        if not product_found:
            print("Produto não cadastrado no sistema, tente novamente ou feche o programa")


def addClient(name, age, cpf):
    # Adiciona o cliente trago por newClient a matriz
    client = [name, age, cpf]
    clients.append(client)
    print("Novo Cliente Adicionado com Sucesso!") 


def newClient():
    #   Criará um novo cliente e mandará pra funcao que adiciona a matriz
    name = str(input("Informe o nome do cliente? \n"))
    age = int(input("Informe a idade do cliente \n"))
    cpf = str(input("Informe o CPF do cliente \n"))
    addClient(name, age, cpf)




def cartSum(cart): 
    # Soma do total de produtos adicionados ao carrinho
    sumC = 0
    for i in cart:
        sumC += i[2]
    return sumC
def discount(cart):
    #  Na funcao checkCllient, será checado se o comprador é um cliente, caso seja...
    # ...será jogado a essa funcao que descreve o desconto
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
    # Função simples que mostra TUDO que foi adicionado ao carirno
    print("\t\tCarrinho de Compras")
    print("Valor total: ", vTotal)
    print("Itens do carrinho: ")
    for prod in cart:
        print(prod[1])


def checkClient():
    # Funcao que checará quem é cliente, e se tem direito ao desconto ou nao
    vTotal = 0
    name = str(input("Qual o nome do cliente? \n"))
    for c in clients:
        if c[0].lower() == name.lower():
            print("Cliente cadastrado, desconto será aplicado")
            vTotal = discount(cart)
            print()
        else:
            print("Cliente não cadastrado!")
            vTotal = cartSum(cart)

    return vTotal



def employee():
    # Funcao envolvendo tudo que o funcionário pode fazer
    while True:
        print("\nMenu Funcionário\n".center(50))
        print("1. Adicionar produto no carrinho")
        print("2. Cadastrar Clientes")
        print("3. Finalizar compra")
        print("4. Fechar o menu funcionário")
        optional = int(input())
        match (optional):
            case 1:
                cartAdd()
            case 2:
                newClient()
            case 3:
                showCart(cart, checkClient()) 
            case 4:
                print("Fechando o menu funcionário")
                break


def manager():
    # Funcao com todos os poderes do gerente
    while True:
        print("\nMenu Gerente\n".center(50))
        print("1. Criar Produtos ")
        print("2. Alterar Produtos")
        print("3. Deletar Produtos")
        print("4. Fechar o menu gerente")
        option = int(input())
        match (option):
            case 1:
                newProduct()
            case 2:
                changeProducts()
            case 3:
                deleteProducts()
            case 4:
                print("Saindo do menu de gerente...")
                break



if __name__ == "__main__":
  # Funcao principal, o menu onde tudo começará
  while True:
    opcao = login()
    match (opcao):
      case 1:
        manager()
      case 2:
        employee()
      case _:
        print("Opção inválida, tente novamente")