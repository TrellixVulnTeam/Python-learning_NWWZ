import socket


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 从键盘输入数据
    send_data = input("请输入要发送的数据：")
    # 可以使用套接字收发数据
    # udp_socket.sendto(b"hahahaha", 对方的ip以及port)
    # 例如 udp_socket.sendto(b"hahahaha", ("192.168.3.3", 8080))
    udp_socket.sendto(send_data.encode("utf-8"), ("192.168.244.1", 8080))
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
