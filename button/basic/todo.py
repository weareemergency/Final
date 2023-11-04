from tkinter import Label, Tk, Canvas, BOTH, TRUE
from PIL import ImageTk, Image

from ..database.database import DataBase


class TodoPart:
    def __init__(self, can, ro):
        self.canvas = can  # canvas
        self.root = ro  # root
        # label
        self.show_name = None
        self.todo_list = None
        self.due_date = None
        self.is_complete = None
        self.white_background = None

        self.get_value()

    def create_windows(self):
        self.load_image()
        self.create_labels()
        self.place()

    def load_image(self):
        image_path = {
            "completed": "/Users/byungchan/Desktop/mirror_software/img/check.png",  # 체크 표시
            "not_completed": "/Users/byungchan/Desktop/mirror_software/img/ai_rect.png",  # 미완료 표시
            "background": "/Users/byungchan/Desktop/mirror_software/img/Rect16.png",  # 흰색 배경
        }

        self.root.completed = ImageTk.PhotoImage(Image.open(image_path["completed"]).resize((49, 49)))
        self.root.not_completed = ImageTk.PhotoImage(Image.open(image_path["not_completed"]).resize((49, 49)))
        self.root.white_background = ImageTk.PhotoImage(Image.open(image_path["background"]).resize((915, 538)))

    def create_labels(self):
        self.show_name = Label(self.root, text="투두리스트>", font=('NaumGothic', 25), bg="#1b1b1b", fg="white",
                               borderwidth=0, highlightthickness=0, justify="left")
        self.todo_list = Label(self.root, font=('Noto Sans', 16, 'bold'), text="Todo List", fg="black", bg="white")
        self.due_date = Label(self.root, font=('Noto Sans', 16, 'bold'), text="Due Date", fg="black", bg="white")
        self.is_complete = Label(self.root, font=('Noto Sans', 16, 'bold'), text="Complete", fg="black", bg="white")
        self.white_background = Label(self.root, image=self.root.white_background, bg="#1b1b1b", borderwidth=0,
                                      highlightthickness=0)

    def get_value(self):  # db 값 불러오는
        database = DataBase
        database.load_todo_data()

    def place(self):
        self.todo_list.lift()
        self.due_date.lift()
        self.is_complete.lift()

        self.canvas.create_window(200, 524, window=self.show_name)
        self.canvas.create_window(180, 630, window=self.todo_list)
        self.canvas.create_window(670, 630, window=self.due_date)
        self.canvas.create_window(890, 630, window=self.is_complete)
        self.canvas.create_window(540, 840, window=self.white_background)


if __name__ == "__main__":
    root = Tk()  # Tk 생성
    canvas = Canvas(root, bg="#1b1b1b")
    canvas.pack(fill=BOTH, expand=TRUE)
    TodoPart(canvas, root)
    root.geometry("1080x1920")
    root.mainloop()
