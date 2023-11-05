import cv2

# 카메라 초기화
cap = cv2.VideoCapture(0)

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