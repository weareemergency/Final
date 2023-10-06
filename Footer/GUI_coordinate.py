"""
GUI에서 사용되는 각 버튼별 좌표 저장 파일
"""


def setting():  # 설정 관련 함수  ---------------------------------
    setting_coordinate = {
        "background": [700, 815],  # 뒤 흰색 배경 좌표
        "icon": [325, 620],  # 설정 아이콘 좌표
        # --- 텍스트 부분 좌표
        "show_name": [680, 980],  # 이름
        "text_aram": [570, 900],  # 전체 알림
        "text_medicine": [550, 740],  # 약 복용 알림
        "text_result": [590, 820],  # 자세 분석 결과 제공
        "text_api": [570, 900],  # 심평원 API 동의
        # --- 스위치 부분 좌표
        "switch_aram": [870, 660],  # 전체 알림
        "switch_medicine": [870, 740],  # 약 복용 알림
        "switch_result": [870, 820],  # 자세 분석 결과 제공
        "switch_api": [870, 660]  # 심평원 API 동의
    }
    return setting_coordinate
