import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from pprint import pprint
from PIL import ImageTk, Image
from pathlib import Path
from tkinter.scrolledtext import ScrolledText
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from scipy.interpolate import make_interp_spline
from database import Graph

class HealthReport:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.health()

    def health(self):
        self.ract = Image.open("img/health_rect1.png")
        self.ract = self.ract.resize((918, 257))
        self.root.ract = ImageTk.PhotoImage(self.ract)

        self.ract2 = Image.open("img/health_rect2.png")
        self.ract2 = self.ract2.resize((918, 229))
        self.root.ract2 = ImageTk.PhotoImage(self.ract2)

        self.ract3 = Image.open("img/health_rect3.png")
        self.ract3 = self.ract3.resize((910, 174))
        self.root.ract3 = ImageTk.PhotoImage(self.ract3)

        self.note = Image.open("img/notebook.png")
        self.note = self.note.resize((50, 50))
        self.root.note = ImageTk.PhotoImage(self.note)

        self.ract2_image = Label(self.root, image=self.root.ract2, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.ract3_image = Label(self.root, image=self.root.ract3, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.health_label = Label(self.root, font=('NanumGothic', 25, 'bold'), text='건강보고함      >', fg="white",
                                  bg="#1b1b1b")
        self.note_icon = Label(self.root, image=self.root.note, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.ract_image = Label(self.root, image=self.root.ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.health_con = Label(self.root, font=('NanumGothic', 23, 'bold'), text='양유빈님의 현재 건강 상태', fg="black",
                                bg="white")
        self.con_en = Label(self.root, font=('NanumGothic', 18, 'bold'), text='Physical condition', fg="#7c7c7c",
                            bg="white")
        self.con_list = Listbox(self.root, font=('NanumGothic', 21), width=48, height=5, borderwidth=0, bg="white",
                                highlightthickness=0)
        self.medi_list = Listbox(self.root, font=('NanumGothic', 21), width=48, height=4, borderwidth=0, bg="white",
                                 highlightthickness=0)
        self.medi_label = Label(self.root, font=('NanumGothic', 23, 'bold'), text='복욕 약 현황', fg="black", bg="white")
        self.medi_en = Label(self.root, font=('NanumGothic', 18, 'bold'), text='Current status of medication taken',
                             fg="#7c7c7c", bg="white")
        self.surgery_label = Label(self.root, font=('NanumGothic', 23, 'bold'), text='수술 및 시술기록', fg="black",
                                   bg="white")
        self.surgery_en = Label(self.root, font=('NanumGothic', 18, 'bold'), text='hospital admission records',
                                fg="#7c7c7c", bg="white")
        self.surgery_list = Listbox(self.root, font=('NanumGothic', 21), width=48, height=3, borderwidth=0, bg="white",
                                    highlightthickness=0)

        self.con_list.insert(END, '- 올해 3월 경추추간판, 요추추간판 탈출증 초기 및 허리뼈, ')
        self.con_list.insert(END, '  경추의 여좌 및 긴장 판정 후 일주일 입원')
        self.con_list.insert(END, '- 목감기, 코감기 약 일주일째 복용 중')
        self.con_list.insert(END, '- 임플란트 1')

        self.medi_list.insert(END, '- 신경외과: 목디스크, 허리디스크 통증 약 (3일분 남음)')
        self.medi_list.insert(END, '- 내과: 감기약(2일분 남음)')
        self.medi_list.insert(END, '- 피부과 처방약 (8일분 남음)')

        self.surgery_list.insert(END, '- 2012년 편도수술')
        self.surgery_list.insert(END, '- 2023년 목, 허리 디스크 시술')

        self.canvas.create_window(540, 1280, window=self.surgery_list)
        self.canvas.create_window(520, 1200, window=self.surgery_en)
        self.canvas.create_window(240, 1200, window=self.surgery_label)
        self.canvas.create_window(540, 1250, window=self.ract3_image)
        self.canvas.create_window(510, 964, window=self.medi_en)
        self.canvas.create_window(540, 1055, window=self.medi_list)
        self.canvas.create_window(210, 964, window=self.medi_label)
        self.canvas.create_window(540, 1040, window=self.ract2_image)
        self.canvas.create_window(540, 810, window=self.con_list)
        self.canvas.create_window(600, 700, window=self.con_en)
        self.canvas.create_window(300, 700, window=self.health_con)
        self.canvas.create_window(260, 620, window=self.note_icon)
        self.canvas.create_window(193, 620, window=self.health_label)
        self.canvas.create_window(540, 790, window=self.ract_image)


class HealthList:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.health()

    def health(self):
        A = Graph()
        
        result = A.get_health_neck('jiseok')
        
        if result:
            self.ract = Image.open("img/rectangle1.png")
            self.ract = self.ract.resize((918, 645))
            self.root.ract = ImageTk.PhotoImage(self.ract)

            self.leg = Image.open("img/Legend.png")
            self.leg = self.leg.resize((93, 43))
            self.root.leg = ImageTk.PhotoImage(self.leg)

            self.leg2 = Image.open("img/Legend2.png")
            self.leg2 = self.leg2.resize((93, 43))
            self.root.leg2 = ImageTk.PhotoImage(self.leg2)

            self.health_result = Label(self.root, font=('NanumGothic', 25, 'bold'), text='이지석님의 자세 분석 결과   >', fg="white",
                                    bg="#1b1b1b")
            self.rectangle = Label(self.root, image=self.root.ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
            self.date_label = Label(self.root, font=('NanumGothic', 20), width=50, anchor='w', fg="black", bg="white")
            self.check_health = Label(self.root, font=('NanumGothic', 23, 'bold'), width=40, anchor='w', fg="black", bg="white")
            self.details_sub_label = Label(self.root, font=('NanumGothic', 23, 'bold'), text='세부 사항', fg="black",
                                        bg="white")
            self.details_subtitle_label = Label(self.root, font=('NanumGothic', 20), text='Detail', fg="#7c7c7c",
                                                bg="white")
            self.details = Label(self.root, font=('NanumGothic', 18), wraplength=300, width=20, height=9, anchor='nw', fg="black", bg="white", justify='left')
            self.suggestion = Label(self.root, font=('NanumGothic', 22, 'bold'), width=40, justify='center', fg="black",
                                    bg="#ADFFD8")
            self.grap_label1 = Label(self.root, image=self.root.leg, bg="white", borderwidth=0, highlightthickness=0)
            self.grap_label2 = Label(self.root, image=self.root.leg2, bg="white", borderwidth=0, highlightthickness=0)
            
            count = 0
            data = None
            avg_data = None
            
            print(len(result))
            
            if len(result) == 0:
                self.date_label['text'] = "최신 측정을 해주세요"
            elif len(result) < 7:
                self.date_label['text'] = "측정 데이터가 더 필요합니다"
                if result[0][1] < 1:
                    self.check_health['text'] = "거북목이 감지 되었습니다"
                    self.details['text'] = f"- 거북목이 감지 되었습니다.\n" + "- 정확한 측정은 전문가와 상담해주세요"
                    self.suggestion['text'] = "거북목 교정 스트레칭을 하는 것을 추천 드립니다."
                else:
                    self.check_health['text'] = "거북목이 감지 되지 않았습니다"
                    self.details['text'] = f"- 거북목이 감지 되지 않았습니다.\n" + "- 정확한 측정은 전문가와 상담해주세요"
                    self.suggestion['text'] = "꾸준한 운동을 해주세요"
            else:
                for i in result:
                    count = count + 1
                    if data == None:
                        data=i[1]
                    else:
                        if avg_data == None:
                            avg_data = i[1]
                        avg_data = (i[1]+avg_data)/2
                print(data) 
                if data < 1 :
                    self.date_label['text'] = f"{result[6][2]} ~ {result[0][2]} 까지의 데이터로 분석한 결과입니다"
                    if data > avg_data:                 
                        self.check_health['text'] = "저번 측정 대비 자세가 더 약화 되었습니다"
                        self.details['text'] = f"- 거북목이 감지되었지만 전 주 대비향상 되었습니다. 수치는 {data-avg_data} 증가하였습니다. \n" + "- 이대로 유지해주세요. 정확한 측정은 전문가와 상담해주세요"
                    elif data < avg_data:
                        self.check_health['text'] = "저번 측정 대비 자세가 더 악화 되었습니다"
                        self.details['text'] = f"- 거북목이 감지 되었습니다. 수치는 {avg_data-data} 감소하였습니다. \n" + "- 정확한 측정은 전문가와 상담해주세요"
                    self.suggestion['text'] = "거북목 교정 스트레칭을 하는 것을 추천 드립니다."
                else :
                    self.date_label['text'] = f"{result[6][2]} ~ {result[0][2]} 까지의 데이터로 분석한 결과입니다"
                    self.check_health['text'] = "거북목이 감지되지 않았습니다"
            
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
            grap_list = []
            if len(result) < 7:
                self.plot(0, 0, 0, 0, 0, 0, 0)
            else:
                for i in result:
                    if i[1] < 1:
                        grap_list.append(int(i[1]*10))
                    else:
                        grap_list.append(0)
                    print(int(i[1]*10))
                print('heheh')
                print(grap_list)
                # print(int(grap_list[0]))
                # print(int(grap_list[1]))
                # print(int(grap_list[2]))
                # print(int(grap_list[3]))
                # print(int(grap_list[4]))
                # print(int(grap_list[5]))
                # print(int(grap_list[6]))
                # print(type(int(grap_list[0])))
                # self.plot(int(grap_list[0]),int(grap_list[1]),int(grap_list[2]),int(grap_list[3]),int(grap_list[4]),int(grap_list[5]),int(grap_list[6]))
                self.plot(int(grap_list[0]),int(grap_list[1]),int(grap_list[2]),int(grap_list[3]),int(grap_list[4]),int(grap_list[5]),int(grap_list[6]))
            self.grap_label2.lift()
            self.details_sub_label.lift()
            self.details.lift()
            self.grap_label1.lift()
        else:
            print('error')

    def plot(self,sel1, sel2, sel3, sel4, sel5, sel6, sel7):
        # 그래프를 그리는 함수이다
        # 57을 기준으로 표시
        
        fig = Figure(figsize=(6, 3), dpi=100)
        #print(sel)
        x=np.array([1,2,3,4,5,6,7])
        y=np.array([sel1, sel2, sel3, sel4, sel5, sel6, sel7])
        x2=np.array([1,2,3,4,5,6,7])
        y2=np.array([0,0,0,0,0,0,0])
        
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
        self.canvas.get_tk_widget().place(x=82, y=880)


if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b")
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)

    HealthList(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()