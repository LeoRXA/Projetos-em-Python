import random
import PySimpleGUI as sg

class Gerador_Dado:
    def __init__(self):
        self.valor_maximo = 6
        self.valor_minimo = 1
        #Layout
        self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button('SIM'), sg.Button('NÃO')]
        ]
    
    def Iniciar(self):
        #criar um janela
        self.janela = sg.Window('Simulador de Dado',layout = self.layout)
        #ler valor na tela
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'SIM' or self.eventos == 's':
                self.Gerar_Valor_Dado()
            elif self.eventos == 'NÃO' or self.eventos == 'n':
                print('Agradecemos sua participação')
            else:
                print('Deve digitar apenas sim ou não')
        except:
            print('Ocorreu um erro inesperado.')
        
    def Gerar_Valor_Dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = Gerador_Dado()
simulador.Iniciar()