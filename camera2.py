import cv2
import imutils

# VideoCapture 객체를 생성하여 라즈베리 파이 카메라를 연결합니다.
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 나타냅니다.

# 영상의 너비와 높이를 설정합니다.
cap.set(3, 640)  # 너비
cap.set(4, 480)  # 높이

while True:
    # 비디오 프레임을 읽어옵니다.
    ret, frame = cap.read()
    
    if not ret:
        break

    # 프레임을 화면에 표시합니다.
    cv2.imshow("Raspberry Pi Camera", frame)

    # 'q' 키를 누르면 루프를 종료합니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 사용이 끝났으면 카메라와 창을 해제합니다.
cap.release()
cv2.destroyAllWindows()
'''
pip install opencv-python-headless
pip install imutils
sudo apt-get update
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install -y python3-dev python3-numpy python3-pip
sudo apt-get install -y libxvidcore-dev libx264-dev libgtk-3-dev
sudo apt-get install -y libtbb2 libtbb-dev libdc1394-22-dev
sudo apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev


'''