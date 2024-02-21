import socket
import threading
import time

def timeupdate():
    global now
    now = time

def nowtime():
    global now
    return now.localtime().tm_hour + " : " + now.localtime().tm_min + " : " + now.localtime().tm_sec + " "

def login():
    print("서버 연결을 시작합니다.")
    print("연결할 서버의 포트를 입력해주세요.")
    host = "127.0.0.1"
    port = int(input(">>"))
    login(host, port)
    print("사용할 이름을 입력해주세요.")
    name = input(">>")
    print("이름이 입력되었습니다.")
    print("서버에 연결을 시작합니다.")
    client = socket.socket()
    client.bind(host, port)
    print("접속 돼었습니다.")
    print("로그인 정보를 서버에게 보내는 중..")
    client.send("login " + name.encode())
    print("정보가 보내졌습니다.")
    print("서버에게 로그인 성공 데이터를 받기를 대기중입니다..")
    loginokdata = client.recv(1024).decode()
    print("서버 내용 : " + loginokdata)
    if loginokdata == "ok":
        print("로그인이 성공되었습니다.")
    else:
        print("로그인에 실패했습니다. 로그인 데이터가 충돌 된 것 같습니다.")
        print("서버에게 서버 재부팅 명령을 보내고 있습니다.")
        client

if __name__ == "__main__":
    login()