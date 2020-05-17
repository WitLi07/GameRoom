import socket

gameBoard = {'7': ' ','8': ' ','9': ' ','4': ' ','5': ' ','6': ' ','1': ' ','2': ' ','3': ' '}

board_keys = []

for key in gameBoard:
    board_keys.append(key)

def getBoard(board):
    return board['7'] + '|' + board['8'] + '|' + board['9'] + '\n' + '-+-+-' + '\n' + board['4'] + '|' + board['5'] + '|' + board['6'] + '\n' + '-+-+-' + '\n' + board['1'] + '|' + board['2'] + '|' + board['3'] + '\n'
    

def game(conn, total, clientWon, serverWon, lastWon):

    turn = 'X'
    count = 0

    conn.send("hello\n")
    total += 1

    for i in range(10):
        print(getBoard(gameBoard))
        conn.send(getBoard(gameBoard))
        if(turn=='X'):
            conn.send(turn + " Turn. Move to? ")
            move = conn.recv(1024)
        else:
            move = input(turn + " Turn. Move to? ")
            
        move = str(move)       

        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            if(turn=='X'):
                conn.send("That place is filled.\nA new place? ")
            else:
                print("That place is filled.\nA new place? ")
            continue

        if count >= 5:
            if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
                print(getBoard(gameBoard))
                conn.send(getBoard(gameBoard))
                print("\nGame Over.\n")                
                print(turn + " won!")
                if(turn == 'X'):
                    clientWon += 1
                    lastWon = 'you'
                else:
                    serverWon += 1
                    lastWon = 'me'
                conn.send(turn + " won!")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
                print(getBoard(gameBoard))
                conn.send(getBoard(gameBoard))
                print("\nGame Over.\n")                
                print(turn + " won!")
                if(turn == 'X'):
                    clientWon += 1
                    lastWon = 'you'
                else:
                    serverWon += 1
                    lastWon = 'me'
                conn.send(turn + " won!")
                break
            
            elif gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
                print(getBoard(gameBoard))
                conn.send(getBoard(gameBoard))
                print("\nGame Over.\n")                
                print(turn + " won!")
                if(turn == 'X'):
                    clientWon += 1
                    lastWon = 'you'
                else:
                    serverWon += 1
                    lastWon = 'me'                
                conn.send(turn + " won!")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
                print(getBoard(gameBoard))
                conn.send(getBoard(gameBoard))
                print("\nGame Over.\n")                
                print(turn + " won!")
                if(turn == 'X'):
                    clientWon += 1
                    lastWon = 'you'
                else:
                    serverWon += 1
                    lastWon = 'me'
                conn.send(turn + " won!")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
                print(getBoard(gameBoard))
                conn.send(getBoard(gameBoard))
                print("\nGame Over.\n")                
                print(turn + " won!")
                if(turn == 'X'):
                    clientWon += 1
                    lastWon = 'you'
                else:
                    serverWon += 1
                    lastWon = 'me'
                conn.send(turn + " won!")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
                print(getBoard(gameBoard))
                conn.send(getBoard(gameBoard))
                print("\nGame Over.\n")                
                print(turn + " won!")
                if(turn == 'X'):
                    clientWon += 1
                    lastWon = 'you'
                else:
                    serverWon += 1
                    lastWon = 'me'
                conn.send(turn + " won!")
                break 
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
                print(getBoard(gameBoard))
                conn.send(getBoard(gameBoard))
                print("\nGame Over.\n")                
                print(turn + " won!")
                if(turn == 'X'):
                    clientWon += 1
                    lastWon = 'you'
                else:
                    serverWon += 1
                    lastWon = 'me'
                conn.send(turn + " won!")
                break 
            elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ':
                print(getBoard(gameBoard))
                conn.send(getBoard(gameBoard))
                print("\nGame Over.\n")                
                print(turn + " won!")
                if(turn == 'X'):
                    clientWon += 1
                    lastWon = 'you'
                else:
                    serverWon += 1
                    lastWon = 'me'
                conn.send(turn + " won!")
                break

        
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie.")
            conn.send("It's a Tie.")

        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    

    conn.send("Play Again?")
    restart = conn.recv(1024)
    restart = str(restart)

    if restart.startswith('y') or restart.startswith('Y'):  
        for key in board_keys:
            gameBoard[key] = " "

        game(conn,total,clientWon,serverWon,lastWon)

    conn.send("Game Over")

    return total, clientWon, serverWon, lastWon
