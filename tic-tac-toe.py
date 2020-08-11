#libraries:
import random , numpy


playground = [[1,2,3],
              [4,5,6],      
              [7,8,9]]


def default():
    global playground 
    playground = [[1,2,3],
                   [4,5,6],      
                   [7,8,9]]

#display
def display(ground):
    print('-------------')
    for row in ground:
        for value in row:
            print('|',value , end=" ")
        print('|')

        #row seperator
        print('-------------')

def main():    
    #playground
    pass






def main_menu():
    global player1
    global player2

    print(55*"=","welcome to tic-tac-toe game",55*"=")
    print(48*"=","we wish you good luck beating your friend",48*"=")

    print("press enter to proceed")
    input("> ")

    player1 = input("input the first player name ")
    player2 = input("input the second player name ")
    
    start(player1,player2)


def toss_a_coin(player1,player2):
    choices = ['tales' , 'head']

    player_2_choice = ''

    player_1_choice = input(f'{player1} input tales / head :  ')

    if player_1_choice == choices[0]:
        player_2_choice = choices[1]

    elif player_1_choice == choices[1]:
        player_2_choice = choices[0]
    
    toss = random.choice(choices)
    
    if toss == player_1_choice:
        return player1
    else:
        return player2
    

def start(player1,player2):
    global next_turn
    global playground
    print(f'\n {player1} vs {player2}')

    winner = toss_a_coin(player1,player2)


    print(f'{winner} begins')
    print(f'{winner}\'s turn - play with X')

    next_turn = winner
    display(playground)
    choose(int(input('where? ')),next_turn)
 
    while (is_a_win() == False):

        display(playground)

        choose(int(input('where?')),next_turn)
        
        if next_turn == player1:

            next_turn = flip(player2)

        elif next_turn == player2:
            
            next_turn = flip(player1)


def get_axis(array):
    numpy_array = numpy.array(array)
    main_axis = list()
    other_axis = list()
    x,y = numpy_array.shape

    if x == y :
        b= -1
        for counter in range(x):
            main_axis.append(numpy_array[counter][counter])
        for i in range(x):
            other_axis.append(numpy_array[i][b])
            b = b-1


    return (main_axis , other_axis)
def is_a_win():
    global playground

    O_array = numpy.array(['O','O','O'])
    X_array = numpy.array(['X','X','X'])
    

    tem_play = numpy.array(playground)

    for row in tem_play:
        if list(row) == list(O_array):  
            return 'o'
        elif list(row) == list(X_array):
            return 'x'

    for column in tem_play.T:
        if list(column) == list(O_array):  
            return 'o'
        elif list(column) == list(X_array):
            return 'x'

    for axis in get_axis(playground):
        
        if axis == list(O_array):  
            return 'o'
        elif axis == list(X_array):
            return 'x'

    return False



    



def flip(player):
    global next_turn
    global player1 
    global player2

    

    if player == player1:
        return player2
    elif player == player2:
        return player1

    
def choose(choice,next_turn):
    global playground
    global player1
    global player2

    if next_turn == player1:
        ch = 'X'
    elif next_turn == player2:
        ch = 'O'


    if choice == 1:
        playground[0][0] = ch
    elif choice == 2:
        playground[0][1] = ch
    elif choice == 3:
        playground[0][2] = ch
    elif choice == 4:
        playground[1][0] = ch
    elif choice == 5:
        playground[1][1] = ch
    elif choice == 6:
        playground[1][2] = ch 
    elif choice == 7:
        playground[2][0] = ch 
    elif choice == 8:
        playground[2][1] = ch
    elif choice == 9:
        playground[2][2] = ch
    else:
        print('not valid')

main_menu()