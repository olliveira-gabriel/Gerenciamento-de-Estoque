class Produtos:
    def __init__(self, IDProduto, nome, preco, marca):
        self.nome = nome
        self.preco = preco
        self.marca = marca
        self.IDproduto = IDProduto

    def __str__(self):
        return f"(Id: {self.IDproduto} - {self.nome} - R${self.preco} - {self.marca})"


class EstoqueProduto:
    def __init__(self):
        self.estoque = {}

    def adicionar_produto(self, produto):
        if produto.IDproduto in self.estoque:
            print(f"O ID {produto.IDproduto} já existe no estoque.")
        else:
            self.estoque[produto.IDproduto] = produto
            print(f"Produto {produto.nome} adicionado ao estoque.")

    def mostrar_estoque(self):
        if not self.estoque:  
                print("Estoque vazio")
        else:
            for produto in self.estoque.values():  
                print(produto)


    def RemoverProduto(self, IDproduto):
        if IDproduto in self.estoque:
            del self.estoque[IDproduto]
            print(f'Produto com o ID {IDproduto} foi removido')
        else:
            print("produto não está no estoque ")


    def EditarProduto(self, IDproduto, NovoNome=None, NovoPreco=None, NovaMarca=None):
        if IDproduto in self.estoque:
            Produto = self.estoque[IDproduto]
            
            if NovoNome is not None:
                Produto.nome = NovoNome
            
            if NovoPreco is not None:
                Produto.preco = NovoPreco
            
            if NovaMarca is not None:
                Produto.marca = NovaMarca
            
            print(f"Produto com ID {IDproduto} foi atualizado.")
        else:
            print("Produto não encontrado")
    
    def LimparEstoque(self):
        self.estoque.clear()
        print("O estoque foi limpo.")


estoque = EstoqueProduto()


