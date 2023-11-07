"""
  Jogo da Velha usando o chatGPT. Feito em Python.
"""
import random

# Printa as jogadas no tabuleiro
def print_board(board):
    # Cell é a jogada do usuário
    for row in board:
        for cell in row:
            print(cell, end=" | ")
        print("\n")

# Função que verifica o vencedor da partida
def check_winner(board, player):
    for row in board:
        # A função all retorna True ou False
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# A máquina faz um movimento completamente aleatório
def make_random_move(board, player):
    # Retorna uma lista que contém as células do tabuleiro que estão vazias
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = player

# Função principal do jogo
def main():
    # Cria o tabuleiro do jogo
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    # Enquanto não há vencedor ou uma entrada errada
    while True:
        print_board(board)

        # verifica se o movimento é inválido
        if current_player == "X":
            row, col = map(int, input(f"Player {current_player}, enter row and column (e.g., 1 2): ").split())
            if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != " ":
                print("Invalid move. Try again.")
                continue
            board[row - 1][col - 1] = current_player
        # Nesse caso, o movimento não é inválido
        else:
            print(f"Player {current_player} is making a move...")
            make_random_move(board, current_player)

        # Caso em que há um vencedor
        if check_winner(board, current_player):
            winner = current_player
            break

        # Caso em que todas as casas foram preenchidas
        if all(cell != " " for row in board for cell in row):
            break

        current_player = "X" if current_player == "O" else "O"

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
