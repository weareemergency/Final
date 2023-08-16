"""
    개발 log{
        2023.06.26 이지석
        - main.py 모듈 제작
    }
    사용 label{  
        grap_result_label   # "자세 분석 결과:" 문자를 출력
        grap_vare_label     # "전주 대비 향상 되었습니다!" 등 결과를 문자로 출력
        crow_img_label      # 랭크 화면의 이미지를 출력
        list_label          # 1위 랭크를 출력
        list_rank_lable     # 2등 랭크를 출력
        list_rank2_lable    # 3등 랭크를 출력
    }
    button{
        button              # 영상들을 추천하는 그림을 출력
        ract_img_button     # 자세분석 결과 박스 출력
        ract2_img_button    # 투두 리스트 박스 출력
    }
"""

from tkinter import *
import numpy as np
from PIL import ImageTk, Image
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pprint import pprint
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from scipy.interpolate import make_interp_spline

class main_menu:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.write_main()
        
    def write_main(self):
        self.ract_img2 = Image.open("img/Rectangle.png")
        self.ract_img2 = self.ract_img2.resize((300, 260))
        
        self.ract_img = Image.open("img/ract-1.png")
        self.ract_img = self.ract_img.resize((560,260))
        
        self.crow_img = Image.open("img/crow.png")
        self.crow_img = self.crow_img.resize((70,70))
        
        self.btn_inactive = Image.open("img/main2.png")
        self.btn_inactive = self.btn_inactive.resize((900, 260))
        # 이미지를 가져오고 사이즈를 지정 한다
        
        self.root.btn_inactive = ImageTk.PhotoImage(self.btn_inactive)
        self.root.ract_img = ImageTk.PhotoImage(self.ract_img)
        self.root.ract_img2 = ImageTk.PhotoImage(self.ract_img2)
        self.root.crow_img  = ImageTk.PhotoImage(self.crow_img)
        # 이미지를 모듈로 만들어 준다
        
        self.health_check_button = Button(self.root, text="양유빈 님의 건강 상태를 확인하세요>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0)
        
        self.grap_result_label = Label(self.root, font=('NanumGothic', 27,'bold') ,text='자세 분석 결과:',fg="black", bg="white")
        # "자세 분석 결과:" 문자를 출력하는 label 이다
        self.grap_vare_label = Label(self.root, font=('NanumGothic', 20), text='전주 대비 향상 되었습니다!',fg="black", bg="white")
        # "전주 대비 향상 되었습니다!" 등 결과를 문자로 출력하는 label 이다
        self.button = Button(self.root, image=self.root.btn_inactive, bg="#1b1b1b", width=900, height=260, borderwidth=0, highlightthickness=0)
        # 영상들을 추천하는 그림을 출력하는 button 이다
        self.ract_img_button = Button(self.root, image=self.root.ract_img, bg="#1b1b1b", width=560, height=260, borderwidth=0, highlightthickness=0)
        # 자세분석 결과 박스를 만드는 button 이다
        self.ract2_img_button = Button(self.root, image=self.root.ract_img2, bg="#1b1b1b", width=300, height=260, borderwidth=0, highlightthickness=0)
        # 투두 리스트 박스를 만드는 button 이다
        self.crow_img_label = Label(self.root, image = self.root.crow_img, bg="white", borderwidth=0, highlightthickness=0)
        # 랭크 화면의 이미지를 출력하는 label 이다
        self.list_label = Label(self.root, font=('NanumGothic', 20, 'bold') ,text='현재 양유빈님이\n투두 1등 입니다',fg="black", bg="white")
        # 1위 랭크를 출력하는 label 이다
        self.list_rank_lable = Label(self.root, font=('NanumGothic', 17), text='2등 이지석님',fg="black", bg="white")
        # 2등 랭크를 출력하는 label 이다
        self.list_rank2_lable = Label(self.root, font=('NanumGothic', 17), text='3등 양성웅님',fg="black", bg="white")
        # 3등 랭크를 출력하는 label 이다
        
        self.canvas.create_window(540, 750, window=self.button)
        self.canvas.create_window(373, 1040, window=self.ract_img_button)
        self.canvas.create_window(250, 960, window=self.grap_result_label)
        self.canvas.create_window(285, 1000, window=self.grap_vare_label)
        self.canvas.create_window(838, 1040, window=self.ract2_img_button)
        self.canvas.create_window(740, 970, window=self.crow_img_label)
        self.canvas.create_window(880,975, window=self.list_label)
        self.canvas.create_window(840, 1070, window=self.list_rank_lable)
        self.canvas.create_window(840, 1100, window=self.list_rank2_lable)
        self.canvas.create_window(360, 590, window=self.health_check_button)
        
        self.grap_result_label.lift()
        self.grap_vare_label.lift()
        
        self.plot()
        
    def plot(self):
        # 그래프를 그리는 함수이다
        fig = Figure(figsize = (5, 1),dpi = 100)
        
        x=np.array([1,2,3,4,5,6,7])
        y=np.array([100,100,100,100,10,10,50])
        x2=np.array([1,2,3,4,5,6,7])
        y2=np.array([0,0,0,100,50,50,50])
        
        model=make_interp_spline(x, y)
        model2=make_interp_spline(x2, y2)
        
        xs=np.linspace(1,7,500)
        ys=model(xs)
        
        xs2=np.linspace(1,7,500)
        ys2=model2(xs2)
        plt.rcParams['font.family'] = 'NanumGothic'
        plot1 = fig.add_subplot(111)
        plot1.plot(xs, ys,zorder=50, color = 'green',label='거북목')
        plot1.plot(xs2, ys2,zorder=50, color = 'blue',label='목디스크')
        
        plot1.axis('off')
        plot1.legend()
        # 그래프에서 축을 삭제한다
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)  
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=110,y=1040)
        
    def clean_show(self):
        # 위젯을 pack으로 전부 생성 한다
        self.button.pack()
        self.button.pack_forget()
        self.ract_img_button.pack()
        self.grap_result_label.pack()
        self.grap_vare_label.pack()
        self.ract2_img_button.pack()
        self.crow_img_label.pack()
        self.list_label.pack()
        self.list_rank_lable.pack()
        self.list_rank2_lable.pack()
        self.health_check_button.pack()
        self.canvas.get_tk_widget().place()
        self.canvas.get_tk_widget().place_forget()
        
        #생성한 위젯을 hide 를 한다
        self.ract_img_button.pack_forget()
        self.grap_result_label.pack_forget()
        self.grap_vare_label.pack_forget()
        self.ract2_img_button.pack_forget()
        self.crow_img_label.pack_forget()
        self.list_label.pack_forget()
        self.list_rank_lable.pack_forget()
        self.list_rank2_lable.pack_forget()
        self.health_check_button.pack_forget()
        print('clean')