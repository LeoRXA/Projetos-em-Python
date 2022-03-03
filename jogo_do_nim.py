# Esse é a minha versão do jogo do NIM feito no curso Introdução ao Python do Coursera

class Jogo_Do_NIM:
    def __init__(self, game_start = None):
        self.game_start = str(input('Digite 1 para jogar partida única e 2 para jogar uma competição. '))
        try:
            if self.game_start == '1':
                self.match()
            elif self.game_start == '2':
                self.competition()
            else:
                print('Digite da forma pedida.')
                Jogo_Do_NIM()
        except:
            print('Erro no código !!!')
match = Jogo_Do_NIM()