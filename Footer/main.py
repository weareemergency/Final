from tkinter import *
from PIL import ImageTk, Image

from coordinate import setting
from basic_setting import SettingLabel  # 클래스
from basic_setting import setting_image_path  # 함수


# DB 클래스 추가 필요!!!!!!

# class Basic:
#     def __init__(self, canvas, root):
#         self.canvas = canvas
#         self.root = root


class SettingPart:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.label = SettingLabel
        self.image_path = setting_image_path()  # 이미지 불러옴
        self.setting_image()  # 아래 setting_image 함수 실행)

    def setting_image(self):  # setting 이미지 불러옴 파일
        # print("값 확인", self.image_path["setting_icon"])
        self.root.setting_icon = ImageTk.PhotoImage(Image.open(self.image_path["setting_icon"]).resize((50, 50)))  # 톱니 바퀴 사진
        self.root.white_background = ImageTk.PhotoImage(Image.open(self.image_path["background"]))  # 뒤 흰색 배경
        self.root.on = ImageTk.PhotoImage(Image.open(self.image_path["off"]))  # 스위치 on
        self.root.off = ImageTk.PhotoImage(Image.open(self.image_path["on"]))  # 스위치 off

    def setting_label_text(self):  # label 텍스트
        show_name = self.label(self.root, "양유빈님의 설정", 25).label_text(True)  # 굵은 글씨 True || O0O님의 설정
        aram_label = self.label(self.root, "전체알림", 19).label_text(False)  # UI -> 전체 알림
        medicine_label = self.label(self.root, "약 복용 알림", 19).label_text(False)  # UI -> 약 복용 알림
        result_label = self.label(self.root, "자세 분셕 결과 제공", 19).label_text(False)  # UI -> 자체 분석 결과 제공
        api_label = self.label(self.root, "API", 19).label_text(False)  # UI -> API

        label_list = [show_name, aram_label, medicine_label, result_label, api_label]  # 전부 리스트로 묶어서 리턴
        return label_list

    def setting_label_image(self):  # label image
        setting_icon = self.label(self.root, None, None).image_label(self.root.setting_icon)  # UI -> 톱니바퀴 이미지
        background = self.label(self.root, None, None).image_label(self.root.white_background)  # UI -> 흰색 배경

        label_list = [setting_icon, background]  # 전부 리스트로 묶어서 리턴
        return label_list

    def create_window(self):  # window 생성 함수
        label_text = self.setting_label_text()
        label_image = self.setting_label_image()
        label = label_text + label_image  # label_text 다음 label_image
        setting_coordinates = setting()  # setting 좌표가 들어가 있는 변수

        count = 0
        for coordinate in setting_coordinates.values():
            label[count].lift()
            self.canvas.create_window(coordinate[0], coordinate[1], window=label[count])  # 사용자 이름
            count += 1

        # self.canvas.create_window(200, 200, window=label[1])  # 전체 알림
        # self.canvas.create_window(330, 330, window=label[6])  # 설정 아이콘
        # self.canvas.create_window(218, 620, window=label[0])  # 사용자 이름

        # for key, value in setting_coordinates.items():
        #     label[count].lift()
        #
        #     count += 1








    def start(self):
        pass


if __name__ == "__main__":
    print("main 부분 실행")
    root = Tk()  # Tk 생성
    # root.overrideredirect(True)
    canvas = Canvas(root, bg="#1b1b1b")
    # gui화면 설정 배경 bg="색갈입력" 현재 #1b1b1b 설정됨
    canvas.pack(fill=BOTH, expand=TRUE)
    # footer.footer_menu(canvas, root)
    SettingPart(canvas, root).create_window()
    root.geometry("1000x1920")
    # 화면 크기를 지정한다
    root.mainloop()

