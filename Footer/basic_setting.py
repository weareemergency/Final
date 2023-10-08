"""
글꼴, 이미지 파일 설정 파일
"""
from tkinter import Label, Button


def setting_image_path():  # setting_image 파일 경로
    # 위도우 파일 ========>
    # images = {
    #     "setting_icon": r"C:/Users/user/Desktop/python/gui_make/img/setting.png",  # 설정 아이콘 (톱니바퀴)
    #     "background": r"C:/Users/user/Desktop/python/gui_make/img/Rectangle_setting.png",  # 뒤 배경 (흰색)
    #     "on": r"C:/Users/user/Desktop/python/gui_make/img/switch_on.png",  # 스위치 on
    #     "off": r"C:/Users/user/Desktop/python/gui_make/img/switch_off.png"  # 스위치 off
    # }

    # 맥, 리눅스 작업 파일 ========>
    images = {
        "setting_icon": "../img/setting.png",  # 설정 아이콘 (톱니바퀴)
        "background": "../img/Rectangle_setting.png",  # 뒤 배경 (흰색)
        "on": "../img/switch_on.png",  # 스위치 on
        "off": "../img/switch_off.png"  # 스위치 off
    }

    return images


def todo_image_path():
    # 윈도우 파일 ========>
    # images = {
    #     "complete": r"C:/Users/user/Desktop/python/gui_make/img/check.png",
    #     "not_complete": r"C:/Users/user/Desktop/python/gui_make/img/ai_rect.png",
    #     "todo_background": r"C:/Users/user/Desktop/python/gui_make/img/Rect16.png",
    # }

    # 맥, 리눅스 작업 파일 =====>
    images = {
        "complete": "../img/check.png",
        "not_complete": "../img/ai_rect.png",
        "todo_background": "../img/Rect16.png",
    }
    return images

# ===============================================================================================

class SettingLabel:  # 설정 UI 부분
    def __init__(self, root, text, text_size, font_name):
        self.root = root
        self.text = text
        self.text_size = text_size  # 텍스트 사이즈 설정 (25, 19)
        self.font_name = font_name  # 폰트 설정

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

    def button(self, image):
        image = image
        return Button(self.root, image=image, bg="white", borderwidth=0, highlightthickness=0)


class TodoLabel(SettingLabel):
    def __init__(self, root, text, text_size):
        super().__init__(root, text, text_size, None)
        self.english_font = "Noto Sans"
        self.static_text_list = ["양유빈님의 성공 현황", "TodoList", "Due Date", "Complete"]

    def static_label_text(self):
        labels = []

        count = 0
        for text in self.static_text_list:
            if count:
                label = Label(self.root, font=(self.english_font, 16, "bold"), text=text, fg="black", bg="white")
            else:
                label = Label(self.root, font=('Noto Sans', 16, 'bold'), text=text, fg="black", bg="white")
            labels.append(label)
            count += 1

        # show_name = Label(self.root, font=(self.english_font, 16, "bold"), text=self.static_text_list[0], fg="black", bg="white")
        # todo = Label(self.root, font=('Noto Sans', 16, 'bold'), text=self.static_text_list[1], fg="black", bg="white")
        # due = Label(self.root, font=('Noto Sans', 16, 'bold'), text=self.static_text_list[2], bg="white")
        # complete = Label(self.root, font=('Noto Sans', 16, 'bold'), text=self.static_text_list[3], fg="black", bg="white")
        # labels = [show_name, todo, due, complete]

        return labels
