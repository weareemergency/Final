from tkinter import Label, Button, Tk, Canvas, BOTH, TRUE
from PIL import ImageTk, Image


class SettingPart:
    def __init__(self, can, ro):
        self.canvas = can  # canvas
        self.root = ro  # root

        self.show_name = None  # 이름
        # label
        self.label_aram = None
        self.label_medicine = None
        self.label_result = None
        self.label_api = None
        # label with image
        self.setting_icon = None
        self.background = None
        # button
        self.switch_medicine = None
        self.switch_aram = None
        self.switch_result = None
        self.switch_api = None

        self.create_windows()  # 실행

    def create_windows(self):
        self.load_images()
        self.position()

    def load_images(self):
        image_path = {
            "setting_icon": "./img/setting.png",  # 설정 아이콘 (톱니바퀴)
            "background": "./img/Rectangle_setting.png",  # 뒤 배경 (흰색)
            "on": "./img/switch_on.png",  # 스위치 on
            "off": "./img/switch_off.png"  # 스위치 off
        }

        self.root.setting_icon = ImageTk.PhotoImage(Image.open(image_path["setting_icon"]).resize((50, 50)))
        self.root.background = ImageTk.PhotoImage(Image.open(image_path["background"]))
        self.root.on = ImageTk.PhotoImage(Image.open(image_path["on"]))
        self.root.off = ImageTk.PhotoImage(Image.open(image_path["off"]))

    def create_labels(self):
        font_name, bold = "NanumGothic", "bold"
        self.show_name = Label(self.root, font=(font_name, 25, bold), text="양유빈님의 설정 >", fg="white", bg="#1b1b1b")
        self.label_aram = Label(self.root, font=(font_name, 19), text="전체 알림", fg="black", bg="white")
        self.label_medicine = Label(self.root, font=(font_name, 19), text="약 복용 알림", fg="black", bg="white")
        self.label_result = Label(self.root, font=(font_name, 19), text="자세 분석 결과 제공", fg="black", bg="white")
        self.label_api = Label(self.root, font=(font_name, 19), text="API 활성화", fg="black", bg="white")
        self.setting_icon = Label(self.root, image=self.root.setting_icon, bg="#1b1b1b", borderwidth=0, highlightthickness=0)
        self.background = Label(self.root, image=self.root.background, bg="#1b1b1b", borderwidth=0, highlightthickness=0)

    def
        self.switch_aram = Button(self.root, image=self.root.on, bg="white", borderwidth=0, highlightthickness=0)
        self.switch_api = Button(self.root, image=self.root.on, bg="white", borderwidth=0, highlightthickness=0)
        self.switch_medicine = Button(self.root, image=self.root.off, bg="white", borderwidth=0, highlightthickness=0)
        self.switch_result = Button(self.root, image=self.root.on, bg="white", borderwidth=0, highlightthickness=0)

    def position(self):
        self.canvas.create_window(570, 900, window=self.label_api)

        self.canvas.create_window(870, 900, window=self.switch_api)
        self.canvas.create_window(870, 820, window=self.switch_result)
        self.canvas.create_window(870, 740, window=self.switch_medicine)  #
        self.canvas.create_window(870, 660, window=self.switch_aram)  # 스위치 온 (이미지)

        self.canvas.create_window(590, 820, window=self.label_result)
        self.canvas.create_window(550, 740, window=self.label_medicine)  # 약 복용 텍스트
        self.canvas.create_window(534, 660, window=self.label_aram)  # 알람 텍스트

        self.canvas.create_window(700, 815, window=self.background)  # 흰색 배경
        self.canvas.create_window(325, 620, window=self.setting_icon)  # 설정 아이콘
        self.canvas.create_window(218, 620, window=self.show_name)  # 사용자 이름


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, bg="#1b1b1b")
    canvas.pack(fill=BOTH, expand=TRUE)
    SettingPart(canvas, root).create_windows()
    root.geometry("1080x1920")
    root.mainloop()
