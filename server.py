import threading
import socket
import time
brodoserver = None
comlist = {}
# made by wandukong
#!화장실이급한!화장실이급한!화장실이급한!화장실이급한!화장실이급한!화장실이급한!화장실이급한!화장실이급한!화장실이급한!화장실이급한!


def nowtime():
    return now.localtime().tm_hour + " : " + now.localtime().tm_min + " : " + now.localtime().tm_sec + " "

def clientlogin():
    global brodoserver
    brodoserver.listen(2)
    while True:
        conn, addr = brodoserver.accept()
        print(nowtime + "클라이언트가 접속했습니다.")
        print("콘 : " + str(conn))
        print("어드레스 : " + str(addr))

        print(nowtime + "콘 정보를 데이터에 저장합니다.")

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
    print(nowtime + "로그인 서버가 생성됐습니다.")
    brodoserver = socket.socket()
    brodoserver.bind((host, port2))
    print("브로도캐스트 서버가 생성됐습니다.")
    print("")
    print(nowtime + "클라이언트 대기를 시작합니다...")

if __name__ == "__main__":
    serveropen()