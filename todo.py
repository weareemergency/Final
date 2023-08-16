from tkinter import *
from pprint import pprint
from PIL import ImageTk, Image
from pathlib import Path
from tkinter.scrolledtext import ScrolledText
import header
import footer

class todo_list:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.todo()
         
    def todo(self):
        self.todo_ract = Image.open("img/Rect16.png")
        self.todo_ract = self.todo_ract.resize((915, 538))
        self.root.todo_ract = ImageTk.PhotoImage(self.todo_ract)
        
        self.check = Image.open("img/check.png")
        self.check = self.check.resize((49, 49))
        self.root.check = ImageTk.PhotoImage(self.check)
        
        self.check_not = Image.open("img/white_img.jpg")
        self.check_not = self.check_not.resize((49, 49))
        self.root.check_not = ImageTk.PhotoImage(self.check_not)
        
        self.todo_name_label= Label(self.root, text="양유빈님의 투두리스트>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0, justify="left")
        self.todo_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text='To Do List',fg="black", bg="white")
        self.due_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text='Due Date',fg="black", bg="white")
        self.com_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text='Complete',fg="black", bg="white")
        self.todo_ract = Label(self.root, image=self.root.todo_ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        
        self.view_list = Listbox(self.root, font=('NaumGothic',20),width=25, height=13, borderwidth=0,bg="white",highlightthickness=0)
        self.date_list = Listbox(self.root, font=('NaumGothic',20),width=10, height=13, borderwidth=0,bg="white",highlightthickness=0)
        self.check_box = Listbox(self.root, font=('NaumGothic',20),width=2, height=14, borderwidth=0,bg="white",highlightthickness=0)
        
        self.img_list = ScrolledText(self.root, width=10, height=26,borderwidth=0,highlightthickness=0)
        
        self.ranking_Button = Button(self.root, text="랭킹 보러가기>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0, justify="left")
        
        #투두 리스트를 했을경우 check 이미지를 나오게 한다
        self.img_list.image_create(INSERT, image=self.root.check_not)
        self.img_list.insert(INSERT, '\n')
        self.img_list.insert(INSERT, '\n')
        self.img_list.image_create(INSERT, image=self.root.check_not)
        self.img_list.insert(INSERT, '\n')
        self.img_list.insert(INSERT, '\n')
        self.img_list.image_create(INSERT, image=self.root.check_not)
        self.img_list.insert(INSERT, '\n')
        self.img_list.insert(INSERT, '\n')
        self.img_list.image_create(INSERT, image=self.root.check)
        self.img_list.insert(INSERT, '\n')
        self.img_list.insert(INSERT, '\n')
        self.img_list.image_create(INSERT, image=self.root.check)
        self.img_list.insert(INSERT, '\n')
        self.img_list.insert(INSERT, '\n')
        self.img_list.image_create(INSERT, image=self.root.check)
        self.img_list.insert(INSERT, '\n')
        self.img_list.insert(INSERT, '\n')
        
        #투두 리스트 날짜를 입력한다
        self.date_list.insert(0, '2023.05.15')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.17')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.14')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.14')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.14')
        self.date_list.insert(END, '')
        self.date_list.insert(END, '2023.05.14')
        self.date_list.insert(END, '')
        
        #투두 리스트내용을 입력한다
        self.view_list.insert(0, '신경외과 처방약 (디스크)복용')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '프라임 병원 신경과 16:00 내원')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '내과 내원')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '이좋은 치과 내원 (임플란트 검진)')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '도수 치료, 전기충격파 치료')
        self.view_list.insert(END, '')
        self.view_list.insert(END, '양유빈 경험 담')
        
        #listbox 클릭 활성화를 종료한다
        self.view_list.bindtags((self.view_list, self.root, "all"))
        self.date_list.bindtags((self.date_list, self.root, "all"))
        
        self.canvas.create_window(540,1140, window=self.ranking_Button)
        self.canvas.create_window(915,884, window=self.img_list)
        self.canvas.create_window(950, 875, window=self.check_box)
        self.canvas.create_window(330, 890, window=self.view_list)
        self.canvas.create_window(686, 890, window=self.date_list)
        self.canvas.create_window(540, 840, window=self.todo_ract)
        self.canvas.create_window(254, 524, window=self.todo_name_label)
        self.canvas.create_window(180, 630, window=self.todo_lable)
        self.canvas.create_window(670, 630, window=self.due_lable)
        self.canvas.create_window(890, 630, window=self.com_lable)
        
        self.todo_lable.lift()
        self.due_lable.lift()
        self.com_lable.lift()
        self.check_box.lift()
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    header.Header_menu(canvas, root)
    footer.footer_menu(canvas, root)
    todo_list(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()