from tkinter import Label, Button, Tk, Canvas, BOTH, TRUE
from PIL import ImageTk, Image


class TodoPart:
    def __init__(self, can, ro):
        self.canvas = can  # canvas
        self.root = ro  # root

        self.show_name = None
        self.todo_list = None
        self.due_date = None
        self.is_complete = None

        self.image_load()

    def image_load(self):
        image_path = {
            "complete": "/Users/byungchan/Desktop/mirror_software/img/check.png",  # todo 완료
            "not_complete": "/Users/byungchan/Desktop/mirror_software/img/ai_rect.png",  # todo 미완료
            "background_white": "/Users/byungchan/Desktop/mirror_software/img/Rect16.png",  # 흰색 배경
            "background_black": "/Users/byungchan/Desktop/mirror_software/img/1B1B1B.png"  # 검은색 배경
        }

        self.root.complete = ImageTk.PhotoImage(Image.open(image_path["complete"]).resize((49, 49)))
        self.root.not_complete = ImageTk.PhotoImage(Image.open(image_path["not_complete"]).resize((49, 49)))
        self.root.background_white = ImageTk.PhotoImage(Image.open(image_path["background_white"]).resize((915, 538)))
        self.root.background_black = ImageTk.PhotoImage(Image.open(image_path["background_black"]).resize((1050, 1200)))

    def create_labels(self):
        eng_font, kor_font, bold = "Noto Sans", "NaumGothic", "bold"
        self.show_name = Label(self.root, text="양유빈님의 성공 현황", font=(kor_font, 25), bg="#1b1b1b", fg="white", borderwidth=0, highlightthickness=0, justify="left")
        self.todo_list = Label(self.root, font=(eng_font, 16, bold), text="Todo List", fg="black", bg="white")
        self.due_date = Label(self.root, font=(eng_font, 16, bold), text="Due Date", fg="black", bg="white")
        self.is_complete = Label(self.root, font=(eng_font, 16, bold), text="Complete", fg="black", bg="white")

        self.canvas.create_window(540, 840, window=self.root.background_white)
        self.canvas.create_window(200, 524, window=self.show_name)
        self.canvas.create_window(180, 630, window=self.todo_list)
        self.canvas.create_window(670, 630, window=self.due_date)
        self.canvas.create_window(890, 630, window=self.is_complete)


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, bg="#1b1b1b")
    canvas.pack(fill=BOTH, expand=TRUE)
    TodoPart(canvas, root).create_labels()
    root.geometry("1080x1920")
    root.mainloop()