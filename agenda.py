class Horario:
    def __init__(self, hora, dia):
        self.hora = hora
        self.dia = dia

class Agenda:
    def __init__(self):
        self.horarios_agendados = []

    def adicionarHorario(self, horario):
        self.horarios_agendados.append(horario)

    def prompt(self):
        for horario in self.horarios_agendados:
            print(horario.hora, horario.dia)
