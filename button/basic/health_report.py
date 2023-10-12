from tkinter import Label, Listbox, Tk, Canvas, BOTH, TRUE, END
from PIL import ImageTk, Image


class HealthReport:
    def __init__(self, can, ro):
        self.canvas = can  # canvas
        self.root = ro   # root

        self.box1 = None
        self.box2 = None
        self.box3 = None
        self.notebook = None

        # label
        self.show_name = None
        self.condition = None
        self.condition_en = None
        self.medicine = None
        self.medicine_en = None
        self.operation = None
        self.operation_en = None

        # listbox
        self.condition_list = None

        self.create_windows()

    def create_windows(self):
        self.load_image()
        self.create_labels()
        self.create_listbox()
        self.place()

    def load_image(self):
        image_path = {
            "notebook": "/Users/byungchan/Desktop/mirror_software/img/notebook.png",  # 노트 이미지
            "box1": "/Users/byungchan/Desktop/mirror_software/img/health_rect1.png",  # 흰색 배경
            "box2": "/Users/byungchan/Desktop/mirror_software/img/health_rect2.png",  # 거북목 (그래프)
            "box3": "/Users/byungchan/Desktop/mirror_software/img/health_rect3.png",  # 라운드숄더 (그래프)
        }

        self.root.notebook = ImageTk.PhotoImage(Image.open(image_path["notebook"]).resize((50, 50)))
        self.root.box1 = ImageTk.PhotoImage(Image.open(image_path["box3"]).resize((918, 174)))
        self.root.box2 = ImageTk.PhotoImage(Image.open(image_path["box2"]).resize((918, 229)))
        self.root.box3 = ImageTk.PhotoImage(Image.open(image_path["box1"]).resize((918, 257)))

    def create_labels(self):
        font_name, bold = "NanumGothic", "bold"
        self.box1 = Label(self.root, image=self.root.box1, bg="#1b1b1b", borderwidth=0, highlightthickness=0)  # 맨 위 배경
        self.box2 = Label(self.root, image=self.root.box2, bg="#1b1b1b", borderwidth=0, highlightthickness=0)  # 중간 배경
        self.box3 = Label(self.root, image=self.root.box3, bg="#1b1b1b", borderwidth=0, highlightthickness=0)  # 맨 아래 배경
        self.notebook = Label(self.root, image=self.root.notebook, bg="#1b1b1b", borderwidth=0, highlightthickness=0)  # 노트 아이콘

        self.show_name = Label(self.root, font=(font_name, 25, bold), text="양유빈님의 건강보고함>", fg="white", bg="#1b1b1b")
        self.condition = Label(self.root, font=(font_name, 23, bold), text="현재 건강 상태",fg="black", bg="white")
        self.condition_en = Label(self.root, font=(font_name, 18, bold), text='Physical condition',fg="#7c7c7c", bg="white")
        self.medicine = Label(self.root, font=(font_name, 23, bold), text='복욕 약 현황',fg="black", bg="white")
        self.medicine_en = Label(self.root, font=(font_name, 18, bold), text='Current status of medication taken',fg="#7c7c7c", bg="white")
        self.operation = Label(self.root, font=(font_name, 23, bold), text='수술 및 시술기록',fg="black", bg="white")
        self.operation_en = Label(self.root, font=(font_name, 18, bold), text='hospital admission records',fg="#7c7c7c", bg="white")

    def create_listbox(self):
        """
        이 부분에 listbox 기능 필요함
        """
        pass

    def place(self):
        # label with text
        self.canvas.create_window(193, 170, window=self.show_name)
        self.canvas.create_window(300, 700, window=self.condition)
        self.canvas.create_window(600, 700, window=self.condition_en)
        self.canvas.create_window(210, 964, window=self.medicine)
        self.canvas.create_window(540, 964, window=self.medicine_en)
        self.canvas.create_window(240, 1200, window=self.operation)
        self.canvas.create_window(520, 1200, window=self.operation_en)

        # label with image
        self.canvas.create_window(540, 200, window=self.box3)
        self.canvas.create_window(540, 420, window=self.box2)
        self.canvas.create_window(540, 660, window=self.box1)
        self.canvas.create_window(260, 620, window=self.notebook)

        # listbox


if __name__=="__main__":
    root = Tk()
    canvas = Canvas(root, bg="#1b1b1b")
    canvas.pack(fill=BOTH, expand=TRUE)
    HealthReport(canvas, root)
    root.geometry("1080x1920")
    root.mainloop()