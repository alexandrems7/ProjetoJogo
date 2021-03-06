from tempo import Relogio
relogio = Relogio()
class Personagem:
    def __init__(self):
        self.dormir = True
        self.lanchar_comer = False
        self.higiene = False
        self.saude = False
        self.dinheiro = 50
        self.dispensa = 5
        self.refeicao = False
        self.salario = 0
        self.soneca = False
        self.punicao = False
        self.jantar = True
        self.dormir = True

    
    def __str__(self):
        if (self.lanchar_comer == False ) or (self.higiene == False) or (self.saude==False):
            return f"O personagem está:"+(" dormindo" if self.dormir else " acordado")+", "+("sujo" if self.higiene == False else "limpo")+", "+("\ncom fome" if self.lanchar_comer == False else "\nalimentado")+" "+("e precisando tomar seus remédios" if self.saude == False else "e já tomou seus remédios")+"."
        elif (self.lanchar_comer == True) and (self.higiene == True) and (self.saude==True) and (self.dinheiro==50):
            return f"O personagem está"+(" dormindo" if self.dormir else " acordado")+", "+("sujo" if self.higiene == False else "limpo")+", "+("\ncom fome" if self.lanchar_comer == False else "\nalimentado")+" "+("e precisando tomar seus remédios" if self.saude == False else "e já tomou seus remédios")+"."+"\n\nTUDO CERTINHO, NÉ!\nENTÃO, BORA TRABALHAR! É SÓ SELECIONAR A OPÇÃO 5."
        elif (self.lanchar_comer == True) and (self.higiene == True) and (self.saude==True) and (self.dinheiro>50) and (self.refeicao == False and self.soneca == False):
            return f"O personagem está"+(" querendo FAZER SUA REFEIÇÃO" if self.refeicao == False else " sem fome.")+(" e querendo dormir." if self.soneca == False else " ")
        elif (self.lanchar_comer == True) and (self.higiene == True) and (self.saude==True) and (self.dinheiro>50) and (self.refeicao == True): 
            return f"O personagem está"+(" querendo FAZER SUA REFEIÇÃO" if self.refeicao == False else " sem fome")+" e "+("querendo descansar/dormir" if self.soneca == False else " e descansado.")
       

            
        

    
    def tomarCafe(self):
        self.dispensa -= 1
        self.lanchar_comer = True
    def tomarRemedios(self):
        self.saude = True
    def tomarBanho(self):
        self.higiene = True
    def recebeSalario(self):
        self.salario = 100
        self.dinheiro += 100
    def almocar1(self):
        self.refeicao = True
        self.dispensa-=1
    def almocarFora(self):
        self.dinheiro -= 20
        self.refeicao = True
    def tirarSoneca(self):
        self.soneca = True

    def punido(self):
        self.punicao = True
        self.salario -= 30

class Trabalho:
    def __init__(self, trabalhar = False):
        self.trabalhar = trabalhar

class Academia:
    def __init__ (self):
        self.esteira = False
        self.estação_de_musculação = False
        self.bicicleta = False
        self.aparelho_eliptico = False
        self.cardio_wave = False
        self.aparelhos = 4


    
    def __str__(self):
        return f"\nVOCÊ FOI EM:\n"+("--> na Esteira" if self.esteira==True else " ")+("\n--> na Estação de Musculação" if self.estação_de_musculação == True else " " )+("\n--> na Bicicleta" if self.bicicleta == True else " ")+("\n--> no Aparelho Eliptico" if self.aparelho_eliptico == True else " ")+("\n--> no Cardio Wave" if self.cardio_wave == True else " ")
 
    def ir_na_esteira(self):
        self.esteira = True
        self.aparelhos -= 1
        if self.aparelhos == 0:
            self.aparelhos = 0

    def ir_na_estação_de_musculação(self):
        self.estação_de_musculação = True
        self.aparelhos -= 1
        if self.aparelhos == 0:
            self.aparelhos = 0

    def ir_na_bicicleta(self):
        self.bicicleta = True
        self.aparelhos -= 1
        if self.aparelhos == 0:
            self.aparelhos = 0

    def ir_no_aparelho_eliptico(self):
        self.aparelho_eliptico = True
        self.aparelhos -= 1
        if self.aparelhos == 0:
            self.aparelhos = 0

    def ir_no_cardio_wave(self):
        self.cardio_wave = True
        self.aparelhos -= 1
        if self.aparelhos == 0:
            self.aparelhos = 0






