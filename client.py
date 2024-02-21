import socket
import threading
import time

def timeupdate():
    global now
    now = time

def nowtime():
    global now
    return now.localtime().tm_hour + " : " + now.localtime().tm_min + " : " + now.localtime().tm_sec + " "

def serverconnect():
    print("서버 연결을 시작합니다.")
    print("연결할 서버의 포트를 입력해주세요.")
    host = "127.0.0.1"
    port = int(input(">>"))
    login(host, port)

def login(host, port):
    print("사용할 이름을 입력해주세요.")
    name = input(">>")
    print("이름이 입력되었습니다.")
    print("서버에 연결을 시작합니다.")


if __name__ == "__main__":
    serverconnect()