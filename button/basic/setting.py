from tkinter import Label, Button, Tk, Canvas, BOTH, TRUE
from PIL import ImageTk, Image


class SettingPart:
    def __init__(self, can, ro):
        self.canvas = can  # canvas
        self.root = ro  # root

        self.show_name = None  # 이름 000님의 설정
        # label 부분
        self.label_aram = None
        self.label_medicine = None
        self.label_result = None
        self.label_api = None
        # 이미지
        self.setting_icon = None  # 톱니바퀴 이미지
        self.background_image = None  # 흰색 배경
        # 스위치 부분
        self.switch_api = None
        self.switch_medicine = None
        self.switch_aram = None
        self.switch_result = None

        self.create_windows()  # UI 실행

    def create_windows(self):
        self.load_image()
        self.create_labels()
        self.create_buttons()
        self.place()

    def load_image(self):  # 이미지 로드
        image_path = {
            "setting_icon": "/Users/byungchan/Desktop/mirror_software/img/setting.png",  # 설정 아이콘 (톱니바퀴)
            "background": "/Users/byungchan/Desktop/mirror_software/img/Rectangle_setting.png",  # 뒤 배경 (흰색)
            "on": "/Users/byungchan/Desktop/mirror_software/img/switch_on.png",  # 스위치 on
            "off": "/Users/byungchan/Desktop/mirror_software/img/switch_off.png"  # 스위치 off
        }

        self.root.setting_icon = ImageTk.PhotoImage(Image.open(image_path["setting_icon"]).resize((50, 50)))
        self.root.background = ImageTk.PhotoImage(Image.open(image_path["background"]))
        self.root.switch_on = ImageTk.PhotoImage(Image.open(image_path["on"]))
        self.root.switch_off = ImageTk.PhotoImage(Image.open(image_path["off"]))

    def create_labels(self):  # label 만드는 함수
        font_name, bold = "NanumGothic", "bold"
        self.show_name = Label(self.root, font=(font_name, 25, bold), text='양유빈님의 설정       >', fg="white", bg="#1b1b1b")
        self.setting_icon = Label(self.root, image=self.root.setting_icon, bg="#1b1b1b", borderwidth=0,
                                  highlightthickness=0)
        self.background_image = Label(self.root, image=self.root.background, bg="#1b1b1b", borderwidth=0,
                                      highlightthickness=0)
        self.label_aram = Label(self.root, font=(font_name, 19), text='전체 알람', fg="black", bg="white")
        self.label_medicine = Label(self.root, font=(font_name, 19), text='약 복용 알람', fg="black", bg="white")
        self.label_result = Label(self.root, font=(font_name, 19), text='자세 분석 결과 제공', fg="black", bg="white")
        self.label_api = Label(self.root, font=(font_name, 19), text='심평원 API 동의', fg="black", bg="white")

    def create_buttons(self):  # button 만드는 함수
        self.switch_api = Button(self.root, image=self.root.switch_on, bg="white", borderwidth=0, highlightthickness=0)
        self.switch_medicine = Button(self.root, image=self.root.switch_off, bg="white", borderwidth=0,
                                      highlightthickness=0)
        self.switch_aram = Button(self.root, image=self.root.switch_on, bg="white", borderwidth=0, highlightthickness=0)
        self.switch_result = Button(self.root, image=self.root.switch_on, bg="white", borderwidth=0,
                                    highlightthickness=0)

    def place(self):
        self.canvas.create_window(218, 620, window=self.show_name)  # 사용자 이름
        self.canvas.create_window(325, 620, window=self.setting_icon)  # 설정 아이콘
        # (label)
        self.canvas.create_window(534, 660, window=self.label_aram)  # 전체 알림
        self.canvas.create_window(550, 740, window=self.label_medicine)  # 약 복용 알림
        self.canvas.create_window(590, 820, window=self.label_result)  # 자세 분석 결과 제공
        self.canvas.create_window(570, 900, window=self.label_api)  # API
        # (switch)
        self.canvas.create_window(870, 660, window=self.switch_aram)  # 전체 알림
        self.canvas.create_window(870, 740, window=self.switch_medicine)  # 약 복용 알림
        self.canvas.create_window(870, 820, window=self.switch_result)  # 자세 분석 결과
        self.canvas.create_window(870, 900, window=self.switch_api)  # API

        self.canvas.create_window(700, 815, window=self.background_image)  # 흰색 배경


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, bg="#1b1b1b")
    canvas.pack(fill=BOTH, expand=TRUE)
    SettingPart(canvas, root)
    root.geometry("1080x1920")
    root.mainloop()
