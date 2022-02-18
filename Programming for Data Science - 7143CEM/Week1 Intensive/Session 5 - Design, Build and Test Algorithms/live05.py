# 3. More on loops

print('@@@@@@@@')

for a in range(0,4):
    print(a)
    
a =0
while (a<4):
    print(a)
    a =a+1
    
print('@@@@@@@@')

def insertion_sort(L_input):
    """Sort a list of values into ascending order
    using Insertion Sort"""
    L = L_input.copy()
    for i in range(1,len(L)):
        # suppose we have sorted left part L[0:i]
        #   not including index i
        # right part is L[i:]
        print('---- top of loop ----')
        print('Left-part is ',L[0:i])
        print('Right part is ',L[i:])
        print('Take index',i,' which as value',L[i])
        # need ANOTHER loop to scan down the left-part list
        # k loop with scan right-to-left
        k = i
        keep_going = True
        while(K>0 and keep_going):
            print('Compare index',k,'with index',k-1)
            print(' --> compare value',L[k],' with value ',L[k-1])
            if (L[k]<L[k-1]):
                print('Swap')
                L[k-1],L[k] = L[k],L[k-1] # multiple assignment
                print('List is now',L)
            else:
                print('No swap needed')
                # --> somehow we need to STOP the k loop!!!!
                keep_going = False
                print('List is now',L)
            k= k-1
            
L = [6,4,10,8,2]


# 4. Snakes and dice
    import random
    def snakes_and_dice():
      """Play """
       position = 1
        while(position<25):
        
        
            print(('you are at position:', position))
            dice = random.randint(1,6)
            print('dice roll:', dice)
            position = position+dice
            if(position==5):
               print('climb the ladder to 15')
               position = 15
            if(position ==12):
                print('climb the ladder to 21')
                position=21
            if(position==9):
                print('Slide down to 4')
                position=4
            if(position==24):
                print('slide down the snake to 13')
                position=13
        print("Game Over")
    snakes_and_dice()  