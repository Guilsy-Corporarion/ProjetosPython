import math
import random

class jogador:
    def __init__(eu, letra):
        eu.letra = letra


        def get_move( eu, jogo):
            pass 

class RandomComputerPlayer(jogador):
    def __init__(eu, letra):
        super().__init__(letra)

    def get_move(eu, jogo):
        # obter um local válido aleatório para o nosso próximo movimento
        square = random.choice(jogo.avaiable_moves())
        return square

class JogadorHumano(jogador):
    def __init__(eu, letra):
        super().__init__(letra)
    
    def get_move(eu, jogo):
        bola_valida = False
        val = None
        while not bola_valida:
            bola = input(eu.letra + '\'s virar. Movimento de entrada (0-9):')
            # vai verificar que este um valor correto, tentando lançar
            # para um inteiro, e se não é, então dizemos que é inválido
            # é o ponto não é avaliável no conselho, também dizemos que é inválido
            try:
                val = int(square)
                if val not in jogo.movimentos_validos():
                    raise ValueError
                bola_valida = True # se funcionar, ótimo!
            except ValueError:
                print('Bola Errada. Tente novamente.')

        return val
