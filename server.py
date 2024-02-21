import threading
import socket
import time
brodoserver = None
comlist = {}
# made by wandukong
# 응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~응 꿀잠~

def clientlogin():
    global brodoserver
    brodoserver.listen(2)
    while True:
        conn, addr = brodoserver.accept()
        print("클라이언트가 접속했습니다.")
        print("콘 : " + str(conn))
        print("어드레스 : " + str(addr))
        print("콘 정보를 데이터에 저장합니다.")
        logindata = conn.recv(1024).decode
        name = logindata[6:]
        print("사용자가 로그인 됐습니다. 닉네임 : " + name)


def serveropen():
    global brodoserver
    host = socket.gethostname()
    print("로그인 서버 생성을 시작합니다.")
    print("로그인 서버 포트를 입력하세요.")
    port = int(input(">>"))
    print("브로도캐스트 서버 생성을 시작합니다.")
    print("브로도캐스트 서버 포트를 입력하세요.")
    port2 = int(input(">>"))
    loginserver = socket.socket()
    loginserver.bind((host, port))
    print("로그인 서버가 생성됐습니다.")
    brodoserver = socket.socket()
    brodoserver.bind((host, port2))
    print("브로도캐스트 서버가 생성됐습니다.")
    print("클라이언트 대기를 시작합니다...")

if __name__ == "__main__":
    serveropen()