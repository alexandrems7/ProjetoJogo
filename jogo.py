import os
os.system('cls' if os.name == 'nt' else 'clear')
from personagem import Personagem
from tempo import Relogio
from personagem import Academia
from time import sleep
personagem = Personagem()
academia = Academia()
relogio = Relogio()
#Alteração do arquivo

if(__name__ == "__main__"):
    while True:
        if personagem.dormir == True:
            print('='*50)
            print('Olá, bom dia!\n')
            print(relogio)
            print(personagem)
            print(f'\nVAMOS ACORDÁ-LO?')
            print('='*50)
            print('''
            DIGITE A OPCAO DESEJADA

            [ 1 ] - Acordar
            [ 2 ] - Continuar dormindo
            ''')
            resp = int(input('OPÇÃO SELECIONADA:  '))
          
            
            if resp == 1:
                

                print(f'Olha só quem acordou!\n')
                while True:
                    personagem.dormir = False
                    print('='*50)
                    print(f'\n{relogio}\n')
                    
                    print(personagem)
                    print('='*50)
                    print('''
                    DIGITE A OPCAO DESEJADA

                    [ 1 ] - Tomar banho / Escovar dentes
                    [ 2 ] - Fazer café
                    [ 3 ] - Comprar café
                    [ 4 ] - Tomar remédios
                    [ 5 ] - Ir trabalhar
                    ''')
                    resp = int(input('OPÇÃO SELECIONADA:  '))
                    while True:
                        if resp == 1:
                            relogio.timeRun()
                            personagem.tomarBanho()
                            break
                        elif resp == 2:
                            relogio.timeRun()
                            personagem.tomarCafe()
                            break
                        elif resp == 3:
                            relogio.timeRun()
                            print('O seu café custou R$ 10,00 reais')
                            personagem.dinheiro-=10
                            print('\nQUE CAFÉ DELICIOSO!')
                            break
                        elif resp == 4:
                            relogio.timeRun()
                            personagem.tomarRemedios()
                            break
                        elif resp == 5:
                            personagem.recebeSalario()
                            for r in range(3):
                                relogio.timeRun()                          
                            
                            print('Bem vindo ao trabalho!')
                           
                            print('Você é um Analista de Sistemas do Google')
                        
                            print('Hoje precisa terminar um programinha para a empresa')
                    
                            print('Curtiu? kkkkkk')
                     
                            print('Então, bata o cartão, se não vai dar BO.')
                
                            print(relogio)
                  
                            print('''
                            VOCÊ DESEJA BATER O CARTÃO?
                               
                            [ 1 ] - SIM
                            [ 2 ] - AINDA NÃO
                            ''')
                            while (resp != 1) and (resp != 2):
                                resp = int(input('OPÇÃO SELECIONADA:  '))
                                if (resp != 1) and (resp != 2):
                                    print('Opção inválida!')
                            if resp == 2:
                                break

                            
                                
                        else:
                            print('Opção inválida!')
                            break
                              
                        if resp == 1:
                            if ((relogio.horas == 6) and (relogio.minutos < 50) ):
                                print('Ainda está muito cedo! Você vai precisar aguardar um pouco.')
                                break
                            elif ((relogio.horas == 6) and (relogio.minutos >= 50) and (relogio.minutos <= 59)):
                                print('Bem na hora! Por pouco você se atrasa!')
                                print('Mas deu tudo certo!')
                                sleep(1)
                            elif ((relogio.horas == 7) and (relogio.minutos == 0)):
                                print('Você chegou bem na hora!')
                                sleep(1)
                            elif ((relogio.horas == 7) and (relogio.minutos > 0) and (relogio.minutos <= 10)):
                                print('Você chegou um pouco encima da hora, hein! Tome cuidado com isso!')
                                sleep(1)
                            elif ((relogio.horas == 7) and (relogio.minutos > 10) and (relogio.minutos <= 50)):
                                print('Você chegou muuuuiiiittto atrasado. Se continuar assim vai ser demitido.')
                                sleep(1)
                            elif(relogio.horas>=8):
                                print('Você viu as horas?')
                                print('Assim não dá, né! Vai haver um desconto no seu salário, viu!')
                                sleep(2)
                                personagem.punido()
                                
                  
                            
                
                            print('Agora chega de enrolação e... mãos à obra!')
                            relogio.timeTurno()
           
                            n1 = 1010101010101010101001010
                            n2 = 1101010111101000010101000
                            print('Trabalhando...\n')
                            sleep(1)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print(n1)
                            sleep(0.2)
                            print(n2)
                            sleep(0.2)
                            print('Ufa!')
                   
                            print('Você fez 1500 linhas de código.')
        
                            print('Você é mesmo o cara, hein!')
                            print()
                            if ((personagem.higiene == False) and (personagem.lanchar_comer == False)):
                                    print('Você foi trabalhar sujo e com fome')
                                    personagem.salario *= 0.1
                            elif (personagem.higiene == False):
                                    print("Como você estava sujo, você levou uma advertência.")
                                    personagem.salario *= 0.5
                            elif (personagem.lanchar_comer == False):
                                    print("Como você estava com fome, você não rendeu o esperado.")
                                    personagem.salario *= 0.3
                            elif (personagem.punicao == True):
                                print('Como você chego depois das 8 perderá 30 reais em seu salário.')
                                
                            print(f'Você recebeu {personagem.salario:.2f} reais pelo seu trabalho hoje.')
                            print()                       
                            print(personagem)
                            print(relogio.verHoras())
                            print('''
                                VAMOS PRA CASA?
                                
                                [ 1 ] - SIM
                                [ 2 ] - AINDA NÃO
                                ''')
                            resp = int(input('OPÇÃO SELECIONADA:  '))
                            while resp == 2:
                                resp = int(input('OPÇÃO SELECIONADA:  '))
                                relogio.timeRun()
                                print(relogio)
                                print('É melhor ir pra casa!')

                            if resp == 1:
                                while True:
                                    for r in range(3):
                                        relogio.timeRun()
                                    print(relogio)
                                    print(personagem)
                                    print('''
                                        VOCÊ ESTÁ EM CASA
                                        o que deseja fazer agora?
                                        
                                        [ 1 ] - Almoçar
                                        [ 2 ] - Tirar uma soneca
                                        ''')
                                    resp = int(input('OPÇÃO SELECIONADA:  '))
                                    if resp == 1:
                                        while True:
                                            print(f'Você possui R$ {personagem.dinheiro} reais')
                                            print('''
                                                OPÇÕES DE ALMOÇO
                                            
                                                [ 1 ] - Almoçar em casa
                                                [ 2 ] - Comprar comida
                                                ''')
                                            resp = int(input('OPÇÃO SELECIONADA:  '))
                                            if resp == 1:
                                                personagem.almocar1()
                                                break            
                                            elif resp == 2:
                                                personagem.almocarFora()
                                                break
                                    elif resp == 2:
                                        print(relogio)
                                        personagem.tirarSoneca()
                                        relogio.timeHoras()
                                        sleep(2)
                                        print(personagem)
                                        print()
                                        print('Opa! Boa tarde!')
                                    
                                        print('Dormiu bem?')
                                        print('Temos a tarde inteira pela frente ainda!')
                                        print('Que tal escolher entre as opções abaixo!?')
                                        

                                        while True:
                                            if relogio.horas < 22:
                                                print(personagem)
                                            elif relogio.horas > 22:
                                                pass
                                                print(personagem)

                                            relogio.verHoras()
                                            print(f'''
                                            SÃO: {relogio.verHoras()}

                                            VOCÊ ESTÁ EM CASA
                                            o que deseja fazer agora?

                                                
                                            [ 1 ] - Tirar uma soneca
                                            [ 2 ] - Ir à academia
                                            [ 3 ] - Praticar esportes
                                            [ 4 ] - opções de lazer
                                            [ 5 ] - Fazer tarefas da escola
                                            [ 6 ] - Tomar o café da tarde
                                            [ 7 ] - Curso Blue Edtech (A partir das 19h)
                                            [ 8 ] - Jantar
                                            [ 9 ] -             IR DORMIR
                                            ''')
                                            resp = int(input('OPÇÃO SELECIONADA:  '))
                                            if resp == 1:
                                                personagem.tirarSoneca()
                                                relogio.timeHoras()
                                                sleep(2)
                                                print()
                                            elif resp == 2:
                                                print('Isso aí, vamos malhar!')
                                                print('A diária da academia são R$ 10,00 reais')
                                                print(f'Você possui R$ {personagem.dinheiro} reais')
                                                print('Você tem vários aparelhos para usar, mas só pode ir em QUATRO POR DIA.')
                                                if personagem.dinheiro>=10:
                                                    voltas = 4
                                                    if voltas < 0:
                                                        voltas = 0
                                                    while True:
                                                        print(relogio)
                                                        if voltas == 0:
                                                            print('Hora de ir pra casa!')
                                                        if academia.aparelhos <= 0:
                                                            academia.aparelhos*=0

                                                        print(f'''
                                                        ESCOLHA UM APARELHO
                                                        --> Você ainda tem {academia.aparelhos} aparelhos para utilizar <--
                                                            
                                                        [ 1 ] - Esteira
                                                        [ 2 ] - Estação de musculação
                                                        [ 3 ] - Bicicleta
                                                        [ 4 ] - Eliptico
                                                        [ 5 ] - Cardio Wave
                                                        [ 6 ] - Voltar para casa
                                                        ''')
                                                        voltas-=1
                                                        resp = int(input('OPÇÃO SELECIONADA:  '))
                                                        
                                                        if resp == 1:
                                                            academia.ir_na_esteira()
                                                            relogio.meiaHora()

                                                            print(academia)
                                                        elif resp == 2:
                                                            academia.ir_na_estação_de_musculação()
                                                            relogio.meiaHora()

                                                            print(academia)
                                                        elif resp == 3:
                                                            academia.ir_na_bicicleta()
                                                            relogio.meiaHora()

                                                            print(academia)
                                                        elif resp == 4:
                                                            academia.ir_no_aparelho_eliptico()
                                                            relogio.meiaHora()

                                                            print(academia)
                                                        elif resp == 5:
                                                            academia.ir_no_cardio_wave()
                                                            relogio.meiaHora()

                                                            print(academia)
                                                        elif resp == 6:
                                                            break
                                                elif personagem.dinheiro < 10:
                                                    print('Você não tem dinhiro para ir à academia. Tente novamente amanhã.')
                                            elif resp == 3:
                                                print('Isso aí! Praticar esportes é muito bom para a saúde.')
                                                partidasf = 0
                                                partidasn = 0
                                                partidasc = 0
                                                cavalgadas = 0
                                                carro = 1
                                                while True:
                                                    print(relogio)
                                                    print(f'''
                                                    ESPORTES
                                                        
                                                    [ 1 ] - Futebol
                                                    [ 2 ] - Natação
                                                    [ 3 ] - Corrida
                                                    [ 4 ] - Cavalgar
                                                    [ 5 ] - Stock Car
                                                    [ 6 ] - Voltar para casa
                                                    ''')
                                                    resp = int(input('OPÇÃO SELECIONADA:  '))
                                                    if resp == 1:
                                                        partidasf +=1
                                                        
                                                        print(f'Você jogou {partidasf} partidas de futebol')
                                                        relogio.meiaHora()
                                                    elif resp == 2:
                                                        partidasn += 1
                                                        print(f'Você praticou natação {partidasn} vez')
                                                        relogio.meiaHora()
                                                    elif resp == 3:
                                                        partidasc += 1
                                                        print(f'Você correu {partidasc} volta')
                                                        relogio.timeRun()
                                                    elif resp == 4:
                                                        cavalgadas += 1
                                                        print(f'Você cavalgou {cavalgadas} vez.')
                                                        relogio.meiaHora()
                                                    elif resp == 5: 
                                                        carro += 1
                                                        print(f'Você andou {carro} volta de carro.')
                                                        relogio.meiaHora()
                                                    elif resp == 6:
                                                        break
                                            elif resp == 4:
                                                print(relogio)
                                                print(f'''
                                                OPÇÕES DE LAZER
                                                        
                                                [ 1 ] - Ir ao cinema
                                                [ 2 ] - Ir ao parque
                                                [ 3 ] - Visitar a família
                                                [ 4 ] - Meditar
                                                [ 6 ] - Voltar pra casa
                                                ''')
                                                resp = int(input('OPÇÃO SELECIONADA:  '))
                                                if resp == 1:
                                                    while True:
                                                        print(f'Você possui R$ {personagem.dinheiro} reais')
                                                        print(relogio)
                                                        print('''
                                                        OLHA SÓ OS FILMES QUE ESTÃO EM CARTAZ!

                                                        [ 1 ] Minha mãe é uma peça 3  (Valor do ingresso: R$ 20,00)
                                                        [ 2 ] Raya e o último dragão  (Valor do ingresso: R$ 10,00)
                                                        [ 3 ] The woman in the window (Valor do ingresso: R$ 15,00)
                                                        [ 4 ] Voltar para casa
                                                        ''')
                                                        resp = int(input('FILME ESCOLHIDO:  '))
                                                        if resp == 1:
                                                            if personagem.dinheiro >= 20:
                                                                print('Você viu o filme: Minha mãe é uma peça 3')
                                                                relogio.timeHoras()
                                                                relogio.timeHoras()
                                                                personagem.dinheiro -= 20
                                                            elif personagem.dinheiro < 20:
                                                                print('Você não possui dinheiro o suficiente. Tente assistir a outro filme.')
                                                        elif resp == 2:
                                                            if personagem.dinheiro >= 10:
                                                                print('Você assistiu ao filme: Raya e o último dragão')
                                                                relogio.timeHoras()
                                                                relogio.timeHoras()
                                                                personagem.dinheiro -= 10
                                                            elif personagem.dinheiro < 10:
                                                                print('Você não possui dinheiro o suficiente. Tente assistir a outro filme.')
                                                        elif resp == 3:
                                                            if personagem.dinheiro >= 15:
                                                                print('Você assistiu ao filme: The woman in the window')
                                                                relogio.timeHoras()
                                                                relogio.timeHoras()
                                                                personagem.dinheiro -= 15
                                                            elif personagem.dinheiro < 15:
                                                                print('Você não possui dinheiro o suficiente. Tente assistir a outro filme.')
                                                        if resp == 4:
                                                            break
                                                elif resp == 4:
                                                    print('Ótima escolha!')
                                                    sleep(1)
                                                    print('A meditação faz muito bem pra gente!')
                                                    sleep(1)
                                                    relogio.timeHoras()

                                                elif resp == 2:
                                                    print('Isso aí!')
                                                    print('Você foi passear no parque')
                                                    print('o contato com a natureza faz muito bem pra gente!')
                                                    relogio.timeHoras()
                                                elif resp == 3:
                                                    while True: 
                                                        print(relogio)
                                                        print('''
                                                        QUEM VOCÊ DESEJA VISITAR?
                                                        [ 1 ] Seus pais
                                                        [ 2 ] Sua irmã
                                                        [ 3 ] Seu irmão
                                                        [ 4 ] Seu melhor amigo
                                                        [ 5 ] Permanecer em casa
                                                        ''')
                                                        resp = int(input('LAZER ESCOLHIDO:  '))
                                                        if resp == 1:
                                                            print('Parabéns! Devemos sempre visitar nossos pais!')
                                                            print('Eles ficaram muito felizes com sua visita')
                                                            relogio.timeHoras()
                                                        elif resp == 2:
                                                            print('Isso aí!')
                                                            print('Você acaba de visitar a sua irmã.')
                                                            print('Ela ficou muito feliz em vê-lo.')
                                                            relogio.timeHoras()
                                                        elif resp == 3:
                                                            print('Isso aí!')
                                                            print('Você acaba de visitar o seu irmão.')
                                                            print('Ele ficou muito feliz em vê-lo.')
                                                            relogio.timeHoras()
                                                        elif resp == 4:
                                                            print('Isso aí!')
                                                            print('Você acaba de visitar o seu melhor amigo.')
                                                            print('Ele ficou muito feliz em vê-lo.')
                                                            relogio.timeHoras()
                                                        elif resp == 5:
                                                            break
                                            elif resp == 5:
                                                print('Isso aí!!!')
                                                print('Você acaba de fazer as atividades que o Professor Thiago deixou para casa.')
                                                print('Ele vai ficar muito feliz')
                                                relogio.meiaHora()
                                            elif resp == 6:
                                                while True:
                                                    print(f'Você possui R$ {personagem.dinheiro} reais')
                                                    print(f'O café completo na padaria custa R$ 10,00 reais')
                                                    print('''
                                                    VOCÊ DESEJA
                                                    [ 1 ] Comprar café na padaria
                                                    [ 2 ] Fazer café em casa
                                                    [ 3 ] Voltar
                                                    ''')
                                                    resp = int(input('OPÇÃO ESCOLHIDA:  '))
                                                    if resp == 1:
                                                        if personagem.dinheiro >= 10:
                                                            personagem.dinheiro -= 10
                                                            print('O café estava mesmo delicioso!')
                                                            relogio.timeRun()
                                                            break
                                                            
                                                        elif personagem.dinheiro < 10:
                                                            print(f'Você não tem dinheiro o suficiente para pagar o café.')
                                                            print(f'O café custa R$ 10,00 reais e você possui {personagem.dinheiro}')
                                                    elif resp == 2:
                                                        personagem.dispensa -= 1
                                                        relogio.timeRun()
                                                        print('Você preparou um café muito bom, hein! Parabéns!!!')
                                                        break
                                                    if resp == 3:
                                                        break
                                            elif resp == 7:
                                                if relogio.horas >= 19:
                                                    if (relogio.horas >= 19) and (relogio.minutos <= 10):
                                                        print('Professor Vini: -Seja muito bem vido!')
                                                        sleep(1)
                                                        print('Professor Thiago: -A aula de hoje está cheia de conteúdo novo!')
                                                        sleep(1)
                                                        print('Bora lá, então!?')
                                                        print('Estudando.')
                                                        sleep(0.5)
                                                        print('Estudando..')
                                                        sleep(0.5)
                                                        print('Estudando...')
                                                        sleep(0.5)
                                                        print('Estudando....')
                                                        sleep(0.5)
                                                        print('Hora do intervalo')
                                                        sleep(0.5)
                                                        print('Estudando.')
                                                        sleep(0.5)
                                                        print('Estudando..')
                                                        sleep(0.5)
                                                    elif (relogio.horas >= 19) and (relogio.minutos > 10):
                                                    
                                                        print('Professor Thiago: -Olha só, você chegou muito atrasado!')
                                                        sleep(2)
                                                        print('Professor Vini: -Vai ter que assistir a gravação do momento que perdeu até aqui, no portal!')
                                                        sleep(2)
                                                        print('Professor Thiago: E já perdeu o pool também! Não deixa isso acontecer amanhã.')
                                                        sleep(1)
                                                        print('Bora pra aula!')
                                                        sleep(0.5)
                                                        print('Estudando.')
                                                        sleep(0.5)
                                                        print('Estudando..')
                                                        sleep(0.5)
                                                        print('Estudando...')
                                                        sleep(0.5)
                                                        print('Estudando....')
                                                        sleep(0.5)
                                                        print('Hora do intervalo')
                                                        sleep(0.5)
                                                        print('Estudando.')
                                                        sleep(0.5)
                                                        print('Estudando..')
                                                        sleep(0.5)
                                                    print()



                                                    relogio.timeHoras()
                                                    relogio.timeHoras()
                                                    relogio.timeHoras()
                                                    relogio.timeHoras()
                                                    print('Nossa, acabou muito rápido!')
                                                    sleep(1)
                                                    print('O curso de hoje estava ótimo, hein!')
                                                    sleep(1)
                                                    print('Aprendemos sobre listas, tuplas e dicionários')
                                                    sleep(1)
                                                    print('Agora é só refazers os exercícios para apreender tudo.\n')
                                                    sleep(1)
                                                    personagem.refeicao = False
                                                    personagem.soneca = False

                                                    


                                                elif relogio.horas<19:
                                                    print('Ainda não está na hora do curso.')
                                                    sleep(0.5)
                                                    print('o professor Thiago ainda não está na sala, então não tem como você entrar.')
                                                    sleep(1)
                                                    print('Tente novamente à partir das 19 horas')
                                                    sleep(1)
                                            elif resp == 8:
                                                if relogio.horas >= 17:
                                                    relogio.timeRun()
                                                    personagem.refeicao = True
                                                    personagem.soneca = False
                                                    print('Bora jantar!?')
                                                    sleep(1)
                                                    print('Hum.... Tem um escondidinho de carne na geladeira, vai ser ele mesmo!')
                                                    sleep(1)
                                                    print('que jantar delicioso!')
                                                    sleep(2)
                                                    


                                                if relogio.horas < 23:
                                                    print('Ah, para!')
                                                    print('Você ainda não está com fome, vai! kkkk')
                                                    sleep(2)
                                        
                                            elif resp == 9:
                                                if relogio.horas >= 23 and personagem.refeicao == True:
                                                    personagem.refeicao = True
                                                    personagem.soneca = True
                                                    print('Nossa, o dia hoje foi maravilhoso!')
                                                    sleep(1)
                                                    print('Deu pra fazer muita coisa boa.')
                                                    sleep(1)
                                                    print('Ahhhhhhh, que sono!')
                                                    sleep(1)
                                                    print('Boa noite!')
                                                    sleep(1)
                                                    print('Até amanhã!')
                                                    sleep(1)
                                                    print('''

                                                    ===========         =           =            =
                                                    =                   =           =  =      =  =
                                                    =                   =           =    =  =    =
                                                    ===========         =           =     =      =
                                                    =                   =           =            =    
                                                    =                   =           =            = 
                                                    =                   =           =            =


                                                    ''')
                                                    quit()
                                                elif relogio.horas < 23:
                                                    print('Ops! ')
                                                    print('Você ainda não está com sono e você precisa estudar até as 23.')
                                                    print('Então...')
                                                    print('Vê se para de preguiça e vai fazer alguma coisa que não seja dormir. kkkkk')
                                                elif relogio.horas >= 23 and personagem.refeicao == False:
                                                    print('Você está com muita fome para dormir.')
                                                    sleep(1)
                                                    print('Jante primeiro.')
                                                    sleep(0.5)

            if resp == 2:
                relogio.timeRun()
                print('Que pena! Tome cuidado, você pode perder a hora, hein!')
                print('Vou te dar dez segundos pra acordar, tá!?')
                sleep(2)
                for cont in range(1,10):
                    print(cont)
                    sleep(0.6)
            else:
                print('Opção inválida!')