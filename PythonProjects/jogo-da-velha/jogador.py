import math
import random

class jogador:
    def __init__(self, letter):
        self.letter = letter


        def get_move( self, game):
            pass 

class RandomComputerPlayer(jogador):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # obter um local válido aleatório para o nosso próximo movimento
        square = random.choice(game.avaiable_moves())
        return square

class JogadorHumano(jogador):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s virar. Movimento de entrada (0-9):')
            # vai verificar que este um valor correto, tentando lançar
            # para um inteiro, e se não é, então dizemos que é inválido
            # é o ponto não é avaliável no conselho, também dizemos que é inválido
            try:
                val = int(square)
                if val not in game.avaiable_moves():
                    raise ValueError
                valid_square = True # se funcionar, ótimo!
            except ValueError:
                print('Bola Errada. Tente novamente.')

        return val
