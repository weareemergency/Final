from tkinter import *
import main
import HeaderFooter
mode = 1

if __name__=="__main__":
    root = Tk()#Tk 생성
    
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b") 
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    
    root.geometry("1080x1920") #540
    # 화면 크기를 지정한다
    
    mode = 1
    HeaderFooter.Header_footer(canvas,root, mode)
    main_id=main.main_menu(canvas, root)
    
    # root.wm_attributes('-fullscreen', 'True') # gui 완성시 주석 삭제
    # 윈도우 상당 바를 없애고 풀스크린 설정 한다
    
    root.mainloop()