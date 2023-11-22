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
sudo apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libopencv-core-dev \
    libopencv-highgui-dev \
    libopencv-calib3d-dev \
    libopencv-features2d-dev \
    libopencv-imgproc-dev \
    libopencv-video-dev \
    libopencv-videoio-dev \
    protobuf-compiler \
    python3-pip \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    python3-numpy \
    python3-opencv \
    cmake


'''