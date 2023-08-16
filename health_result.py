"""
    개발 log{
        2023.08.9 이지석
        - health_result.py 모듈 제작
        .......
    }
    사용 label{
        
    }
    사용 listbox{
        
    }
"""

from tkinter import *
from pprint import pprint
from PIL import ImageTk, Image
import header
import footer
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pprint import pprint
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from scipy.interpolate import make_interp_spline

class health_list:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.health()
         
    def health(self):
        self.ract = Image.open("img/rectangle1.png")
        self.ract = self.ract.resize((918,645))
        self.root.ract = ImageTk.PhotoImage(self.ract)
        
        self.leg = Image.open("img/Legend.png")
        self.leg = self.leg.resize((93,43))
        self.root.leg = ImageTk.PhotoImage(self.leg)
        
        self.leg2 = Image.open("img/Legend2.png")
        self.leg2 = self.leg2.resize((93,43))
        self.root.leg2 = ImageTk.PhotoImage(self.leg2)
        
        self.health_result = Label(self.root, font=('NanumGothic', 25, 'bold'), text='양유빈님의 자세 분석 결과   >',fg="white", bg="#1b1b1b")
        self.rectangle = Label(self.root, image=self.root.ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.date_label = Label(self.root, font=('NanumGothic', 20), width=50, anchor='w',text='2022년 5월까지의 데이터로 분석한 결과입니다',fg="black", bg="white")
        self.check_health = Label(self.root, font=('NanumGothic', 23, 'bold'), width=40, anchor='w',text='전주 대비 자세가 더 약화 되었습니다.',fg="black", bg="white")
        self.details_sub_label = Label(self.root, font=('NanumGothic', 23, 'bold'),  text='세부 사항',fg="black", bg="white")
        self.details_subtitle_label = Label(self.root, font=('NanumGothic', 20),  text='Detail',fg="#7c7c7c", bg="white")
        self.details = Label(self.root, font=('NanumGothic', 18),  wraplength=300,width=20, height=9,anchor='nw',text="",fg="black", bg="white", justify='left')
        self.suggestion = Label(self.root, font=('NanumGothic', 22,'bold'), width=40,justify='center',fg="black", bg="#ADFFD8")
        self.grap_label1 = Label(self.root, image = self.root.leg, bg="white", borderwidth=0, highlightthickness=0)
        self.grap_label2 = Label(self.root, image = self.root.leg2, bg="white", borderwidth=0, highlightthickness=0)
        self.details['text']="- 전 주 대비 라운드숄더가 더 심해졌습니다. 수치는 11.8 증가하였습니다. \n"+ "- 거북목 자세는 전 주 대비향상 되었습니다."
        self.suggestion['text']="라운드 숄더 교정 스트레칭을 하는 것을 추천 드립니다."
        
        self.canvas.create_window(250, 1170, window=self.grap_label2)
        self.canvas.create_window(360, 1170, window=self.grap_label1)
        self.canvas.create_window(540, 1230, window=self.suggestion)
        self.canvas.create_window(810, 1060, window=self.details)
        self.canvas.create_window(830, 900, window=self.details_subtitle_label)
        self.canvas.create_window(720, 900, window=self.details_sub_label)
        self.canvas.create_window(505, 760, window=self.check_health)
        self.canvas.create_window(525, 720, window=self.date_label)
        self.canvas.create_window(285, 620, window=self.health_result)
        self.canvas.create_window(540, 980, window=self.rectangle)
        
        self.plot()
        
        self.grap_label2.lift()
        self.details_sub_label.lift()
        self.details.lift()
        self.grap_label1.lift()
    def plot(self):
        # 그래프를 그리는 함수이다
        fig = Figure(figsize = (6, 3),dpi = 100)
        
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
        plot1.plot(xs, ys,zorder=50, color = 'green')
        plot1.plot(xs2, ys2,zorder=50, color = 'blue')
        
        plot1.axis('off')
        #plot1.legend()
        # 그래프에서 축을 삭제한다
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)  
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=82,y=880)
        
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    header.Header_menu(canvas, root)
    # footer.footer_menu(canvas, root)
    health_list(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()