from agenda import *
from veterinario import *
from estoque import *
        
veterinario = Veterinario("Lucas")

veterinario.agenda.adicionarHorario(Horario(8, "seg"))
veterinario.agenda.adicionarHorario(Horario(10, "ter"))
veterinario.agenda.adicionarHorario(Horario(22, "seg"))

veterinario.agenda.prompt()


estoque = Estoque()
estoque.adicionarProduto("Shampoo pra lucas", 10, 50)
estoque.adicionarProduto("Shampoo pra lucas", 15, 50)
estoque.adicionarProduto("Condicionar", 20, 5)
estoque.removerProduto("Condicionar", 4)
estoque.prompt()
