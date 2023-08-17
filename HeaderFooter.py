import threading, requests, todo, main, Health, setting
from tkinter import *
from datetime import datetime
from bs4 import BeautifulSoup as bs
from pprint import pprint
from PIL import ImageTk, Image

class Header_footer:
    # write_header 함수를 실행하여 label, button을 출력한다
    def __init__(self, canvas, root, call_main):
        self.canvas = canvas
        self.root = root
        self.write_header()
        self.call_main = call_main
        self.write_footer()

    def write_header(self):
        self.weather_icon = Image.open("img/sun-dynamic.png")
        self.weather_icon = self.weather_icon.resize((100,100)) # 버튼 이미지를 열어서 가져온다
        self.root.weather_icon = ImageTk.PhotoImage(self.weather_icon) # 사진 imagetk 모듈로 변환
        self.waether_posion_label = Label(self.root, font=('NanumGothic', 20), text='부산광역시 강서구 가락동',fg="white", bg="#1b1b1b") # "부산광역시 강서구 가락동"등 위치를 알려주는 문자이다
        self.time_label = Label(self.root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b") # 시분초 출력 label 설정 정의
        self.Yemd_label = Label(self.root, font=('NaumGothic',20), fg="white", bg="#1b1b1b") # 년월일 출력 label 설정 정의
        self.weather_icon_label = Label(self.root, image=self.root.weather_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0) # 날씨 그림을 가져와 출력하는 label 이다
        self.weather_tem_label = Label(self.root, font=('NanumGothic', 30), fg="white", bg="#1b1b1b") # 날씨 온도를 출력하는 label 이다

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


    # ----------- footer line

    def todo_click(self):
        self.black_img = Image.open("img/1B1B1B.png")
        self.black_img = self.black_img.resize((1050, 1200))
        self.root.black_img = ImageTk.PhotoImage(self.black_img)

        self.star_button = Label(self.root,image=self.root.black_img,width=1050,height=1200, bg="white",borderwidth=0, highlightthickness=0)

        self.canvas.create_window(540, 1000, window=self.star_button)
        todo.todo_list(self.canvas, self.root)
    
    def hfile_click(self):
        self.black_img = Image.open("img/1B1B1B.png")
        self.black_img = self.black_img.resize((1050, 1200))
        self.root.black_img = ImageTk.PhotoImage(self.black_img)

        self.star_button = Label(self.root,image=self.root.black_img,width=1050,height=1200, bg="white",borderwidth=0, highlightthickness=0)

        self.canvas.create_window(540, 1000, window=self.star_button)
        Health.HealthReport(self.canvas, self.root)
    def check(self):
        self.black_img = Image.open("img/1B1B1B.png")
        self.black_img = self.black_img.resize((1050, 1200))
        self.root.black_img = ImageTk.PhotoImage(self.black_img)

        self.star_button = Label(self.root,image=self.root.black_img,width=1050,height=1200, bg="white",borderwidth=0, highlightthickness=0)

        self.canvas.create_window(540, 1000, window=self.star_button)
        Health.HealthList(self.canvas, self.root)
    """
    def aram(self):
        self.black_img = Image.open("img/1B1B1B.png")
        self.black_img = self.black_img.resize((1050, 1200))
        self.root.black_img = ImageTk.PhotoImage(self.black_img)

        self.star_button = Label(self.root,image=self.root.black_img,width=1050,height=1200, bg="white",borderwidth=0, highlightthickness=0)

        self.canvas.create_window(540, 1000, window=self.star_button)
        Health.HealthList(self.canvas, self.root)
    """
    def setting(self):
        self.black_img = Image.open("img/1B1B1B.png")
        self.black_img = self.black_img.resize((1050, 1200))
        self.root.black_img = ImageTk.PhotoImage(self.black_img)

        self.star_button = Label(self.root,image=self.root.black_img,width=1050,height=1200, bg="white",borderwidth=0, highlightthickness=0)

        self.canvas.create_window(540, 1000, window=self.star_button)
        setting.setting_menu(self.canvas, self.root)
        
    def write_footer(self):
        footer_ra_img = Image.open("img/footer_ract.png")
        todo_img = Image.open("img/todo.png")
        hfile_img = Image.open("img/hfile.png")
        searcheck_img = Image.open("img/searcheck.png")
        aram_img = Image.open("img/aram.png")
        setting_img = Image.open("img/setting_menu.png")
        # 이미지를 가져온다

        footer_ra_img = footer_ra_img.resize((900, 170))
        todo_img = todo_img.resize((100, 140))
        hfile_img = hfile_img.resize((100, 140))
        searcheck_img = searcheck_img.resize((100, 140))
        aram_img = aram_img.resize((100, 140))
        setting_img = setting_img.resize((100, 140))
        # 이미지 사이즈를 지정한다

        self.root.footer_ra_img = ImageTk.PhotoImage(footer_ra_img)
        self.root.todo_img = ImageTk.PhotoImage(todo_img)
        self.root.hfile_img = ImageTk.PhotoImage(hfile_img)
        self.root.searcheck_img = ImageTk.PhotoImage(searcheck_img)
        self.root.aram_img = ImageTk.PhotoImage(aram_img)
        self.root.setting_img = ImageTk.PhotoImage(setting_img)
        # 이미지를 모듈로 만들어 준다

        self.footer_img_lable = Label(self.root, image=self.root.footer_ra_img, bg="#1b1b1b", borderwidth=0,
                                      highlightthickness=0)
        self.todo_button = Button(self.root, image=self.root.todo_img, bg="#535355", width=100, height=140,
                                  borderwidth=0, highlightthickness=0, command=self.todo_click)
        self.hfile_button = Button(self.root, image=self.root.hfile_img, bg="#535355", width=100, height=140,
                                   borderwidth=0, highlightthickness=0, command=self.hfile_click)
        self.searcheck_button = Button(self.root, image=self.root.searcheck_img, bg="#535355", width=100, height=140,
                                       borderwidth=0, highlightthickness=0, command=self.check)
        self.aram_button = Button(self.root, image=self.root.aram_img, bg="#535355", width=100, height=140,
                                  borderwidth=0, highlightthickness=0)
        self.setting_button = Button(self.root, image=self.root.setting_img, bg="#535355", width=100, height=140,
                                     borderwidth=0, highlightthickness=0, command=self.setting)

        self.canvas.create_window(540, 1750, window=self.footer_img_lable)
        self.canvas.create_window(270, 1750, window=self.todo_button)
        self.canvas.create_window(405, 1750, window=self.hfile_button)
        self.canvas.create_window(540, 1750, window=self.searcheck_button)
        self.canvas.create_window(675, 1750, window=self.aram_button)
        self.canvas.create_window(810, 1750, window=self.setting_button)

    def clean_show(self):
        self.footer_img_lable.pack_forget()
        self.todo_button.pack_forget()
        self.hfile_button.pack_forget()
        self.searcheck_button.pack_forget()
        self.aram_button.pack_forget()
        self.setting_button.pack_forget()


if __name__ == "__main__":
    root = Tk()  # Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b")
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)

    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    test = main.main_menu(canvas, root)
    #Header(canvas, root, test)

    # root.wm_attributes('-fullscreen', 'True') # gui 완성시 주석 삭제
    # 윈도우 상당 바를 없애고 풀스크린 설정 한다
    root.mainloop()