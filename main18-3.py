from ppadb.client import Client
import time

def adb_connect():
    client = Client(host="127.0.0.1", port=5037) 
    find_devices = client.devices()

    if len(find_devices) == 0:
        print('No devices')
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스: {device}')

    return device, client

device, client = adb_connect()

device.shell('input keyevent 64')  # 웹 브라우저를 실행합니다.
time.sleep(2.0)

xyPosition = "423 136" 
device.shell(f'input tap {xyPosition}')  # 주소창으로 이동하여 터치합니다.
time.sleep(2.0)

url = "www.naver.com"   # URL을 입력합니다.
device.shell(f'input text {url}')
time.sleep(2.0)

device.shell('input keyevent 66')  # 엔터를 누릅니다.
time.sleep(2.0)

result = device.screencap()  # 스크린 캡쳐한 화면을 result 변수에 넣어줍니다.
with open(r"18. 스마트폰자동화\screen.png", "wb") as fp:  # 스마트 폰 자동화 폴더에 screen.png의 이름으로 캡쳐한 사진을 저장합니다. with문을 사용하면 close를 하지 않아도 with블록이 끝나면 자동으로 close해준다.
    fp.write(result)