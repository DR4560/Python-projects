#Socket WebServer
#Ответ-запрос эхо сервера + клиент-заглушка

import socket

def start_server():
    try:
        my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_server.bind(('127.0.0.1', 1025))
        my_server.listen(4)#input calls ,4- max

        while True:
            print('In process...')
            client_socket, address = my_server.accept()
            data = client_socket.recv(1025).decode('utf-8')
            #print(data)
            content = load_page(data) #('The connection was reset. Error 10948v%%55').encode('utf-8')
            client_socket.send(content)#HDRS.encode('utf-8') +
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        my_server.close()
        print('Exit....')




def load_page(request_data):#from the use request
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n'
    HDRS_500 = 'HTTP/1.1 500 OK\r\nContent-Type:text/html;charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    try:
        with open('views'+path,'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') +response
    except FileNotFoundError:
        return (HDRS_404 +'Page is not available').encode('utf-8')
    except ErrorCase as e:
        return (HDRS_500 +'505 INTERNAL ERROR').encode ('utf-8')

client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if __name__ == '__main__':
    start_server()

