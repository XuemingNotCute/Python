import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen(5)
print('start connecting...')
conn, address = server.accept()
print(conn)
print(address)

"""
# 1. 第一次单向通信
data = conn.recv(1024)
print("received msg:", data)

# 2. 第一次双向通信
conn.send(b"I have got your msg. Welcome to the board.")

# 3. 循环收发
while True:
    data = conn.recv(1024)
    print("received from client；", data)
    conn.send(b"Server has got the msg.")
"""

# 4. 模拟 QQ 自动回复
while True:
    data = conn.recv(1024)
    print("received from client；", data)
    conn.send(b"AUTO_REPLY: I have got your msg. Sorry I'm not available now, I will reply you as soon as possible.")
