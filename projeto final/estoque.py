class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.quantidade = 0

    def display(self):
        print("\n"+self.nome,
                "\n -Valor:", self.valor,"R$",
                "\n -Quantidade:", self.quantidade,
                "\n")
    def adicionar(self, qnt):
        self.quantidade += qnt

    def remover(self, qnt):
        if(self.quantidade < qnt):
            raise ValueError("Não foi possivel remover! Quantidade: {}, tentando remover {}.".format(self.quantidade, qnt))
        self.quantidade -= qnt

    
class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionarProduto(self, nome, valor, qnt):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.adicionar(qnt)
                produto.valor = valor
                return produto
        produto = Produto(nome, valor)
        produto.adicionar(qnt)
        self.produtos.append(produto)

    def removerProduto(self, nome, qnt):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.remover(qnt)
                return True
        print("Produto não encontrado.")
        return False

    def encontrarProduto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        raise ValueError("Produto não encontrado.")
        
    
    def display(self):
        print("Produtos")
        for produto in self.produtos:
            produto.display()
