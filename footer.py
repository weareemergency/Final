"""
    개발 log{
        2023.06.25 이지석
        - footer.py 모듈 제작
    }
    사용 label{  
        footer_img_lable
    }
    button{
        todo_button
        hfile_button
        searcheck_button 
        aram_button
        setting_button
    }
"""

from tkinter import *
from PIL import ImageTk, Image
import todo
import main
class footer_menu:
    def __init__(self, canvas, root, call_main):
        self.canvas = canvas
        self.root = root
        self.call_main = call_main
        self.write_footer()
        # write_header 함수를 실행하여 label, button을 출력한다
        
    def todo_click(self):
        self.call_main.clean_show()
        self.tell_todo = todo.todo_list(self.canvas, self.root)
        
    def write_footer(self):
        footer_ra_img = Image.open("img/footer_ract.png")
        todo_img = Image.open("img/todo.png")
        hfile_img = Image.open("img/hfile.png")
        searcheck_img = Image.open("img/searcheck.png")
        aram_img = Image.open("img/aram.png")
        setting_img = Image.open("img/setting.png")
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
        
        self.footer_img_lable = Label(self.root, image=self.root.footer_ra_img, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.todo_button = Button(self.root, image=self.root.todo_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0, command=self.todo_click)
        self.hfile_button = Button(self.root, image=self.root.hfile_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
        self.searcheck_button = Button(self.root, image=self.root.searcheck_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
        self.aram_button = Button(self.root, image=self.root.aram_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
        self.setting_button = Button(self.root, image=self.root.setting_img, bg="#535355", width=100, height=140, borderwidth=0, highlightthickness=0)
        
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