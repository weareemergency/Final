"""
    개발 log{
        2023.06.25 이지석
        - header.py 모듈 제작
    }
    사용 label{
        time_label //시분초를 출력
        Yemd_label //년월일을 출력
        weather_icon_label //날씨 이미지 출력
        weather_tem_label //온도 출력
        waether_posion_label //지역 표시
    }
"""

from tkinter import *
from datetime import datetime
import threading
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from PIL import ImageTk, Image

class Header_menu:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.write_header()
        # write_header 함수를 실행하여 label, button을 출력한다
        
    def write_header(self):
        self.weather_icon = Image.open("img/sun-dynamic.png")
        self.weather_icon = self.weather_icon.resize((100,100))
        # 버튼 이미지를 열어서 가져온다

        self.root.weather_icon = ImageTk.PhotoImage(self.weather_icon)
        # 사진 imagetk 모듈로 변환
        
        self.waether_posion_label = Label(self.root, font=('NanumGothic', 20), text='부산광역시 강서구 가락동',fg="white", bg="#1b1b1b")
    # "부산광역시 강서구 가락동"등 위치를 알려주는 문자이다
        self.time_label = Label(self.root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b") 
        # 시분초 출력 label 설정 정의
        self.Yemd_label = Label(self.root, font=('NaumGothic',20), fg="white", bg="#1b1b1b")
        # 년월일 출력 label 설정 정의
        self.weather_icon_label = Label(self.root, image=self.root.weather_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        # 날씨 그림을 가져와 출력하는 label 이다
        self.weather_tem_label = Label(self.root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b")
        # 날씨 온도를 출력하는 label 이다
        
        self.Thread_time()
        self.startThread_Ymd()
        self.Thead_weather()
        # 스레드를 생성한다
        
        self.canvas.create_window(130, 100, window=self.time_label)
        self.canvas.create_window(170, 50, window=self.Yemd_label)
        self.canvas.create_window(250, 220, window=self.weather_tem_label) 
        self.canvas.create_window(130, 200, window=self.weather_icon_label)
        self.canvas.create_window(330, 170, window=self.waether_posion_label)
        # label window 에 생성 한다
        
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M")
        self.time_label.config(text=current_time)
        self.Yemd_label.after(1000, self.update_time)
        # 시분초를 가져와 업데이트 하는 함수 이다
    
    def update_Ymd(self):
        current_Ymd = datetime.now().strftime("%y년%m월%d일")
        self.Yemd_label.config(text=current_Ymd)
        self.Yemd_label.after(1000, self.update_Ymd)
        # 년월일을 가져와 업데이트 하는 함수
        
    def Thread_time(self):
        # 시분초 를 출력하는 쓰레드를 생성한다
        thread = threading.Thread(target=self.update_time)
        # thead 사용할 함수를 지정한다
        thread.daemon = True
        # thread 사용을 허용 해준다
        thread.start()
        # thread를 시작한다

    def startThread_Ymd(self):
        # 년월일 쓰레드 생성
        thread = threading.Thread(target=self.update_Ymd)
        # thead 사용할 함수를 지정한다
        thread.daemon = True
        # thread 사용을 허용 해준다
        thread.start()
        #쓰레드를 시작한다
        
    def update_weather(self):
        # 날씨를 지속 적으로 파싱 한다
        html = requests.get('https://search.naver.com/search.naver?query=부산강서구가락동날씨')
        # html 주소를 가져온다
        soup = bs(html.text,'html.parser')
        # 주소로들어간 싸이트를 파싱한다
        # (슬라이싱 작업){
        data1 = soup.find('div',{'class':'temperature_text'})
        data2 = data1.findAll('strong')
        data3=str(data2[0])
        data3= data3[data3.find('</span>')+7:]
        data3=data3[:data3.find('<')]+"°"
        
        icon_data =soup.find('div',{'class':'weather_main'})
        icon_data2 = icon_data.findAll('i')
        icon_data3 = str(icon_data2)
        icon_data3=icon_data3[icon_data3.find('i class')+9:]
        icon_data3=icon_data3[:icon_data3.find('"')]+".png"
        #print(icon_data3)
        # }
        
        self.weather_icon = Image.open("img/weather_img/"+icon_data3)
        self.weather_icon = self.weather_icon.resize((100,100))
        # 버튼 이미지를 열어서 가져온다

        self.root.weather_icon = ImageTk.PhotoImage(self.weather_icon)
        
        self.weather_icon_label.config(image=self.root.weather_icon)
        self.weather_tem_label.config(text=data3)
        self.weather_tem_label.after(600000, self.update_weather)
        # 10분 마다 업데이트 한다
    def Thead_weather(self):
        # 날씨 쓰레드를 생성한다
        thread = threading.Thread(target=self.update_weather)
        # thead 사용할 함수를 지정한다
        thread.daemon = True
        # thread 사용을 허용 해준다
        thread.start()
        #쓰레드를 시작한다