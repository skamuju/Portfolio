# Saketh Kamuju, Jonathan King
# NOTE: Until you fill in the TicTacToe class, you will get AttributeErrors. Don't worry
# about those yet––follow the README for exactly what to do, rather than the errors
# you are seeing on the asserts.

class TicTacToeBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self, board=["*", "*", "*", "*", "*", "*", "*", "*", "*"]):
        self.board = board

    def __str__(self):

        return str(self.board[0:3]) + "\n" + str(self.board[3:6]) + "\n" + str(self.board[6:9])

    def has_won(self, player):

        board = self.board
        win = [player, player, player]

        if board[0:3] == win or board[3:6] == win or board[6:9] == win:
            return True

        elif board[0:9:3] == win or board[1:9:3] == win or board[2:9:3] == win:
            return True

        elif board[0:9:4] == win or board[2:8:2] == win:
            return True

        return False

    def game_over(self):

        game = self

        if TicTacToeBoard.has_won(game, "X") or TicTacToeBoard.has_won(game, "O"):
            return True

        elif "*" not in game.board:
            return True

        return False

    def make_move(self, player, pos):

        if player == "X":
            if self.board[pos] == "*":
                self.board[pos] = "X"

            else:
                return False

        elif player == "O":
            if self.board[pos] == "*":
                self.board[pos] = "O"

            else:
                return False

        # print(self)
        return True

    def clear(self):

        self.board = []
        for i in range(9):
            self.board.append("*")


def play_tic_tac_toe():
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TicTacToeBoard()
    brd.clear()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # Here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TicTacToeBoard class is behaving
    # proprely.
    brd = TicTacToeBoard()
    brd.make_move("X", 8)
    # print("")
    brd.make_move("O", 7)

    assert brd.game_over() == False
    # print("jello")

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True
    # print("jello")

    brd.clear()

    assert brd.game_over() == False
    # print("jello")

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)
    # print("")

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True
    # print("jello")

    brd.clear()

    brd.make_move("X", 0)
    brd.make_move("X", 2)
    brd.make_move("X", 4)
    brd.make_move("X", 7)
    brd.make_move("O", 1)
    brd.make_move("O", 3)
    brd.make_move("O", 5)
    brd.make_move("O", 6)
    brd.make_move("O", 8)
    # print(brd)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == False
    assert brd.game_over() == True
    # print("jello")
    brd.clear()

    print("All tests passed!")

    # uncomment to play!
    # play_tic_tac_toe()
