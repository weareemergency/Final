from tkinter import *
from PIL import ImageTk, Image
from ranking import RankList
from database import TodoDataBase


class LabelSetting:
    def __init__(self, root, font, size, text):
        self.root = root
        self.font = font
        self.size = size
        self.text = text

    def head_font(self):  # bold 폰트
        fg, bg = "white", "#1b1b1b"
        return Label(self.root, font=(self.font, self.size, 'bold'), text=self.text, fg=fg, bg=bg)

    def normal_font(self):
        fg, bg = "black", "white"
        return Label(self.root, font=(self.font, self.size), text=self.text, fg=fg, bg=bg)

    def image_label(self, image):
        image = image
        return Label(self.root, image=image, bg="#1b1b1b", borderwidth=0, highlightthickness=0)


class Init:  # 필요한 기본 값 (상속 할거임)
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root


class BottomSetting(Init):  # GUI 하단 설정 클래스
    def __init__(self, canvas, root):
        super().__init__(canvas, root)
        self.image_files = {
            "background": "img/Rectangle_setting.png",
            "on": "img/switch_on.png",
            "off": "img/switch_off.png"
        }
        self.font_name = "NanumGothic"
        self.setting()

    def setting(self):
        self.root.setting_icon = ImageTk.PhotoImage(Image.open("img/setting.png").resize((50, 50)))  # resize 필요하여 반복문에서 제외
        for name, path in self.image_files.items():
            image = Image.open(f"{str(path)}")
            setattr(self, name, ImageTk.PhotoImage(image))
            setattr(self.root, name, getattr(self, name))

        show_name = LabelSetting(self.root, self.font_name, 25, "양유빈님의 설정          >").head_font()
        aram_label = LabelSetting(self.root, self.font_name, 19, "전체알림").normal_font()
        medicine_label = LabelSetting(self.root, self.font_name, 19, "약 복용 알림").normal_font()
        result_label = LabelSetting(self.root, self.font_name, 19, "자세 분셕 결과 제공").normal_font()
        api_label = LabelSetting(self.root, self.font_name, 19, "API").normal_font()

        setting_icon = LabelSetting(self.root, None, None, None).image_label(self.root.setting_icon)
        setting_background = LabelSetting(self.root, None, None, None).image_label(self.root.background)










