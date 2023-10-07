"""
GUI에서 사용되는 각 버튼별 좌표 저장 파일
"""


def setting():  # 설정 관련 함수  ---------------------------------
    setting_coordinate = {
        # --- 좌표 테스트 ===============
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


        # 이 아래 좌표 절대 지우지 말것!!!!!!!!!!!!!! (순서 유지 필수)
        # "show_name": [680, 980],  # 이름
        # "aram_label": [570, 900],  # 전체 알림
        # "medicine_label": [550, 740],  # 약 복용 알림
        # "result_label": [590, 820],  # 자세 분석 결과 제공
        # "api_label": [570, 900],  # 심평원 API 동의
        # "setting_icon": [325, 620],  # 설정 아이콘 좌표
        # "background": [700, 815],  # 뒤 흰색 배경 좌표
    }
    return setting_coordinate


if __name__ == "__main__":
    setting_coordinates = setting()

    for key, value in setting_coordinates.items():
        print(f"{key} : {value}")