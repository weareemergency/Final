"""
글꼴, 이미지 파일 설정 파일
"""
from tkinter import Label


def setting_image_path():  # setting_image 파일 경로
    images = {
        "setting_icon": "../img/setting.png",  # 설정 아이콘 (톱니바퀴)
        "background": "../img/Rectangle_setting.png",  # 뒤 배경 (흰색)
        "on": "../img/switch_on.png",  # 스위치 on
        "off": "../img/switch_off.png"  # 스위치 off
    }
    return images


class SettingLabel:  # 설정 UI 부분
    def __init__(self, root, text, text_size):
        self.root = root
        self.text = text  # 텍스트 (DB 불러옴)
        self.text_size = text_size  # 텍스트 사이즈 설정 (25, 19)
        self.font_name = "NanumGothic"  # 폰트 설정

    def label_text(self, bold):  # label text 부분
        if bold:  # 굵고, 큰 글씨일 경우
            fg, bg = "white", "#1b1b1b"
            return Label(self.root, font=(self.font_name, self.text_size, 'bold'), text=self.text, fg=fg, bg=bg)
        else:
            fg, bg = "black", "white"
            return Label(self.root, font=(self.font_name, self.text_size), text=self.text, fg=fg, bg=bg)

    def image_label(self, image):  # label image 부분
        image = image
        return Label(self.root, image=image, bg="#1b1b1b", borderwidth=0, highlightthickness=0)

