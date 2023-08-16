"""
    개발 log{
        2023.07.25 이지석
        - login.py 모듈 제작
    }
    사용 label{
        login_incon_label //로그인 icon 출력
    }
"""
from tkinter import *
import header
from pprint import pprint
from PIL import ImageTk, Image
class login_face:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.login_header()
        # write_header 함수를 실행하여 label, button을 출력한다
        
    def login_header(self):
        self.login_icon = Image.open("img/login.png")
        self.login_icon = self.login_icon.resize((639,194))
        
        self.root.login_icon = ImageTk.PhotoImage(self.login_icon)
        
        self.login_icon_label = Label(self.root, image=self.root.login_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.canvas.create_window(540, 960, window=self.login_icon_label)
        
if __name__=="__main__":
    root = Tk()#Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    header.Header_menu(canvas, root)
    login_face(canvas, root)
    root.geometry("1080x1920")
    # 화면 크기를 지정한다
    root.mainloop()