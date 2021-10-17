def show_result(): #showing the current condition of the game board
    print(result['TL'],' | ',result['TM'],' | ',result['TR'])
    print('---|-----|---')
    print(result['ML'],' | ',result['MM'],' | ',result['MR'])
    print('---|-----|---')
    print(result['BL'],' | ',result['BM'],' | ',result['BR'])

def show_rules(): #opening of the game
    print('\n')
    print('2 players, X and O, will take turns placing their corresponding symbols on the board')
    print('When it is your turn, please use the two letter code below to choose where you want to place your symbols\n')
    print('TL',' | ','TM',' | ','TR')
    print('----|------|----')
    print('ML',' | ','MM',' | ','MR')
    print('----|------|----')
    print('BL',' | ','BM',' | ','BR')

def check_turn(x): #checking which player's turn currently
    if x %2 !=0:
        return 'X'
    else:
        return 'O'

def check_move(x,y): #making sure that the players only enter the valid move
    for i in result:
        if x==i:
            if result[i]==' ':
                result[i]=y
                return 0 #the move is valid and got appended into the result list
                break
            else:
                return 1 #the move already taken
                break

    return 2 #the move is invalid, its not in the moveset

def check_result(x):
    #checking the win by row
    for i in row:
        tempCounter=0
        for j in col:
            if result[i+j]==x:
                tempCounter+=1
            if tempCounter==3:
                return 1

    #checking the win by column
    for u in col:
        tempCounter=0
        for v in row:
            if result[v+u]==x:
                tempCounter+=1
            if tempCounter==3:
                return 1

    #checking the win by the diagonal
    if result['TL']==x and result['MM']==x and result['BR']==x or result['TR']==x and result['MM']==x and result['BL']==x:
        return 1
    return 0

#setting variables
row=['T','M','B']
col=['L','M','R']

roundCounter=1
result={
    'TL':' ' , 'TM':' ' , 'TR':' ',
    'ML':' ' , 'MM':' ' , 'MR':' ',
    'BL':' ' , 'BM':' ' , 'BR':' '
    }

#game code
print('Welcome to the TIC TAC TOE Game by @arkawimba')
input('Press Enter to show the rules')
show_rules()
input('\nPress Enter to start playing')

while True:
    player=check_turn(roundCounter)
    print('-----------------------------------------------')

    if roundCounter == 10: #draw the game when all the position in the board already filled w/o a winner
        print("DRAW GAME!")
        break

    print('ROUND ',roundCounter,)
    print('PLAYER ',player,' TURN! WHAT IS YOUR MOVE?')
    tempInput=input('Please enter a valid move: ')
    check=check_move(tempInput,player)

    if check == 1:
        print('Invalid ~ Move already taken')
        continue
    if check == 2:
        print('Invalid ~ Please enter valid move from the move set ')
        continue
    else:
        show_result()
        if check_result(player)==1:
            print('CONGRATULATION! PLAYER',player,'WIN!')
            break
        roundCounter+=1
        

print('GAME OVER')


