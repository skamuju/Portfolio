import random


class Board:

    def __init__(self, layout=[]):

        self.layout = layout
        for i in range(3):
            self.layout.append(["_", "_", "_"])

        #This line creates the respective pieces on the board with one side being * and the other side being ^
        for i in range(len(self.layout)):

            if i == 0:
                pnum = 0
                for j in range(len(self.layout[i])):
                    self.layout[i][j] = "*"
                    pnum += 1

            elif i == 2:
                pnum = 0
                for j in range(len(self.layout[i])):
                    self.layout[i][j] = "^"
                    pnum += 1

    def __str__(self):

        blank = ""
        for row in self.layout:
            blank += "{}\n".format(row)

        return blank

    def move(self, team, col):

        if team == "*":
            for i in reversed(range(len(self.layout))):
                for j in range(len(self.layout[i])):
                    if j == col and self.layout[i][j] == "*":
                        if i != 2 and self.layout[i+1][j] == "_":
                            self.layout[i][j] = '_'
                            self.layout[i + 1][j] = "*"
                            return str(self.layout)

                        else:
                            print("This move is invalid")

        elif team == '^':
            for i in range(len(self.layout)):
                for j in range(len(self.layout[i])):
                    if j == col and self.layout[i][j] == "^":
                        if i != 0 and self.layout[i-1][j] == "_":
                            self.layout[i][j] = '_'
                            self.layout[i-1][j] = "^"
                            return str(self.layout)

                        else:
                            print("This move is invald")

    def take(self, team, col, eta):

        xpos = col
        ypos = 0
        if team == "*":
            for i in reversed(range(len(self.layout))):
                for j in range(len(self.layout[i])):
                    if j == col and self.layout[i][j] == "*":
                        if eta == "right" and col != 2:
                            self.layout[i][j] = "_"
                            self.layout[i+1][j+1] = "*"

                        elif eta == "left" and col != 0:
                            self.layout[i][j] = "_"
                            self.layout[i+1][j-1] = "*"

                        else:
                            print("This move is invalid")

        elif team == "^":
            for i in range(len(self.layout)):
                for j in range(len(self.layout[i])):
                    if j == col and self.layout[i][j] == "^":
                        if eta == "right" and col != 2:
                            self.layout[i][j] = "_"
                            self.layout[i-1][j+1] = "^"

                        elif eta == "left" and col != 0:
                            self.layout[i][j] = "_"
                            self.layout[i-1][j-1] = "^"

                        else:
                            print("This move is invalid")

    def check(self):

        if "^" in self.layout[0]:
            return "win"

        elif "*" in self.layout[-1]:
            return "loss"

        switch = True

        for i in range(len(self.layout)):
            for j in range(len(self.layout[i])):
                if self.layout[i][j] == "*":
                    if self.layout[i+1][j] == "_":
                        switch = False

                elif self.layout[i][j] == "^":
                    if self.layout[i-1][j] == "_":
                        switch = False

        if switch:
            return "tie"

    def reset(self):
        self.layout = []
        for i in range(3):
            self.layout.append(["_", "_", "_"])

        #This line creates the respective pieces on the board with one side being * and the other side being ^
        for i in range(len(self.layout)):

            if i == 0:
                for j in range(len(self.layout[i])):
                    self.layout[i][j] = "*"

            elif i == 2:
                for j in range(len(self.layout[i])):
                    self.layout[i][j] = "^"


def hexbot(game):

    # I wasn't able to make the full bot because I couldnt make any movement mechanincs in situations where pieces were doublestacked work after two or three approaches, with whats left being my third
    #     actions = {
    #         "poss1" : [1,2,3],
    #         "poss2" : [1,2],
    #         "poss3" : [1,2,3,4],
    #         "poss4" : [1,2,3,4],
    #         "poss5" : [1,2,3],
    #         "poss6" : [1,2,3],
    #         "poss7" : [1,2,3],
    #         "poss8" : [1,2],
    #         "poss9" : [1,2],
    #         "poss10" : [1,2],
    #         "poss11" : [1,2],
    #         "poss12" : [1,2],
    #         "poss13" : [1],
    #         "poss14" : [1,2],
    #         "poss15" : [1],
    #         "poss16" : [1,2]
    #     }

    #     if game.layout == [["*", "*", "*"], ["^", "_", "_"], ["_", "^", "^"]]:
    #         key = "poss1"
    #         action = random.choice(actions[key])
    #         if action == 1:
    #             Board.take(game, "*", 2, "left")

    #         elif action == 2:
    #             Board.move(game, "*", 2)

    #         elif action == 3:
    #             Board.move(game, "*", 3)

    #     elif game.layout == [["*", "*", "*"], ["_", "^", "_"], ["^", "_", "^"]]:
    #         key = "poss2"
    #         action = random.choice(actions[key])
    #         if action == 1:
    #             Board.move(game, "*", 1)

    #         else:
    #             Board.take(game, "*", 1, "right")

    #     elif game.layout == [["*", "_", "*"], ["*", "^", "_"], ["_", "_", "^"]]:
    #         key = "poss3"
    #         action = random.choice(actions[key])
    #         if action == 1:
    #             Board.move()

    #     elif game.layout == [["_", "*", "*"], ["^", "*", "_"], ["_", "_", "^"]]:
    #         key = "poss4"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["*", "_", "*"], ["^", "^", "_"], ["_", "^", "_"]]:
    #         key = "poss5"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["*", "*", "_"], ["^", "_", "^"], ["_", "_", "^"]]:
    #         key = "poss6"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["_", "*", "*"], ["_", "*", "^"], ["^", "_", "_"]]:
    #         key = "poss7"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["_", "*", "*"], ["*", "^", "^"], ["^", "_", "_"]]:
    #         key = "poss8"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["*", "_", "*"], ["*", "_", "^"], ["_", "^", "_"]]:
    #        key = "poss9"
    #        action = random.choice(actions[key])

    #     elif game.layout == [["*", "*", "_"], ["^", "^", "*"], ["_", "_", "^"]]:
    #         key = "poss10"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["_", "*", "*"], ["_", "^", "_"], ["_", "_", "^"]]:
    #         key = "poss11"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["_", "*", "*"], ["_", "^", "_"], ["^", "_", "_"]]:
    #         key = "poss12"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["*", "_", "*"], ["^", "_", "_"], ["_", "_", "^"]]:
    #         key = "poss13"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["_", "_", "*"], ["*", "*", "^"], ["_", "_", "_"]]:
    #         key = "poss14"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["*", "_", "_"], ["^", "^", "^"], ["_", "_", "_"]]:
    #         key = "poss15"
    #         action = random.choice(actions[key])

    #     elif game.layout == [["_", "*", "_"], ["*", "^", "^"], ["_", "_", "_"]]:
    #         key = "poss16"
    #         action = random.choice(actions[key])

    #     if Board.check(game) == "win":
    #         actions[key].remove(action)
    for i in reversed(range(len(game.layout))):
        for j in reversed(range(len(game.layout[i]))):
            if game.layout[i][j] == "*":
                if game.layout[i+1][j] == "_":
                    print(j, "up one")
                    Board.move(game, "*", j)
                    break

                elif j == 2:
                    if game.layout[i+1][j-1] == "^":
                        print(j, "take left")
                        Board.take(game, "*", j, "left")
                        break

                    else:
                        pass

                elif j == 1:
                    if game.layout[i+1][j-1] == "^":
                        print(j, "take left")
                        Board.take(game, "*", j, "left")
                        break

                    elif game.layout[i+1][j+1] == "^":
                        print(j, "take right")
                        Board.take(game, "*", j, "right")
                        break

                    else:
                        pass

                elif j == 0:
                    if game.layout[i+1][j+1] == "^":
                        print(j, "take right")
                        Board.take(game, "*", j, "right")
                        break

                    else:
                        pass


def play_hex(board):

    print('Hello and welcome to Hexapawn!')
    print("You will be playing as ^ against *")
    print('The goal is to get a piece on the other side of the board')
    print('To turn on the game type on type True or else type False')

    iput = input()
    switch = eval(iput)

    while switch:

        print(board)
        move = input(
            "Would you like to make a move or take? (your choices are m or t) ")
        if move == "m":
            col = int(input("Which piece would you like to move, 1, 2, or 3? "))
            col -= 1
            board.move('^', col)

        elif move == "t":
            col = int(input("Which piece would you like to move, 1, 2, or 3? "))
            col -= 1
            direc = input(
                "Which direction would you like to move, right or left? (Your options are right or left)? ")
            board.take('^', col, direc)

        print(board)
        print('player moved')

        if Board.check(game) == "win":
            print(game)
            print('You Won!')
            again = input("Play again? (y/n) ")
            if again == "y":
                game.reset()
                play_hex(game)

            else:
                print("Bye!")
                break

        elif Board.check(game) == "loss":
            print(game)
            print('Better luck next time!')
            again = input("Play again? (y/n) ")
            if again == "y":
                game.reset()
                play_hex(game)

            else:
                print("Bye!")
                break

        elif Board.check(game) == "tie":
            print(game)
            print("You tied!")
            again = input("Play again? (y/n) ")
            if again == "y":
                game.reset()
                play_hex(game)

            else:
                print("Bye!")
                break

        print('game was checked')

        hexbot(game)

        print('hexbot moved')

        if Board.check(game) == "win":
            print(game)
            print('You Won!')
            again = input("Play again? (y/n) ")
            if again == "y":
                game.reset()
                play_hex(game)

            else:
                print("Bye!")
                break

        elif Board.check(game) == "loss":
            print(game)
            print('Better luck next time!')
            again = input("Play again? (y/n) ")
            if again == "y":
                game.reset()
                play_hex(game)

            else:
                print("Bye!")
                break

        elif Board.check(game) == "tie":
            print(game)
            print("You tied!")
            again = input("Play again? (y/n) ")
            if again == "y":
                game.reset()
                play_hex(game)

            else:
                print("Bye!")
                break

        print("game was checked")


game = Board()


if __name__ == "__main__":

    play_hex(game)
