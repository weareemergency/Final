import nanocamera as nano

# 카메라 초기화
camera = nano.Camera(camera_type=1, device_id=1, width=640, height=480, fps=30)

# 카메라에서 프레임 캡처
frame = camera.read()

# 캡처된 프레임 출력
cv2.imshow('frame', frame)

# 키가 눌릴 때까지 대기
cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()

# 카메라 해제
camera.release()
