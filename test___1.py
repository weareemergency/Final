import cv2
import mediapipe as mp
import threading
import os
import PIL.Image, PIL.ImageTk
import playsound
import main, Health # class 가져 오기
import torch 

from tkinter import *
from PIL import ImageTk, Image


class Voice:
    def __init__(self): 
        self.start_voice = './mpfile/checking.mp3'
        self.end_voice = './mpfile/finish_checking.mp3'
        self.fail_voice = './mpfile/fail.mp3'

    def start(self): # 측정 시작 사운드 출력
        playsound.playsound(self.start_voice)

    def end(self): # 측정 종료 사운드 출력 
        playsound.playsound(self.end_voice)

    def fail(self): # 측정 실패 사운드 출력 
        playsound.playsound(self.fail_voice)


class InitialSettings:
    def __init__(self, cap):
        self.cap = cap # frame
        self.cap_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.cap_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        folder_path = 'Result/' # 측정 사진 저장 폴더 경로
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"폴더를 만들었습니다.: {folder_path}")
        else:
            print(f"폴더 존재 : {folder_path}")

    def frame_info(self): # 카메라 가로 세로 사이즈 확인할 때 사용하는 코드
        text = f"가로 사이즈 : {self.cap_width}, 세로 사이즈 : {self.cap_height}"
        print(text)



class Check: # 값 누락 확인 클래스 
    def __init__(self, x, y, label, confidence):
        self.part_x = x 
        self.part_y = y 
        self.label = label
        self.confidence = confidence

    def check_index(self): # 기존 코드의 문제점을 보완 ==> index error (어떤 부분이 누락되었는지 확인 불가능 했었음)
        if self.label or self.confidence:
            print(f"{self.label} 값 2개 확인 ==> {self.part_x, self.part_y}")
            return True    
        else:
            print(f"{self.label} 값 누락")
            return False
        

class Draw: 
    def __init__(self, ear, number7): # 귀 좌표, 경추 7번 좌표 순서로 구성 
        self.image = 'Result/UserPicture.jpeg'
        self.save_path = 'Result/result_image.jpg'
        self.ear_x, self.ear_y = ear 
        self.number7_x , self.number7_y = number7
        self.red_color = (0, 0, 255)

    def save_draw_image(self): # -- 귀와 목에 직선을 그린 사진 저장 하는 함수 --
        save_path = 'result_image.jpg'
        cv2.imwrite(save_path, image)
 
    def draw_point_line(self): # -- 각각의 부분에 대한 마커와 직선을 그음 --
        image = cv2.imread(self.image)  

        cv2.circle(image, (self.ear_x, self.ear_y), 5, self.red_color, -1)  # 귀 부분에 마킹 
        cv2.circle(image, (self.number7_x, self.number7_y), 5, self.red_color, -1)  # 경추7번 부분에 마킹 
        cv2.line(image, (self.ear_x, self.ear_y), (self.number7_x, self.number7_y), self.red_color, 2) # 귀에서 경추7번 까지 직선 
        cv2.line(image, (self.ear_x, self.number7_y), (self.number7_x, self.number7_y), self.red_color, 2) # 경추7번에서 수평으로 직선 

        cv2.imwrite(self.save_path, image) # 검사 결과지 저장 

class Detect: # 측정 클래스 
    def __init__(self):
        self.weight_file_path = 'weights/Version_1.pt'
        self.image_file_path = 'Result/UserPicture.jpeg'
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', self.weight_file_path, force_reload=True)
        self.ear_coordinates = []  # 귀 좌표를 저장할 리스트
        self.number7_coordinates = []  # number7 좌표를 저장할 리스트

    def process_label(self, row): # -- 초반 필요한 변수 모음 함수 --
        label = row['name'] # 라벨명 
        confidence = row['confidence'] # 정확도 
        bbox = row[['xmin', 'ymin', 'xmax', 'ymax']].values # 박스 모서리 좌표 
        x_min, y_min, x_max, y_max = bbox.astype(int) # 박스 모서리 좌표를 (x_min, x_max, ...) 형태로 반환 
        return (x_min + x_max) // 2, (y_min + y_max) // 2, label, confidence

    def get_coordinates(self): # -- 측정 함수 -- 
        image = cv2.imread(self.image_file_path)
        result = self.model(image)
        predictions = result.pandas().xyxy[0]

        for _, row in predictions.iterrows():
            part_x, part_y, label, confidence = self.process_label(row)
            if confidence > 0.51111: # 정확도가 0.5111 초과인 것만 탐지
                check = Check(part_x, part_y, label, confidence)
                if check.check_index(): # 값 누락 확인 함수 
                    if label == 'ear': # 귀에 대한 좌푯값 
                        self.ear_coordinates.append((part_x, part_y)) # 이 부분에서 좌표값 더함(append)
                    if label == 'number7': # 경추 7번에 대한 좌푯값 
                        self.number7_coordinates.append((part_x, part_y)) # 위와 동일 
                else:
                    print("값이 누락되어 다시 측정 바랍니다.")
                    return 0

    def combine_coordinates(self): # -- 귀 xy좌표와 경추7번 xy좌표 합치는 함수 --
        combined_coordinates = list(self.ear_coordinates) + list(self.number7_coordinates) # [(000, 000), (000, 000)] 형태로 저장
        partdraw = Draw(combined_coordinates[0], combined_coordinates[1]) # 귀 좌표, 경추 7번 좌표 순서로 구성 
        partdraw.draw_point_line() 


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    # camera_info = InitialSettings(cap) 기초 설정 
    
    image = 'Result/UserPicture.jpeg' # 이미지 파일 

    if os.path.isfile(image): # 여긴 테스트 버전이므로 사진 넣어서 바로 실행 
        print("바로 측정")
        model = Detect()
        model.get_coordinates()
        model.combine_coordinates()
    

    else:
        print("사진 측정 시작")


    