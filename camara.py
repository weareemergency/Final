import cv2
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst

# GStreamer 파이프라인 설정
pipeline = 'nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM), width=1920, height=1080, framerate=30/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=540 ! videoconvert ! appsink'

# GStreamer 파이프라인 생성
pipeline = Gst.parse_launch(pipeline)

# GStreamer 파이프라인 시작
pipeline.set_state(Gst.State.PLAYING)

# 카메라에서 프레임 캡처
while True:
    sample = pipeline.emit('pull-sample')
    if sample:
        buf = sample.get_buffer()
        caps = sample.get_caps()
        width = caps.get_structure(0).get_value('width')
        height = caps.get_structure(0).get_value('height')
        frame = buf.extract_dup(0, buf.get_size())
        frame = np.frombuffer(frame, dtype=np.uint8).reshape((height, width, 3))
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# GStreamer 파이프라인 정지
pipeline.set_state(Gst.State.NULL)
