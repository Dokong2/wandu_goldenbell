import threading
import socket
chatserver = None
comserver = None
comlist = {}
# made by wandukong
# ver 1.0

def comsee():
    global comserver,comlist
    print("com 서버 클라이언트 접속 대기중입니다..")
    comserver.listen(2)
    while True:
        comserver.accept(conn,addr)
        print("com 서버에 누군가 접속했습니다. 지금 로그인을 대기 중입니다... 어드레스 : " + str(addr))
        client_login(conn=conn)

def client_login(conn):
    while True:
            logindata = conn.recv(1024).decode()
            if logindata[0:5] == "login":
                comlist[conn] : logindata[6:]
                print("로그인 되었습니다. 아이디 : " + logindata[6:])
        

def serveropen():
    global chatserver
    global comserver
    print("완두완두 골든밸")
    print("")
    print("개인 게임 : 추후 멀티존에 추가됩니다.")
    print("설치 버전 : 1.0")
    print("서버를 오픈하시려면 [start]를 입력하세요.")
    print("서버 매뉴얼을 읽으시려면 [help]를 입력하세요.")
    while True:
        start = input
        if start == "help":
            print("완두골든밸 1.0 기준 서버 매뉴얼입니다.")
            print("통신 서버 포트는 기본 포트가 [8080]입니다.")
            print("채팅 서버 포트는 기본 포트가 [1010]입니다.")
            print("포트로 서버가 열리면 클라이언트를 대기하고 진행상태를 알아서 보고합니다.")
            print("서버 매뉴얼은 이것으로 끝입니다.")
        elif start == "start":
            print("서버 실행중...")
            print("채팅 서버를 생성합니다...")
            print("채팅 서버 포트를 입력하세요.")
            port = input(">>")
            if port == "":
                port = 1010
            chatserver = socket.socket
            chatserver.bind("127.0.0.1",int(port))
            print("채팅 서버이 생성되었습니다. 포트 : " + str(port))
            print("통신 서버를 생성합니다...")
            print("통신 서버 포트를 입력하세요.")
            port = input(">>")
            if port == "":
                port = 8080
            comserver = socket.socket
            comserver.bind("127.0.0.1", int(port))
            print("모든 서버가 생성됐습니다.")
            comsee()

if __name__ == "__main__":
    serveropen()