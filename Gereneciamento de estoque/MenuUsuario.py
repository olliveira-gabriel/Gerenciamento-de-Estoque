import main

Menu = 0


while Menu != 7:

    op = int(input("\n=========== Escolha a alterão que você deseja =========  \n\n 1) Adicionar Produto \n 2) Remover Produto \n 3) Editar produto do estoque \n 4) exibir estoque \n 5) Limpar Estoque \n 6) Finalizar Sistema\n\n Escolha uma opção: "))

    match op:

        case 1:
            Id = int(input("Digite o ID do produto: "))
            Nome = str(input("Digite o nome do produto: "))
            preco = str(input("Digite o preco do produto (0.00): "))
            Marca = str(input("Digite o Marca do produto: "))
            
            ProdutoUsuario = main.Produtos(Id, Nome, preco, Marca)
            main.estoque.adicionar_produto(ProdutoUsuario)

        case 2:
            Id = int(input("Digite o ID do produto que deseja remover: "))
            main.estoque.RemoverProduto(Id)

        case 3:
            Id = int(input("Digite o ID do produto que deseja Alterar: "))
            if Id in main.estoque.estoque:
                NovoNome = input("Digite o novo nome do produto: ")
                NovoPreco = float(input("Digite o novo preco do produto (0.00): "))  
                NovaMarca = input("Digite a nova marca do produto: ")
                
                main.estoque.EditarProduto(Id, NovoNome=NovoNome, NovoPreco=NovoPreco, NovaMarca=NovaMarca)
            else:
                print("Produto não encontrado")

        case 4:
            main.estoque.mostrar_estoque()

        case 5:
            main.estoque.LimparEstoque()

        case 6:
            print(" Finalizar Sistema ")
            break 

        case _:
            print("Digite uma opção valida!")





