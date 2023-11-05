import picamera
import time
import cv2

# 카메라 초기화
camera = picamera.PiCamera()

# 카메라 설정
camera.resolution = (640, 480)
camera.framerate = 30

# 카메라에서 프레임 캡처
camera.capture('/tmp/foo.jpg')

# 캡처된 프레임 읽기
frame = cv2.imread('/tmp/foo.jpg')

# 캡처된 프레임 출력
cv2.imshow('frame', frame)

# 키가 눌릴 때까지 대기
cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()
