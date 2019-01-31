# 这个 ssh 主要是通过客户端执行命令。先启动服务端，后启动客户端，输入命令。
import socket

client = socket.socket()
client.connect(("localhost", 8001))

while True:
    msg = input(">>").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode())
    print("sent command:", msg)
    data = client.recv(1024).decode()
    if data == '0':
        print("\'", msg, "\'", '不是内部或外部命令，也不是可运行的程序或批处理文件。')
        continue
    else:
        print("--------------------------------------------------")
        print("The res length is:", data, ". \nStarting to receive...")

        total_size = int(data)
        received_size = 0
        res = b''
        while received_size < total_size:
            add = client.recv(1024)
            res += add
            received_size += len(add)
        print("Receiving has been finished.")
        print("--------------------------------------------------")
        print("Here is the cmd responding: ", res.decode())


