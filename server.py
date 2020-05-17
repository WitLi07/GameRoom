import socket
import sys
import os.path
import tictactoe
from os import path

def server_program():
    host = socket.gethostname()
    print("Host name: " + str(host))

    if(len(sys.argv) != 2):
        print("Usage: python server.py <port_number>")
        sys.exit()

    port = int(sys.argv[1])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(5)

    while True:
        conn, address = server_socket.accept()

        print("Connection from: " + str(address))

        totalGame = 0
        lastResult = "us"
        serverWin = 0
        clientWin = 0
        message = conn.recv(1024)

        while str(message).strip() != '.':
            if not message:
                break

            if(message == "HISTORY"):
                conn.send("We have played %d games. You won %d games and I won %d games. The winner of last game is %s." % (totalGame,clientWin,serverWin,lastResult))
                message = conn.recv(1024)
                # print("We have played %d games. You won %d games and I won %d games. The winner of last game is %s." % (totalGame,clientWin,serverWin,lastResult))


            elif(message == "RPS"):
                
                conn.send("READY? ")

                readyState = conn.recv(1024)
                if(readyState != "Yes"):
                    print("Not Ready for the game...")
                    continue

                print("Let's Start!")
                totalGame += 1

                shape = raw_input("What shape do you want? ")
                oppoShape = conn.recv(1024)
                winner = whoWin(shape[0],oppoShape[0]) # only use first character to determine who wins

                if(winner == "T"):
                    print("TIE GAME")
                    lastResult = "a tie"
                    conn.send("TIE GAME")
                elif(winner == "S"):
                    print("You won this one!")
                    serverWin += 1
                    lastResult = "me"
                    conn.send("You lost on this one..")
                else:
                    print("You lost on this one..")
                    clientWin += 1
                    lastResult = "you"
                    conn.send("You won this one!")

                message = conn.recv(1024)

            elif(message == "TTT"):
                totalGame,clientWin,serverWin,lastResult = tictactoe.game(conn, totalGame, clientWin, serverWin, lastResult)

                message = conn.recv(1024)

            else:
                print("Invalid Command!")
            

        conn.close


def whoWin(s1,s2):
    if(s1 == s2):
        return "T"
    elif((s1 == "r" and s2 == "p") or (s1 == "s" and s2 == "r") or (s1 == "p" and s2 == "s")):
        return "C"
    else:
        return "S"

if __name__ == '__main__':
    server_program()
