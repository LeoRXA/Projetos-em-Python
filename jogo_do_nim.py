# Esse é a minha versão do jogo do NIM feito no curso Introdução ao Python do Coursera

class Jogo_Do_NIM:
    def __init__(self, game_start = None):
        self.game_start = str(input('Digite 1 para jogar partida única e 2 para jogar uma competição. '))
        try:
            if self.game_start == '1':
                self.choose_parts()
            elif self.game_start == '2':
                self.competition()
            else:
                print('Digite da forma pedida.')
                Jogo_Do_NIM()
        except:
            print('Erro no código !!!')
    

    def choose_parts(self):
        # Essa função será resposável por receber o números de jogadas e o limite da mesma.

        self.parts = int(input('Quantas peças? '))
        self.parts_limit = int(input("Limite de peças por jogada? "))

        while self.parts < 1:
            print("Ops! O número de jogadas deve ser maior que 0")
            parts = int(input("Quantas peças? "))
        while self.parts_limit >= self.parts:
            print('O limite de peças deve ser menor que o número de peças.')
            self.parts_limit = int(input("Limite de peças por jogada? "))
        print(" ")
        self.decision_match()


    def decision_match(self):
        # Essa função será responsável por definir quem começa o jogador ou o computador
        for i in range(1, 10):
            if (self.parts_limit + 1)* i == self.parts:
                # Caso o jogador comece
                self.comp_start = False
                self.user_start = True
                break
                
            else:
                # Caso o computador comece
                self.comp_start = True
                self.user_start = False

        if self.comp_start == True and self.user_start == False:
            print("Computador começa!")
            print(" ")
            self.comp_choose_play()
        else:
            print("Você começa!")
            print(" ")
            self.user_choose_play()

    def user_choose_play(self):
        self.retired_parts = int(input("Quantas peças você vai tirar? "))
        print('')
        if self.retired_parts > self.parts_limit or self.removed_parts <= 0:
            print('Você deve tirar apenas o limite de peças permitido.')
            print('')
            self.user_choose_play()
        return self.removed_parts

    def comp_choose_play(self):
        if self.parts > self.parts_limit:
            for multiply in range(0, 100):
                if (self.parts_limit + 1) * multiply < self.parts:
                    print(self.parts_limit)
                    return self.parts_limit
                elif (self.parts_limit + 1) * multiply == self.parts:
                    print(self.parts)
                    return self.parts
                else:
                    print(self.parts - self.parts_limit)
                    return self.parts - self.parts_limit

match = Jogo_Do_NIM()