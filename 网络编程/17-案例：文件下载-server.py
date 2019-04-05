import socket


def send_file_2_client(new_client_socket, client_addr):
    # 接收客户端发送来要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端（%s）需要下载的文件是：%s" % (str(client_addr), file_name))
    # 打开这个文件，读取数据
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
    except Exception as ret:
        print("没有要下载的文件（%s）" % file_name)
    # 发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)

def main():
    # socket创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind绑定ip和port
    tcp_server_socket.bind(("", 7890))
    # listen使套接字变为可以被动链接
    tcp_server_socket.listen(128)
    while True:
        # accept等待客户端的链接    
        new_client_socket, client_addr = tcp_server_socket.accept()  # 返回的是元组
        # 调用发送文件函数，完成为客户端服务
        send_file_2_client(new_client_socket, client_addr)
        # 关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
