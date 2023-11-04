from tkinter import Label, Button, Tk, Canvas, BOTH, TRUE
from PIL import ImageTk, Image


def setting():  # 설정 관련 함수  ---------------------------------
    setting_coordinate = {
        # --- 좌표 테스트 =============== 1920 x 1080 에서 의 좌표
        "show_name": [280, 200],  # 이름
        "aram_label": [556, 250],  # 전체 알림
        "medicine_label": [570, 320],  # 약 복용 알림
        "result_label": [600, 390],  # 자세 분석 결과 제공
        "api_label": [536, 460],  # 심평원 API 동의
        "setting_icon": [410, 200],  # 설정 아이콘 좌표
        "background": [700, 400],  # 뒤 흰색 배경 좌표
        "medicine_switch": [860, 320],  # 스위치
        "aram_switch": [860, 250],  # 스위치
        "result_switch": [860, 390],  # 스위치
        "api_switch": [860, 460]  # 스위치

        # --- 좌표 지정 =================== 1080 x 1920
        # "show_name": [218, 620],  # 이름
        # "aram_label": [530, 660],  # 전체 알림
        # "medicine_label": [550, 740],  # 약 복용 알림
        # "result_label": [590, 820],  # 자세 분석 결과 제공
        # "api_label": [570, 900],  # 심평원 API 동의
        # "setting_icon": [360, 620],  # 설정 아이콘 좌표
        # "background": [700, 815],  # 뒤 흰색 배경 좌표
        # "medicine_switch": [870, 740],  # 약 복용 알람 스위치
        # "aram_switch": [870, 660],  # 알람 스위치
        # "result_switch": [870, 820],  # 자세 분석 결과 스위치
        # "api_switch": [870, 900]  # 심평원 api 동의 스위치
    }
    return setting_coordinate


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
        "setting_icon": "/Users/byungchan/Desktop/final/img/setting.png",  # 설정 아이콘 (톱니바퀴)
        "background": "/Users/byungchan/Desktop/final/img/Rectangle_setting.png",  # 뒤 배경 (흰색)
        "on": "/Users/byungchan/Desktop/final/img/switch_on.png",  # 스위치 on
        "off": "/Users/byungchan/Desktop/final/img/switch_off.png"  # 스위치 off
    }

    return images


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


if __name__ == "__main__":
    print("main 부분 실행")
    root = Tk()  # Tk 생성
    canvas = Canvas(root, bg="#1b1b1b")
    canvas.pack(fill=BOTH, expand=TRUE)
    SettingPart(canvas, root).create_window()
    root.geometry("1920x1080")
    root.mainloop()