class JogodaVelha:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # única lista para substituir 3x3
        self.current_winner = None #manter o controle do vencedor

    def print_board(self):
        # isso é apenas para obter as linhas
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (nos dizer que número corresponde a qual caixa)
        number_board = [[str(i) for i in range (j*3, (j*1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def avaliable_moves(self):
         return [i for i, spot in enumerate(self.board) if spot == ' ']

def jogar(jogo, x_jogador, o_jogador, print_jogo=True):
    if print_jogo:
        jogo.print_board_nums()

    letter = 'X' # iniciando as letras
    # iterar enquanto o jogo ainda tem quadrados vazios
    # (não temos que se preocupar com o vencedor, porque vamos apenas retornar o 
    # que quebra o loop)
