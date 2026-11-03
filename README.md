# embeddingsysyem

# Raspberry Pi Dual Servo Control

Python의 gpiozero 및 lgpio 라이브러리를 이용한 Raspberry Pi 3B 기반 다중 서보모터 제어 프로젝트입니다.

## 개발 환경
- Raspberry Pi 3 Model B
- Raspberry Pi OS Trixie
- Python 3
- gpiozero 2.0.1
- lgpio 0.2.2

## GPIO 연결
- Servo Motor 1: GPIO17
- Servo Motor 2: GPIO18
- 서보모터 구동 전원: 별도 외부 전원
- Raspberry Pi와 외부 전원은 공통 GND 연결

## 라이브러리 설치

```bash
sudo apt update
sudo apt install python3-gpiozero python3-lgpio -y
```

## 실행 방법

```bash
python3 dual_servo_control.py
```

입력 예시:

```text
Servo1 Servo2 > 6.0 9.0
Servo1 Servo2 > 9.0 6.0
Servo1 Servo2 > 7.5 7.5
```

## 프로젝트 목표

두 개의 서보모터에 서로 다른 PWM 제어값을 전달하여 독립적인 위치 제어를 구현하는 것이 목표입니다.

현재 라이브러리 설치 및 코드 작성은 완료했으며, 실제 하드웨어 제어 결과는 추가 검증이 필요합니다.

## 주의사항

서보모터에는 적절한 외부 전원이 필요합니다. Raspberry Pi와 서보모터 전원은 공통 GND를 사용해야 합니다. 전원 모듈 과열 또는 배선 이상이 발생하면 즉시 전원을 차단해야 합니다.
