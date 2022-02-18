
# 7143CEM Programming for Data Science

def snakes_two_players():
    """Play snakes and ladders board game
    for two players"""
    print('Welcome to snakes and ladders')
    # Setup the board (idea: dictionary)
    snakes = {  9:  4,
               24: 13}
    ladders = { 5: 15,
               12: 21}
    winning_square = 25
    
    # Start on square 1
    positionA = 1
    positionB = 1
    count_snakes = 0
    count_ladders = 0
    keep_going = True
    while (keep_going):
        # Player A has a turn
        print('---')
        print('Player A is at position=',positionA)
        # Roll the dice
        d = random.randint(1,6)
        print('  dice was',d)
        # Update the position
        positionA = positionA + d
        print('    new position is',positionA)
        # Check for snake
        if (positionA in snakes.keys()):
            print('      ## snake bite')
            count_snakes = count_snakes + 1
            new_position = snakes[positionA]
            positionA = new_position
        # Check for ladder
        if (positionA in ladders.keys()):
            print('      $$ ladder')
            count_ladders = count_ladders + 1
            new_position = ladders[positionA]
            positionA = new_position
        #
        if (positionA >= winning_square):
            print('A has won')
            who_won = 'A'
            keep_going = False
        else:
            # Player B has a turn
            print('---')
            print('Player B is at position=',positionB)
            # Roll the dice
            d = random.randint(1,6)
            print('  dice was',d)
            # Update the position
            positionB = positionB + d
            print('    new position is',positionB)
            # Check for snake
            if (positionB in snakes.keys()):
                print('      ## snake bite')
                count_snakes = count_snakes + 1
                new_position = snakes[positionB]
                positionB = new_position
            # Check for ladder
            if (positionB in ladders.keys()):
                print('      $$ ladder')
                count_ladders = count_ladders + 1
                new_position = ladders[positionB]
                positionB = new_position
            if (positionB >= winning_square):
                print('B has won')
                who_won = 'B'
                keep_going = False
    print('Game over')
    result = {'winner': who_won,
              'ladders': count_ladders,
              'snakes': count_snakes}
    return(result)

print(snakes_two_players())
    
# Questions/challenges:
#   How many dice rolls for each player?
#   If A wins, what square number is B on?
#   If B wins, what square number is A on?
#   If you play 1000 times, how many times does A win? B win?
#      (is there an advantage to going first?)

