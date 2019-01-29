import socket

client = socket.socket()
client.connect_ex(("localhost", 8000))
print(client.connect_ex(("localhost", 8000)))

"""
# 1. 第一次单向通信
client.send(b"Across the Great Wall we can reach every corner in the world.")

# 2. 第一次双向通信
data = client.recv(1024)
print("msg from server", data)

# 3. 循环收发
while True:
    client.send(b"hello world")
    print("send hello world")
    data = client.recv(1024)
    print("feedback from the server", data)
"""

# 4. 模拟 QQ 自动回复
while True:
    msg = input(">>").strip()
    client.send(msg.encode())
    print("sent", msg)
    data = client.recv(1024)
    print("feedback from the server", data)
