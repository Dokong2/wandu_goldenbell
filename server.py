import threading
import socket
# made by wandukong
# ver 1.0

def serveropen():
    print("완두완두 골든밸")
    print("개인 게임 : 추후 멀티존에 추가됩니다.")
    print("설치 버전 : 1.0")
    print("서버를 오픈하시려면 [start]를 입력하세요.")
    print("서버 매뉴얼을 읽으시려면 [help]를 입력하세요.")
    while True:
        start = input
        if start == "help":
            print("완두골든밸 1.0 기준 서버 매뉴얼입니다.")
            print("서버1 포트는 기본 포트가 [8080]입니다.")
            print("채팅서버 포트는 기본 1010입니다.")
            print("포트로 서버가 열리면 클라이언트를 대기하고 진행상태를 알아서 보고합니다.")
            print("서버 매뉴얼은 이것으로 끝입니다.")
        elif start == "start":
            print("서버 실행중...")
            print("서버 소켓을 생성합니다...")
            wandu = 
            goldenbellserver = socket.socket
            goldenbellserver.bind("127.0.0.1",)
            print("서버 1이 생성되었습니다. 포트 : 8080")

