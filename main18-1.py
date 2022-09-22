from ppadb.client import Client  # adb 사용을 위해 라이브러리 가져오기

client = Client(host="127.0.0.1", port=5037) # 127.0.0.1 IP의 5037 포트로 접속합니다. ADB 사용을 위한 고정 IP와 포트주소입니다.
find_devices = client.devices()

if len(find_devices) == 0:  # 디바이스를 찾지 못했다면 코드 종료합니다.
    print('No devices')
    quit()

device = find_devices[0]
print(f'찾은 디바이스: {device}')  # 찾은 디바이스를 출력합니다.