def TicTacToe():
    board = {str(n): ' ' for n in range(1, 10)}

    print(TicTacToe.__doc__)
    printBoard(board)
    while True:
        checkMove('X', board)
        status = checkWin('X', board)
        if status == True:
            break

        checkMove('O', board)
        status = checkWin('O', board)
        if status == True:
            break
    return

def checkMove(S, moves):
    N = input(S + ' move: ')
    if (int(N) in range(1,10)) == False:
        print('Number must be between 1 and 9, try again...')
        checkMove(S, moves)
    else:
        if moves[str(N)] == ' ':
            moves[str(N)] = S
            printBoard(moves)
            return moves
        else:
            print('Position ' + str(N) + ' taken, try again')
            checkMove(S, moves)



def printBoard(moves):
    print(' ')
    print(moves['1']+'|'+moves['2']+'|'+moves['3'])
    print('-----')
    print(moves['4']+'|'+moves['5']+'|'+moves['6'])
    print('-----')
    print(moves['7']+'|'+moves['8']+'|'+moves['9'])
    print(' ')

def checkWin(S, moves):
    if (moves['1']==moves['4']==moves['7']==S or
        moves['2']==moves['5']==moves['8']==S or
        moves['3']==moves['6']==moves['9']==S):
        print(S + ' wins!')
        return True

    elif (moves['1']==moves['2']==moves['3']==S or
        moves['4']==moves['5']==moves['6']==S or
        moves['7']==moves['8']==moves['9']==S):
        print(S + ' wins!')
        return True

    elif (moves['1']==moves['5']==moves['9']==S or
        moves['3']==moves['5']==moves['9']==S):
        print(S + ' wins!')
        return True

    elif(' ' in moves.values()) == False:
        print('Draw!')
        return True
    else:
        return False

TicTacToe()