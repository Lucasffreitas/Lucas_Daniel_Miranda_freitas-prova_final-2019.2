from agenda import *
from veterinario import *
from estoque import *

class Petshop:

    estoque = Estoque()
    veterinarios = []
    
    def __init__(self):
        self.menu_map = {
            "adicionar_produto": self.adicionar_produto,
            "remover_produto": self.remover_produto,
            "vender_produto": self.vender_produto,
            "mostrar_estoque": self.mostrar_estoque,
            "cadastrar_veterinario": self.cadastrar_veterinario,
            "adicionar_horario": self.adicionar_horario,
            "agendar_horario": self.agendar_horario,
            "mostrar_veterinarios": self.mostrar_veterinarios,
            "quit": self.quit
        }

    def adicionar_produto(self):
        nome = input("Nome do produto: ")
        valor = int(input("Valor: "))
        qnt = int(input("Quantidade: "))
        Petshop.estoque.adicionarProduto(nome, valor, qnt)
        
    def remover_produto(self):
        nome = input("Nome do produto: ")
        qnt = int(input("Quantidade: "))
        Petshop.estoque.removerProduto(nome, qnt)
        
    def vender_produto(self):
        nome = input("Nome do produto: ")
        try:
            produto = Petshop.estoque.encontrarProduto(nome)
        except:
            pass
        else:
            produto.display()
            qnt = int(input("Quantidade: "))
            if qnt > produto.quantidade:
                print("Quantidade excessiva.")
            else:
                valor_total = produto.valor * qnt
                buy = input("Valor total R${}.00\n-Comprar? (y/n)".format(valor_total))
                if(buy == 'y'):
                    Petshop.estoque.removerProduto(nome, qnt)
                    print("Produto comprado!")
                else:
                    print("Compra cancelada.")
                    
        
    def mostrar_estoque(self):
        Petshop.estoque.display()

    def cadastrar_veterinario(self):
        nome = input("Nome do veterinario: ")
        veterinario = Veterinario(nome=nome)
        Petshop.veterinarios.append(veterinario)
        print("Vetenario cadastrado com sucesso!")

    def adicionar_horario(self):
        print("Escolha um veterinario")
        for i, veterinario in enumerate(Petshop.veterinarios):
            print("{} - {}".format(i, veterinario.nome))
        i = int(input("Escolha (n): "))
        try:
            veterinario = Petshop.veterinarios[i]
        except:
            print("Não foi possivel selecionar veterinario")
        else:
            print("Veterinario selecionado")
            veterinario.agenda.adicionarHorario()

    def agendar_horario(self):
        print("Escolha um veterinario")
        for i, veterinario in enumerate(Petshop.veterinarios):
            print("{} - {}".format(i, veterinario.nome))
        i = int(input("Escolha (n): "))
        try:
            veterinario = Petshop.veterinarios[i]
        except:
            print("Não foi possivel selecionar veterinario")
        else:
            print("Veterinario selecionado")
            veterinario.agenda.agendarHorario()

    def mostrar_veterinarios(self):
        print("Veterinarios: ")
        for veterinario in Petshop.veterinarios:
            print(" -{}".format(veterinario.nome))        
    def quit(self):
        raise SystemExit()
    
    def menu(self):
        answer = ""
        while True:
            print("""
            Entre um comando:
            \tadicionar_produto\tAdicionar produto
            \tremover_produto\tRemover produto
            \tvender_produto\tVender produto
            \tmostrar_estoque\tMostrar estoque
            \tcadastrar_veterinario\tCadastra um veterinario
            \tadicionar_horario\tAdiciona horario a um veterinario
            \tagendar_horario\tAgenda horario com um veterinario
            \tmostrar_veterinarios\tMostrar os veterinarios
            \tquit\tSai do Petshop
            """)
            answer = input("entre com um comando: ").lower()
            try:
                func = self.menu_map[answer]
            except KeyError:
                    print("{} não é uma opção válida".format(answer))
            else:
                func()
Petshop().menu()
