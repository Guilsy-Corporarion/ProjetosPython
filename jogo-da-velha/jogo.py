class JogodaVelha:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # única lista para substituir 3x3
        self.current_winner = None #manter o controle do vencedor

    def print_board(self):
        # isso é apenas obter as linhas
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (nos dizer que número corresponde a que caixa)
        number_board = [[str(i) for i in range (j*3, (j*1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def avaliable_moves(self):
         return [i for i, spot in enumerate(self.board) if spot == ' ']
#        moves = []
#        for (i, spot) in enumerate(self.board):
#            # ['X', 'x' , 'o'] --> [(0, 'x'), (1, 'x', (2, 'o'))]
#            if spot == ' ':
#                moves.append(i)
#        return moves

