import socket


def service_client(new_socket):
	"""为这个客户端返回数据"""
	# 1 接受浏览器发送来的请求，即http请求， GET /HTTP/1.1 ....
	request = new_socket.recv(1024)
	print(">>>"*50)
	print(request)
	# 2 返回http格式的数据给浏览器, header, body
	response = "HTTP/1.1 200 OK\r\n"
	response += "\r\n"
	# response += "<h1>hello world</h1>"
	f = open("./html/index.html", "rb")
	html_content = f.read()
	f.close()
	new_socket.send(response.encode("utf-8"))
	new_socket.send(html_content)
	# 关闭套接字
	new_socket.close()


def main():
	"""用来完成整体的控制"""
	# 1 创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# 2 绑定
	tcp_server_socket.bind(("", 7890))
	# 3 监听套接字
	tcp_server_socket.listen(128)
	while True:
		# 4 等待新客户端的链接
		new_socket, client_addr = tcp_server_socket.accept()
		# 5 为这个客户端服务
		service_client(new_socket)
	# 关闭监听套接字
	tcp_server_socket.close()


if __name__ == '__main__':
	main()
