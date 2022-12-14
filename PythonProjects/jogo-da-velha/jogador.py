import math
import random


class Jogador():
    def __init__(self, letra):
        self.letra = letra

    def get_move(self, game):
        pass


class HumanJogador(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letra + ', Faça um movimento (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('')
                print('Movimento invalido, tente novamente.')
        return val


class RandomComputerJogador(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerJogador(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letra)['posição']
        return square

    def minimax(self, state, Jogador):
        max_Jogador = self.letra  # você
        other_Jogador = 'O' if Jogador == 'X' else 'X'

        # primeiro queremos verificar se o movimento anterior é um vencedor
        if state.current_winner == other_Jogador:
            return {'posição': None, 'pontos': 1 * (state.num_empty_squares() + 1) if other_Jogador == max_Jogador else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'posição': None, 'pontos': 0}

        if Jogador == max_Jogador:
            best = {'posição': None, 'pontos': -math.inf}  # A cada ponto maximiza
        else:
            best = {'posição': None, 'pontos': math.inf}  # A cada ponto diminui
        for possible_move in state.available_moves():
            state.make_move(possible_move, Jogador)
            sim_pontos = self.minimax(state, other_Jogador)  # simular um jogo depois de fazer esse movimento

            # desfazer um movimento
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_pontos['posição'] = possible_move  # isso representa o movimento ideal para o próximo movimento

            if Jogador == max_Jogador:  # X Jogador máximo
                if sim_pontos['pontos'] > best['pontos']:
                    best = sim_pontos
            else:
                if sim_pontos['pontos'] < best['pontos']:
                    best = sim_pontos
        return best
