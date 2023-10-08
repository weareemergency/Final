from tkinter import Tk, Canvas, BOTH, TRUE, Label
from PIL import ImageTk, Image

from coordinate import setting
from basic_setting import SettingLabel, setting_image_path
from basic_setting import TodoLabel,todo_image_path


# DB 클래스 추가 필요!!!!!!

# class Basic:
#     def __init__(self, canvas, root):
#         self.canvas = canvas
#         self.root = root


# =================================================== setting
class SettingPart:
    def __init__(self, can, ro):
        self.canvas = can
        self.root = ro
        self.label = SettingLabel
        self.image_path = setting_image_path()  # 이미지 불러옴
        self.setting_image()  # 아래 setting_image 함수 실행)
        self.font_name = "NaumGothic"

    def setting_image(self):  # setting 이미지 불러옴 파일
        self.root.setting_icon = ImageTk.PhotoImage(Image.open(self.image_path["setting_icon"]).resize((50, 50)))  # 톱니 바퀴 사진
        self.root.white_background = ImageTk.PhotoImage(Image.open(self.image_path["background"]))  # 뒤 흰색 배경
        self.root.on = ImageTk.PhotoImage(Image.open(self.image_path["on"]))  # 스위치 on
        self.root.off = ImageTk.PhotoImage(Image.open(self.image_path["off"]))  # 스위치 off

    def setting_label_text(self):  # label 텍스트
        show_name = self.label(self.root, "양유빈님의 설정", 25, self.font_name).label_text(True)  # 굵은 글씨 True || O0O님의 설정
        aram_label = self.label(self.root, "전체알림", 19, self.font_name).label_text(False)  # UI -> 전체 알림
        medicine_label = self.label(self.root, "약 복용 알림", 19, self.font_name).label_text(False)  # UI -> 약 복용 알림
        result_label = self.label(self.root, "자세 분석 결과 제공", 19, self.font_name).label_text(False)  # UI -> 자체 분석 결과 제공
        api_label = self.label(self.root, "심평원 API 동의", 19, self.font_name).label_text(False)  # UI -> API

        label_list = [show_name, aram_label, medicine_label, result_label, api_label]  # 전부 리스트로 묶어서 리턴
        return label_list

    def setting_label_image(self):  # label image
        setting_icon = self.label(self.root, None, None, None).image_label(self.root.setting_icon)  # UI -> 톱니바퀴 이미지
        background = self.label(self.root, None, None, None).image_label(self.root.white_background)  # UI -> 흰색 배경

        label_list = [setting_icon, background]  # 전부 리스트로 묶어서 리턴
        return label_list

    def setting_switch(self):  # 스위치 on, off 부분
        aram = self.label(self.root, None, None, None).button(self.root.off)  # UI -> 스위치 on
        medicine = self.label(self.root, None, None, None).button(self.root.on)  # UI -> 스위치 on
        result = self.label(self.root, None, None, None).button(self.root.on)  # UI -> 스위치 on
        api = self.label(self.root, None, None, None).button(self.root.off)  # UI -> 스위치 on

        switch_list = [aram, medicine, result, api]
        return switch_list

    def create_window(self):  # window 생성 함수
        label_text = self.setting_label_text()
        label_image = self.setting_label_image()
        button = self.setting_switch()
        label = label_text + label_image + button
        setting_coordinates = setting()

        count = 0
        for coordinate in setting_coordinates.values():
            if 0 < count < 5:
                label[count].lift()
            self.canvas.create_window(coordinate[0], coordinate[1], window=label[count])  # 사용자 이름
            count += 1


# =================================================== todo
class TodoPart:
    def __init__(self, can, ro):
        self.canvas = can
        self.root = ro
        self.image_path = todo_image_path()
        self.todo_image()

    def todo_image(self):
        self.root.complete = ImageTk.PhotoImage(Image.open(self.image_path["complete"]).resize((49, 49)))
        self.root.not_complete = ImageTk.PhotoImage(Image.open(self.image_path["not_complete"]).resize((49, 49)))
        self.root.todo_background = ImageTk.PhotoImage(Image.open(self.image_path["todo_background"]).resize((915, 538)))

    def todo_static_text(self):  # 상단 내용 (DB X)
        static_text = TodoLabel(self.root, None, None).static_label_text()
        return static_text

    def todo_database_text(self):


    def create_window(self):
        pass


if __name__ == "__main__":
    print("main 부분 실행")
    root = Tk()  # Tk 생성
    canvas = Canvas(root, bg="#1b1b1b")
    canvas.pack(fill=BOTH, expand=TRUE)
    TodoPart(canvas, root).todo_static_text()
    root.geometry("1080x1920")
    root.mainloop()
