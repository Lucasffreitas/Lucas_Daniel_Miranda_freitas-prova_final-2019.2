class Horario:
    def __init__(self, hora, dia):
        self.hora = hora
        self.dia = dia

class Agenda:
    def __init__(self):
        self.horarios = []
        self.horarios_agendados = []

    def adicionarHorario(self):
        dia = input("Dia da semana: ")
        hora = int(input("Horas: "))
        horario = Horario(hora, dia)
        self.horarios.append(horario)

    def agendarHorario(self):
        for i, horario in enumerate(self.horarios):
            print("*{}. {} - {}h".format(i, horario.dia, horario.hora))
        i = int(input("Escolha (n): "))
        try:
            self.horarios_agendados.append(horarios[i])
            self.horarios.remove(horarios[i])
        except:
            print("Não foi possivel agendar horario")
        else:
            print("Horario agendado com sucesso!")
        

    def display(self):
        for horario in self.horarios_agendados:
            print(horario.hora, horario.dia)
