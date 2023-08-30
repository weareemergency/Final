import datetime

from tkinter import *
from tkinter import ttk
from pprint import pprint
from PIL import ImageTk, Image
from pathlib import Path
from tkinter.scrolledtext import ScrolledText

from database import TodoDataBase

class RankList:
    def __init__(self, canvas, root):
        self.crow_icon_path = "img/crow.png"
        self.ract_path = "img/rank_rect16.png"
        self.line_path = "img/Line1.png"
        self.people1_path = "img/people/girl1.png"
        self.people2_path = "img/people/man2.png"
        self.people3_path = "img/people/man1.png"

        self.canvas = canvas
        self.root = root
        self.rank()
    
    def image_open(path, resize):
        name = Image.open(path)
        name = name.resize(resize)
        name = ImageTk.PhotoImage(name)

        return name

    def rank(self):
        db = TodoDataBase()
        if db:
            print("MySQL 연결에 성공하였습니다.")

            self.root.crow_icon = RankList.image_open(self.crow_icon_path, (50,50))
            self.root.ract = RankList.image_open(self.ract_path, (916, 673))
            self.root.line = RankList.image_open(self.line_path, (10, 520))
            
            self.people1 = Image.open(self.people1_path)
            self.people2 = Image.open(self.people2_path)
            self.people3 = Image.open(self.people3_path)

            self.root.people1 = ImageTk.PhotoImage(self.people1)
            self.root.people2 = ImageTk.PhotoImage(self.people2)
            self.root.people3 = ImageTk.PhotoImage(self.people3)
            
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            date = datetime.datetime.now().day
            
            self.rank_label = Label(self.root, font=('NanumGothic', 25, 'bold'), text='투두 랭킹      >',fg="white", bg="#1b1b1b")
            self.rank_icon = Label(self.root,image=self.root.crow_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
            self.ract_image = Label(self.root, image=self.root.ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
            self.date_rank =  Label(self.root, font=('NanumGothic', 20), text=f'{year}년 {month}월 {date}일   기준 랭킹입니다.',fg="black", bg="white")
            self.line_image = Label(self.root, image=self.root.line, bg="white",borderwidth=0, highlightthickness=0)
            self.people_fi = Label(self.root,  anchor='w', width=200,height=180,image=self.root.people1,bg="white",borderwidth=0, highlightthickness=0)
            self.people_se = Label(self.root,  anchor='w', width=200,height=180,image=self.root.people2,bg="white",borderwidth=0, highlightthickness=0)
            self.people_th = Label(self.root,  anchor='w', width=200,height=180,image=self.root.people3,bg="white",borderwidth=0, highlightthickness=0)
            text = f"."
            self.rank_label1 = Label(self.root, font=('NanumGothic', 23,'bold'),anchor='w',height=5, width=16,text=text,fg="black", bg="white")
            self.list_rank =  Listbox(self.root, font=('NaumGothic',20,'bold'),width=15, height=15, borderwidth=0,bg="white",highlightthickness=0, justify="center")
            self.rank_label2 = Label(self.root, font=('NanumGothic', 23,'bold'), anchor='w',height=5, width=16,text=text,fg="black", bg="white")
            self.rank_label3 = Label(self.root, font=('NanumGothic', 23,'bold'), anchor='w',height=5, width=16,text=text,fg="black", bg="white")
            data = db.select_rank()
            for i in range(len(data)):
                if i == 0:
                    self.rank_label1.config(text=f'1위 {data[i][0]}님')
                elif i==1:
                    self.rank_label2.config(text=f'2위 {data[i][0]}님')
                elif i == 2:
                    self.rank_label3.config(text=f'3위 {data[i][0]}님')
                else:
                    self.list_rank.insert(END, f'{i+1}위 {data[i][0]}님')
                    self.list_rank.insert(END, '')
            
            self.list_rank.bindtags((self.list_rank, self.root, "all"))
                
            self.canvas.create_window(800, 1030, window=self.list_rank)
            self.canvas.create_window(200, 850, window=self.people_fi)
            self.canvas.create_window(200, 1031, window=self.people_se)
            self.canvas.create_window(200, 1212, window=self.people_th)
            self.canvas.create_window(450, 850, window=self.rank_label1)
            self.canvas.create_window(450, 1031, window=self.rank_label2)
            self.canvas.create_window(450, 1212, window=self.rank_label3)
            self.canvas.create_window(620, 1030, window=self.line_image)
            self.canvas.create_window(183, 620, window=self.rank_label)
            self.canvas.create_window(235, 620, window=self.rank_icon)
            self.canvas.create_window(540, 990, window=self.ract_image)
            self.canvas.create_window(370,700, window=self.date_rank)
        else:
            print("DB 연결 안됨")
            
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    # footer.footer_menu(canvas, root)
    #(canvas, root)
    RankList(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()