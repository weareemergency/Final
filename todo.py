from tkinter import *
from pprint import pprint
from PIL import ImageTk, Image
from pathlib import Path
from tkinter.scrolledtext import ScrolledText

from ranking import RankList
from database import TodoDataBase
# import footer

class TodoList:
    def __init__(self, canvas, root):
        # Image path & resize init 
        self.todo_image_path = "img/Rect16.png"
        self.check_image_path = "img/check.png"
        self.check_not_image_path = "img/ai_rect.png"
        self.black_img_path = "img/1B1B1B.png"
        self.resize915_538 = (915, 538)
        self.resize49_49 = (49, 49)
        self.resize1050_1200 = (1050, 1200)

        # base
        self.canvas = canvas
        self.root = root
        self.todo()
    
    def ranking_go(self):
        black_img = Image.open(self.black_img_path)
        black_img = black_img.resize(self.resize1050_1200)
        self.root.black_img = ImageTk.PhotoImage(black_img)

        star_button = Label(self.root,image=self.root.black_img,width=1050,height=1200, bg="white",borderwidth=0, highlightthickness=0)

        self.canvas.create_window(540, 1000, window=star_button)
        RankList(self.canvas, self.root)

    def image_open(path, resize):
        name = Image.open(path)
        name = name.resize(resize)
        name = ImageTk.PhotoImage(name)
        
        return name

    def todo(self):
        self.root.todo_ract = TodoList.image_open(self.todo_image_path, self.resize915_538)
        root.check = TodoList.image_open(self.check_image_path, self.resize49_49)
        root.check_not = TodoList.image_open(self.check_not_image_path, self.resize49_49)
        
        self.todo_name_label= Label(self.root, text="투두리스트>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0, justify="left")
        self.todo_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text="Todo List",fg="black", bg="white")
        self.due_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text="Due Date",fg="black", bg="white")
        self.com_lable = Label(self.root, font=('Noto Sans', 16, 'bold'), text="Complete",fg="black", bg="white")
        self.todo_ract = Label(self.root, image=self.root.todo_ract, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        myranking = Label(self.root, text="양유빈님의 현재 38개의 투두 리스트를 완료하였으며 랭킹은 1위입니다.",
                          font=('NaumGothic',19),bg="#1b1b1b",fg="white",borderwidth=0, highlightthickness=0, justify="center")
        self.ranking_Button = Button(self.root, text="랭킹 보러가기>",font=('NaumGothic',25),bg="#1b1b1b",fg="white",
                                    borderwidth=0, highlightthickness=0, justify="left", command=self.ranking_go)
        texts = [
                    ['신경외과 처방약 (디스크) 복용', '2023.05.15','N'], 
                    ['프라임 병원 신경과 16:00 내원','2023.05.15','N'],
                    ['내과 내원','2023.05.15','Y'], 
                    ['이좋은 치과 내원 (임플란트 검진)','2023.05.15','Y'],
                    ['도수 치료, 전기충격파 치료','2023.05.15','Y'] ,
                    ['피부과 내원','2023.05.15','Y']
                ]
        
        todo_list= []
        todo_Date = []
        todo_check = []
        count = 0
        
        for text in texts:
            todo_list.append(Label(self.root, font=('NaumGothic', 19), text=text[0] , width=32, fg="black", bg="white", anchor="w"))
            todo_Date.append(Label(self.root, font=('NaumGothic', 19), text=text[1] , width=10, fg="black", bg="white", anchor="w"))
            if text[2] == 'Y':
                todo_check.append(Button(self.root,image=root.check,bg="white",borderwidth=0, highlightthickness=0))
            else:
                todo_check.append(Button(self.root,image=root.check_not,width=49,height=49,bg="white",borderwidth=0, highlightthickness=0))
            count = count +1
        
        self.canvas.create_window(540,1140, window=myranking)
        self.canvas.create_window(540,1190, window=self.ranking_Button)
        self.canvas.create_window(540, 840, window=self.todo_ract)
        self.canvas.create_window(200, 524, window=self.todo_name_label)
        self.canvas.create_window(180, 630, window=self.todo_lable)
        self.canvas.create_window(670, 630, window=self.due_lable)
        self.canvas.create_window(890, 630, window=self.com_lable)
        
        # 초기 높이 설정
        height = 710
        # 입력된 열만큼 출력한다
        for i in range(0, count):
            self.canvas.create_window(364, height, window=todo_list[i])
            self.canvas.create_window(690, height, window=todo_Date[i])
            self.canvas.create_window(900, height, window=todo_check[i])
            height = height  + 50
        
        self.todo_lable.lift()
        self.due_lable.lift()
        self.com_lable.lift()

if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    #header.Header_menu(canvas, root)
    #footer.footer_menu(canvas, root)
    TodoList(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()