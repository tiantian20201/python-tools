from socket import *
import time
import os

def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text




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
    print("服务器serv-end启动，监听客户端连接:")
    conn, addr = tcpS.accept()
    print("链接的客户端", addr)
    while True:
        try:
            data = conn.recv(BUFSIZ) # 读取已链接客户的发送的消息
        except Exception:
            print("客户端断开连接：", addr)
            print("\n\n")
            break
        cmd = data.decode(COD)
        if cmd != "exit()":
            pass
        else:
            print("客户端发送exit，断开连接\n\n")
            break
        if not data:
            break
        msg = time.strftime("%Y-%m-%d %X") #获取结构化事件戳
        print('[%s]:%s执行命令：%s' % (msg,addr,cmd))
        msg1 = '[%s]:%s' % (msg, execCmd(cmd))
        conn.send(msg1.encode(COD)) #发送消息给已链接客户端
    conn.close() #关闭客户端链接
