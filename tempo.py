class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0

    def __str__ (self):
        if self.horas >= 0 and self.horas<=9:
            return f"SÃO {self.horas:02d} HORAS E {self.minutos:02d} MINUTOS DA MANHÃ.\n"
        elif self.horas >=12 and self.horas<17:
            return f"SÃO {self.horas:02d} HORAS E {self.minutos:02d} MINUTOS DA TARDE.\n"
        elif self.horas >=17 and self.horas<24:
            return f"SÃO {self.horas:02d} HORAS E {self.minutos:02d} MINUTOS DA NOITE.\n"
    def verHoras (self):
        if self.horas >= 0 and self.horas<=9:
            return f"SÃO {self.horas:02d} HORAS E {self.minutos:02d} MINUTOS DA MANHÃ.\n"
        elif self.horas >=12 and self.horas<17:
            return f"SÃO {self.horas:02d} HORAS E {self.minutos:02d} MINUTOS DA TARDE.\n"
        elif self.horas >=17 and self.horas<24:
            return f"SÃO {self.horas:02d} HORAS E {self.minutos:02d} MINUTOS DA NOITE.\n"


    def timeRun (self):
        self.minutos+=10
        if self.minutos == 60:
            self.horas+=1
            self.minutos = 0
        elif self.minutos > 60:
            soma = self.minutos - 60
            self.horas +=1
            self.minutos = soma
    def timeHoras (self):
        self.horas += 1
        self.minutos = 0
        if self.minutos == 60:
            self.horas+=1
            self.minutos = 0
        elif self.minutos > 60:
            soma = self.minutos - 60
            self.horas +=1
            self.minutos = soma

    def meiaHora(self):
        self.minutos+=30
        if self.minutos == 60:
            self.horas+=1
            self.minutos = 0
        
        elif self.minutos > 60:
            soma = self.minutos - 60
            self.horas +=1
            self.minutos = soma
    def timeTurno(self):
        self.horas+=5
        if self.minutos == 60:
            self.horas+=1
            self.minutos = 0
        elif self.minutos > 60:
            soma = self.minutos - 60
            self.horas +=1
            self.minutos = soma
        
        
