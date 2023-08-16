from tkinter import *
from PIL import ImageTk, Image
import main
import footer
class Menu_start:
    def __init__(self, canvas, root, mode):
        self.canvas = canvas
        self.root = root
        self.mode = mode
        self.box_page()
    def box_page(self):
        self.black_img = Image.open("img/1B1B1B.png")
        self.black_img = self.black_img.resize((1060, 1640))
        self.root.black_img = ImageTk.PhotoImage(self.black_img)
        #1b1b1b
        self.star_button = Button(self.root,font=('NaumGothic',25), image=self.root.black_img,width=1050,height=1630, bg="white",fg="white",borderwidth=0, highlightthickness=0, command=self.movepage)
        self.star_button_window=self.canvas.create_window(540, 1100, window=self.star_button)
    def movepage(self):
        # 버튼 클릭시 star_button 을 삭제 한다
        self.canvas.delete(self.star_button_window)
        self.mode=0
        self.main_call=main.main_menu(self.canvas, self.root)    
        footer.footer_menu(self.canvas, self.root,self.main_call)
    def clean(self):
        self.star_button.pack_forget()