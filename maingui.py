"""
    2023-05-02 개발 시작
    코드 참여자 이지석, 양유빈
    개발 log{
        2023.05.04 이지석
        - 시간 가져오기 및 표시
        2023.05.08 이지석
        - ract-1.png를 button 추가
        2023.05.15 이지석
        - gui 멈춤 문제 해결
        2023.05.29 이지석
        - grap, 하단바 구현
        2023.06.25 이지석
        - code 모듈화 진행
    }
    github: https://github.com/weareemergency/python_tkinter.git
    코드 다운방법
    git clone https://github.com/weareemergency/python_tkinter.git
    프로젝트 싸이트:https://juniper-jumbo-de1.notion.site/python-52d9227c31c340249c001f0698a77eac
    설명:
    python tkinter 을 사용해서 의료용스마트 미러 
    main화면 gui를 만드는 코드 이다.
"""

from tkinter import *
import header
import main
import footer
import start_main

mode = 1

if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    header.Header_menu(canvas, root)
    start_main.Menu_start(canvas, root, mode)
    
    # root.wm_attributes('-fullscreen', 'True') # gui 완성시 주석 삭제
    # 윈도우 상당 바를 없애고 풀스크린 설정 한다
    root.mainloop()