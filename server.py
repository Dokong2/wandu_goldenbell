import threading
import socket
chatserver = None
comserver = None
comlist = {}
# made by wandukong
# ver 1.0
#귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아귀찮아
        

def serveropen():
    host = socket.gethostname()
    print("서버 생성을 시작합니다.")
    print("서버 포트를 입력하세요.")
    port = int(input(">>"))
    server_socket = socket.socket()
    server_socket.bind((host, port))
    print("이거프린트되면바로잘거임ㅅㄱ")
    server_socket.close()

if __name__ == "__main__":
    serveropen()