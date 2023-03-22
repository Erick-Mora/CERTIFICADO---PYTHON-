import socket
def main():
    print("Ejercicio 11")
    print("Browser")
    mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #print(mysock)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    #print(cmd)
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if(len(data)<1):
            break
        print(data.decode())
    mysock.close

if __name__ == "__main__":
    main()