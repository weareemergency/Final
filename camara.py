import cv2

# GStreamer 파이프라인 설정
pipeline = 'nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM), width=1280, height=720, framerate=60/1 ! nvvidconv flip-method=0 ! video/x-raw, width=1280, height=720 ! videoconvert ! appsink'

# 카메라 초기화
cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

# 카메라에서 프레임 캡처
ret, frame = cap.read()

# 캡처된 프레임 출력
cv2.imshow('frame', frame)

# 키가 눌릴 때까지 대기
cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()

# 카메라 해제
cap.release()
