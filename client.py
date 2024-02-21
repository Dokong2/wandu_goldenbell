import socket
import threading
import time
version = "4.5"
# 아침시리얼아침시리얼아침시리얼아침시리얼아침시리얼아침시리얼아침시리얼아침시리얼아침시리얼아침시리얼아침시리얼아침시리얼

def start():
    print("완두 골든밸 : 문제를 맞추자!")
    print("설치 버전 : " + version)
    print("서버에 로그인하려면 [login]을 입력하세요.")
    print("명령어 모음을 보시려면 [cmdlist]를 입력하세요.")
    startcmd = input(">>")
    if startcmd == "login":
        login()
    elif startcmd == "cmdlist":
        cmdlist()
        
def cmdlist():
    print("버전 [" + version + "] 기준 명령어 리스트입니다.")
    print("[login] : 서버에 로그인합니다.")
    print("[cmdlist] : 명령어 리스트를 봅니다.")

def login():
    print("로그인을 시작합니다.")
    print("닉네임을 입력하세요.")
    name = input(">>")
    print("통신 서버의 포트를 입력하세요.")
    host = socket.gethostname()
    port = int(input(">>"))
    print("로그인 서버의 포트를 입력하세요.")
    port2 = int(input(">>"))
    com_socket = socket.socket()
    login_socket = socket.socket()
    com_socket.connect((host, port))
    login_socket.connect((host, port2))
    print("로그인을 시작합니다.")
    print("로그인 중...")
    login_socket.send("login " + name.encode())
    print("로그인 데이터를 전송했습니다.")
    data = login_socket.recv(1024).decode()
    if data == "loginok":
        print("로그인이 성공되었습니다.")
    else:
        print("로그인이 실패되었습니다.")
        print("아마 통신 충돌이 난 것 같습니다.")
        print("다중 동시로그인시 충돌이 날 수 있습니다.")
        print("서버에게 셧다운 신호를 보내는중..")
        login_socket.send("close".encode())

if __name__ == "__main__":
    start()