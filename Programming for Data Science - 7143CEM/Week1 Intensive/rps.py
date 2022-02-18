
# What does this mystery code do?
# Start with: rpsoriginal.py

import random
def rock_paper_scissors():
    """Play Rock-Paper-Scissors"""
    count_draw = 0
    count_win = 0
    count_loss = 0
    for i in range(100000):
        a = random.randint(0,2)
        b = random.randint(0,2)
        # 0 is rock, 1 is paper, 2/3 is scissors
        if (a==0):
            if (b==0):
                # both rock (draw)
                count_draw = count_draw+1
            elif (b==1):
                # rock is covered by paper (loss)
                count_loss = count_loss+1
            else:
                # rock smashes scissors (win)
                count_win = count_win+1
        elif (a==1):
            if (b==0):
                # paper covers rock (win)
                count_win = count_win+1
            elif (b==1):
                # both paper (draw)
                count_draw = count_draw+1
            else:
                # paper is cut by scissors (loss)
                count_loss = count_loss+1
        else:
            if (b==0):
                # scissors is smashed by rock (loss)
                count_loss = count_loss+1
            elif (b==1):
                # scissors cuts paper (win)
                count_win = count_win+1
            else:
                # both scissors (draw)
                count_draw = count_draw+1
    result = {'win': count_win,
              'draw': count_draw,
              'loss': count_loss}
    return(result)

# 100 bonus points: Pandey
 
# Summarise:
#   repeat a process 30 times)
#   roll two dice equivalent (four sided dice: 0,1,2,3)
#   increase cd or cl or cw by one depending on a,b

#         a==0    a==1   a==2,3
# b==0     cd      cw     cl
# b==1     cl      cd     cw     
# b==2,3   cw      cl     cd

# Anything strike you?
# - cd when sort of a==b
# - every row has {cd,cw,cl} once each
# - every col has {cd,cw,cl} once each
#    "Latin square" (super geek)

# Clue: w means "win"
# therefore: d is "draw" and l is "loss"
# c is "count"
# play 30 times, each time has a win or draw or loss
# two players, roll one dice each, result is win, draw or loss


print(rock_paper_scissors())

# https://docs.python.org/3/library/random.html
print(random.choice(['red','green','blue']))

L = ['red','green','blue']
random.shuffle(L)
print(L)

# -- the end --
