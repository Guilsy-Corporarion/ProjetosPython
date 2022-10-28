import math
import timer
from jogador import JogadorHumano, JogadorDeComputadorAleatório, JogadorRoboInteligente


class JogoDaVelha():
    def __init__(eu):
        eu.board = eu.make_board()
        eu.vencedor_atual = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(eu):
        for row in [eu.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(eu, square, letra):
        if eu.board[square] == ' ':
            eu.board[square] = letra
            if eu.winner(square, letra):
                eu.vencedor_atual = letra
            return True
        return False

    def winner(eu, square, letra):
        # check the row
        row_ind = math.floor(square / 3)
        row = eu.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letra for s in row]):
            return True
        col_ind = square % 3
        column = [eu.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letra for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [eu.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letra for s in diagonal1]):
                return True
            diagonal2 = [eu.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letra for s in diagonal2]):
                return True
        return False

    def quadrados_vazios(eu):
        return ' ' in eu.board

    def num_quadrados_vazios(eu):
        return eu.board.count(' ')

    def available_moves(eu):
        return [i for i, x in enumerate(eu.board) if x == " "]


def play(jogo, x_jogador, o_jogador, imprimir_jogo=True):

    if imprimir_jogo:
        jogo.print_board_nums()

    letra = 'X'
    while jogo.quadrados_vazios():
        if letra == 'O':
            square = o_jogador.get_move(jogo)
        else:
            square = x_jogador.get_move(jogo)
        if jogo.make_move(square, letra):

            if imprimir_jogo:
                print(letra + ' fazer movimento para quadradi {}'.format(square))
                jogo.print_board()
                print('')

            if jogo.vencedor_atual:
                if imprimir_jogo:
                    print(letra + ' vitória!')
                return letra  # ends the loop and exits the jogo
            letra = 'O' if letra == 'X' else 'X'  # switches jogador

        time.sleep(.8)

    if imprimir_jogo:
        print('É uma gravata!')



if __name__ == '__main__':
    x_jogador = JogadorRoboInteligente('X')
    o_jogador = JogadorHumano('O')
    t = JogodaVelha()
    play(t, x_jogador, o_jogador, imprimir_jogo=True)
