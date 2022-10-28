import math
import random

class jogador:
    def __init__(eu, letra):
        eu.letra = letra


        def get_move( eu, jogo):
            pass 

class JogadorDeComputadorAleatório(jogador):
    def __init__(eu, letra):
        super().__init__(letra)

    def get_move(eu, jogo):
        # obter um local válido aleatório para o nosso próximo movimento
        quadrado = escolha_aleatória(jogo.avaiable_moves())
        return quadrado

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
                val = int(quadrado)
                if val not in jogo.movimentos_validos():
                    raise ValueError
                bola_valida = True # se funcionar, ótimo!
            except ValueError:
                print('Bola Errada. Tente novamente.')

        return val

class JogadorDeComputadorAleatório(jogador):
    def __init__(eu, letra):
        super().__init__(letra)

    def get_move(eu, jogo):
        quadrado = escolha_aleatória(jogo.movimentos_disponíveis())
        return quadrado


class JogadorRoboInteligente(jogador):
    def __init__(eu, letra):
        super().__init__(letra)

    def get_move(eu, jogo):
        if len(jogo.movimentos_disponíveis()) == 9:
            quadrado = escolha_aleatória(jogo.movimentos_disponíveis())
        else:
            quadrado = eu.minimax(jogo, eu.letra)['position']
        return quadrado

    def minimax(eu, state, jogador):
        max_jogador = eu.letra  # youreu
        other_jogador = 'O' if jogador == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_jogador:
            return {'position': None, 'score': 1 * (state.num_empty_quadrados() + 1) if other_jogador == max_jogador else -1 * (
                        state.num_empty_quadrados() + 1)}
        elif not state.empty_quadrados():
            return {'position': None, 'score': 0}

        if jogador == max_jogador:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.movimentos_disponíveis():
            state.make_move(possible_move, jogador)
            sim_score = eu.minimax(state, other_jogador)  # simulate a jogo after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if jogador == max_jogador:  # X is max jogador
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
