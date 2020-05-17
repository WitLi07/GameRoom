import socket
import sys
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

            if(readyState != "Yes"):
                message = raw_input(" What game you want to play? ")
                continue

            client_socket.send("Yes")
            print("Let's Start!")

            shape = raw_input("What shape do you want? ")
            client_socket.send(shape)

            result = client_socket.recv(1024)
            print(result)

            message = raw_input(" What else? ")
        elif(command.startswith("uTake")):
            filename = command.split(" ")[1]

            if(not path.exists("store/"+filename)):
                print("Cannot open or find the file.")
                message = raw_input(" Command: ")
                continue

            client_socket.send(command)

            reply = client_socket.recv(1024)

            if(not reply == "OK"):
                print ("Server not ready to receive file.")
                message = raw_input(" Command: ")
                continue

            with open("store/" + filename, 'rb') as f:
                    for data in f:
                        client_socket.sendall(data)
            client_socket.send("DONE")
            print("Successfully sent file " + filename)
            f.close()
            message = raw_input(" What else? ")
        else:
            print("Sorry, invalid command.")
            message = raw_input(" What do you want to do? ")


    client_socket.close()

if __name__ == '__main__':
    client_program()
