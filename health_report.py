"""
    개발 log{
        2023.08.9 이지석
        - ranking.py 모듈 제작
        .......
    }
    사용 label{
        
    }
    사용 listbox{
        
    }
"""

from tkinter import *
from tkinter import ttk
from pprint import pprint
from PIL import ImageTk, Image
from pathlib import Path
from tkinter.scrolledtext import ScrolledText
import header
import footer

class health_list:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.health()
         
    def health(self):
        self.ract = Image.open("img/health_rect1.png")
        self.ract = self.ract.resize((918,257))
        self.root.ract = ImageTk.PhotoImage(self.ract)
        
        self.ract2 = Image.open("img/health_rect2.png")
        self.ract2 = self.ract2.resize((918,229))
        self.root.ract2 = ImageTk.PhotoImage(self.ract2)
        
        self.ract3 = Image.open("img/health_rect3.png")
        self.ract3 = self.ract3.resize((910,174))
        self.root.ract3 = ImageTk.PhotoImage(self.ract3)
        
        self.note = Image.open("img/notebook.png")
        self.note = self.note.resize((50,50))
        self.root.note = ImageTk.PhotoImage(self.note)
        
        self.ract2_image = Label(self.root, image=self.root.ract2, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.ract3_image = Label(self.root, image=self.root.ract3, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.health_label = Label(self.root, font=('NanumGothic', 25, 'bold'), text='건강보고함      >',fg="white", bg="#1b1b1b")
        self.note_icon = Label(self.root,image=self.root.note, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.ract_image = Label(self.root, image=self.root.ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.health_con = Label(self.root, font=('NanumGothic', 23, 'bold'), text='양유빈님의 현재 건강 상태',fg="black", bg="white")
        self.con_en = Label(self.root, font=('NanumGothic', 18, 'bold'), text='Physical condition',fg="#7c7c7c", bg="white")
        self.con_list = Listbox(self.root, font=('NanumGothic', 21) ,width=48, height=5, borderwidth=0,bg="white",highlightthickness=0)
        self.medi_list = Listbox(self.root, font=('NanumGothic', 21) ,width=48, height=4, borderwidth=0,bg="white",highlightthickness=0)
        self.medi_label = Label(self.root, font=('NanumGothic', 23, 'bold'), text='복욕 약 현황',fg="black", bg="white")
        self.medi_en = Label(self.root, font=('NanumGothic', 18, 'bold'), text='Current status of medication taken',fg="#7c7c7c", bg="white")
        self.surgery_label = Label(self.root, font=('NanumGothic', 23, 'bold'), text='수술 및 시술기록',fg="black", bg="white")
        self.surgery_en = Label(self.root, font=('NanumGothic', 18, 'bold'), text='hospital admission records',fg="#7c7c7c", bg="white")
        self.surgery_list = Listbox(self.root, font=('NanumGothic', 21) ,width=48, height=3, borderwidth=0,bg="white",highlightthickness=0)
        
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
        self.canvas.create_window(540,1250, window=self.ract3_image)
        self.canvas.create_window(510,964, window=self.medi_en)
        self.canvas.create_window(540,1055, window=self.medi_list)
        self.canvas.create_window(210,964, window=self.medi_label)
        self.canvas.create_window(540,1040, window=self.ract2_image)
        self.canvas.create_window(540, 810, window=self.con_list)
        self.canvas.create_window(600,700, window=self.con_en)
        self.canvas.create_window(300,700, window=self.health_con)
        self.canvas.create_window(260, 620, window=self.note_icon)
        self.canvas.create_window(193, 620, window=self.health_label)
        self.canvas.create_window(540, 790, window=self.ract_image)
        
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