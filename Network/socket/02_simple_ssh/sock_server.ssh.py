
# 这个 ssh 主要是通过客户端执行命令。先启动服务端，后启动客户端，输入命令。服务端主要运行在 linux 上。
import socket
import subprocess


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8001))
server.listen(5)
print('start to listen...')


while True:
    conn, client_addr = server.accept()
    print(conn, client_addr)

    while True:
        data = conn.recv(1024)
        print("received from client；", data)
        res_obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res = res_obj.stdout.read()
        length = str(len(res)).encode()
        conn.send(length)
        print('res length is:  ',length,' Bytes')
        conn.send(res)
