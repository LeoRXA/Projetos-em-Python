import random
import PySimpleGUI as sg
def resposta_usuario(m=0, t='não'):
    if m == 0:
        n = str(input("Você gostaria de jogar o dado? "))
        resultado = Jogo_do_Dado(n)
    if m == 1:
        n = str(input("Você gostaria de jogar o dado? "))
        resultado = Jogo_do_Dado(n)
class Jogo_do_Dado:
    def __init__(self,n):
        self.n = n
        #Layout
        layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
        #Criar uma janela
        janela = sg.Window('Simulador de Dado',Layout=layout)
        #ler o valores da tela
        self.n, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        while True:
            lista_n = ["nao",'no','não', 'n','negativo','Negativo','Nao','No','Não','NAO','NÃO','NEGATIVO','N']
            lista_s = ['sim', 'yes', 's', 'positivo', 'Positivo', 'Sim', 'SIM', 'POSITIVO', 'S', 'YES', 'Yes']
            try:
                for i in lista_s:
                    if n == i:
                        self.valor_dado = int(input("Jogue o dado: "))
                        self.dado_resultado = self.jogar_dado()
                        if self.dado_resultado == True:
                            print("Você acertou o resultado. Tente novamente :)")
                            print("")
                            return resposta_usuario(1)
                        else:
                            print("Ops! Você errou o resultado. Tente novamente :)")
                            print("")
                            return resposta_usuario(1)
                for j in lista_n:
                    if n == j:
                        print("Okay, até a próxima!")
                        return resposta_usuario(2, 'não')
                else:
                    self.resposta_errada()
            except:
                print('Ocorreu um erro no jogo!')
    def jogar_dado(self):
        if self.valor_dado >= 1 and self.valor_dado <= 6:
            self.dado = random.randint(1,6)
            if self.dado == self.valor_dado:
                return True
            else:
                return False
        else:
            print("O dado tem apenas de 1 a 6, tente novamente")
            self.valor_dado = int(input("Jogue o dado: "))
            self.dado_resultado = self.jogar_dado()
    def resposta_errada(self):
        print("Resposta inválida, tente novamente.")
        print("")
        resposta_usuario()
resposta_usuario()
