"""
    개발 log{
        2023.08.9 이지석
        - ranking.py 모듈 제작
        .......
    }
    사용 label{
        rank_label
        rank_icon
        ract_image
        date_rank 
        line_image 
        people_fi
        people_se
        people_th 
        rank_label1 
        rank_label2 
        rank_label3 
    }
    사용 listbox{
        list_rank
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

class rank_list:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.rank()
         
    def rank(self):
        self.crow_icon = Image.open("img/crow.png")
        self.crow_icon = self.crow_icon.resize((50,50))
        self.root.crow_icon = ImageTk.PhotoImage(self.crow_icon)
        
        self.ract = Image.open("img/rank_rect16.png")
        self.ract = self.ract.resize((915,673))
        self.root.ract = ImageTk.PhotoImage(self.ract)
       
        self.line = Image.open("img/Line1.png")
        self.line = self.line.resize((10,520))
        self.root.line = ImageTk.PhotoImage(self.line)
        
        self.people1 = Image.open("img/people/girl1.png")
        #self.people1 = self.people1.resize((141,164))
        self.root.people1 = ImageTk.PhotoImage(self.people1)
        
        self.people2 = Image.open("img/people/man2.png")
        #self.people2 = self.people2.resize((10,520))
        self.root.people2 = ImageTk.PhotoImage(self.people2)
        
        self.people3 = Image.open("img/people/man1.png")
        #self.people3 = self.line.resize((10,520))
        self.root.people3 = ImageTk.PhotoImage(self.people3)
        
        self.rank_label = Label(self.root, font=('NanumGothic', 25, 'bold'), text='투두 랭킹      >',fg="white", bg="#1b1b1b")
        self.rank_icon = Label(self.root,image=self.root.crow_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.ract_image = Label(self.root, image=self.root.ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.date_rank =  Label(self.root, font=('NanumGothic', 20), text='2023년 5월 15일 12:32분 기준 랭킹입니다.',fg="black", bg="white")
        self.line_image = Label(self.root, image=self.root.line, bg="white",borderwidth=0, highlightthickness=0)
        self.people_fi = Label(self.root,  anchor='w', width=200,height=180,image=self.root.people1,bg="white",borderwidth=0, highlightthickness=0)
        self.people_se = Label(self.root,  anchor='w', width=200,height=180,image=self.root.people2,bg="white",borderwidth=0, highlightthickness=0)
        self.people_th = Label(self.root,  anchor='w', width=200,height=180,image=self.root.people3,bg="white",borderwidth=0, highlightthickness=0)
        self.rank_label1 = Label(self.root, font=('NanumGothic', 23,'bold'),anchor='w',height=5, width=16,text='1위 양유빈님',fg="black", bg="white")
        self.rank_label2 = Label(self.root, font=('NanumGothic', 23,'bold'), anchor='w',height=5, width=16,text='2위 이지석님',fg="black", bg="white")
        self.rank_label3 = Label(self.root, font=('NanumGothic', 23,'bold'), anchor='w',height=5, width=16,text='3위 김병찬님',fg="black", bg="white")
        self.list_rank =  Listbox(self.root, font=('NaumGothic',20,'bold'),width=15, height=15, borderwidth=0,bg="white",highlightthickness=0, justify="center")
        
        self.list_rank.insert(0, '4위 윤동현')
        self.list_rank.insert(END, '')
        self.list_rank.insert(END, '5위 박민성')
        self.list_rank.insert(END, '')
        self.list_rank.insert(END, '6위 이민준')
        self.list_rank.insert(END, '')
        self.list_rank.insert(END, '7위 손정웅')
        self.list_rank.insert(END, '')
        self.list_rank.insert(END, '8위 이윤찬')
        self.list_rank.insert(END, '')
        self.list_rank.insert(END, '.')
        self.list_rank.insert(END, '')
        self.list_rank.insert(END, '.')
        self.list_rank.insert(END, '')
        self.list_rank.insert(END, '.')
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
        
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    header.Header_menu(canvas, root)
    # footer.footer_menu(canvas, root)
    rank_list(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()