from socket import *
import time
import os

def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text



# server
COD = 'utf-8'
HOST = '127.0.0.1' # 主机ip
PORT = 21566 # 软件端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
SIZE = 10
tcpS = socket(AF_INET, SOCK_STREAM) # 创建socket对象
tcpS.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #加入socket配置，重用ip和端口
tcpS.bind(ADDR) # 绑定ip端口号
tcpS.listen(SIZE)  # 设置最大链接数
while True:
    print("服务器serv-middle启动，监听客户端连接:")
    conn, addr = tcpS.accept()
    print("链接的客户端client-master：", addr)

    # client内置
    CHOST = '127.0.0.1'  # 服务端ip
    CPORT = 21565  # 服务端端口号
    BUFSIZ = 1024
    CADDR = (CHOST, CPORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
    tcpCliSock.connect(CADDR)  # 连接serv-end服务器

    while True:
        try:
            data = conn.recv(BUFSIZ) # 读取已链接客户的发送的消息
        except Exception:
            print("客户端client-master断开连接：", addr)
            tcpCliSock.close()  # 关闭客户端
            print("\n\n")
            break
        cmd = data.decode(COD)
        if cmd == "exit()":
            print("客户端client-master发送exit()，断开连接\n\n")
            tcpCliSock.close()  # 关闭客户端
            break
        elif not data:
            print("客户端client-master发送消息为空，断开连接\n\n")
            tcpCliSock.close()  # 关闭客户端
            break
        print("执行命令：",cmd)
        tcpCliSock.send(data)  # 发送消息->serv-end
        rev_data = tcpCliSock.recv(BUFSIZ)  # 读取消息<-serv-end
        conn.send(rev_data) #发送消息给已链接客户端->client-master
    conn.close() #关闭客户端链接
