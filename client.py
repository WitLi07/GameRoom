import socket
import sys
import tictactoe
from os import path

def client_program():
    if(len(sys.argv) != 3):
        print("Usage: python client.py <server_IP> <server_port>")
        sys.exit()

    port = int(sys.argv[2])
    server_addr = (sys.argv[1], port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(server_addr)

    message = raw_input(" What do you want to do? ")

    while message.strip() != ".":
        command = str(message)

        if(command == "HISTORY"):
            client_socket.send(command)
            history = client_socket.recv(1024)
            print(history)
            message = raw_input(" What else? ")



        elif(command == "RPS"):
            client_socket.send(command)

            reply = client_socket.recv(1024)

            if(reply != "READY? "):
                print(reply)
                message = raw_input(" What game you want to play? ")
                continue

            readyState = raw_input(" READY? ")
            readyState = str(readyState)

            if(not (readyState.startswith('y') or readyState.startswith('Y'))):
                message = raw_input(" What game you want to play? ")
                continue

            client_socket.send("Yes")
            print("Let's Start!")

            shape = raw_input("What shape do you want? ")
            client_socket.send(shape)

            result = client_socket.recv(1024)
            print(result)

            message = raw_input(" What else? ")
        elif(command == "TTT"):
            client_socket.send("TTT")

            while(1):
                res = client_socket.recv(1024)
                if(res == "Game Over"):
                    break
                elif(res == "Play Again?"):
                    again = raw_input("Play Again? ")
                    client_socket.send(again)
                elif(res.startswith("X Turn") or res.startswith("That place")):
                    move = raw_input(res)
                    client_socket.send(move)
                else:
                    print(res)


            message = raw_input(" What else? ")
        else:
            print("Sorry, invalid command.")
            message = raw_input(" What do you want to do? ")


    client_socket.close()

if __name__ == '__main__':
    client_program()
