Welcome to Saketh's Hexapawn!

    This game is a game simmiliar to chess but instead of the normal rules Hexapawn is played on a 3X3 board with three pawns on each side.
The goal of this game is to get your pawn to the other side while blocking your enemy from doing the same. If neither player has a valid move, then it is a
tie. To play the game simply run the program and type in the terminal. For each choice you make please type in your response as you see it on the prompt. For example, 
when the computer askes if you would like to move or take (m or t), simply type in m (to move), or t (to take). This game is much simpler than chess but takes shorter and
can be enjoyable for a quick one or two minute match.

About the program:

    This game is built on OOP. The gameboard is constructed as a class object. You interact with the gameboard through class methods such as move, or take.
This is why sometimes you may see movement as board.move(...) or as Board.move(game...), with board being an object referencing a method or using the name 
of the class Board being used to reference the method with teh object being passed in inside the parentheses. As of right now, the AI operates on two goals. Either 
the computer will move its rightmost piece if possible, or it will attempt a take. If neither of these are availible, itll try a move only for it to be invalid. 
However, that is no fun. Try and expiriment with different opening and middle moves
to find every apth to victory, and have fun! The "hexbot" is simply a function that takes the gamboard as a parameter, and runs a series of if statements on it to 
determine how the computer will move. It will first check if it can move a piece forwards, and then check for any possible takes. If it finds either, it will execute
them by calling one of the class methods "move", or "take". Finally, the actual game operates as a while loop with a Boolean used as a switch based on user input.
In addition, after any move by the player or computer there will be a check to see if the game has been won. If so, the loop will break with a friendly goodby message.

    The original idea for the AI was based on a system of matchbox computers which operated on a genetic algorithm. This meant that the matchboxes planned out every
single possible scenario and then randomly selected a move to make afterwards. If the move resulted in a loss, it would be removed as a possible behavior, thus helping
the comptuer "learn". Unfortunately, I couldn't figure out how to reflect the matchboxes since in real life you simply use the matchbox with a reflected scenario if 
that is what happens in game. I want to try and crack this over the summer but for the sake of time I resorted to the basic approach of either move or take. I wanted to include a 
picture of the matchbox computers for reference but for some reason it isnt working. You can find a pcture by simply Googling Hexapawn. Credit to VSauce for making a video on 
Hexapawn using a matchbox computer in real life. I used his ideas and tried to translate them into code.

 