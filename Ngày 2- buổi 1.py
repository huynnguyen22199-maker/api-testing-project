try:
    print(10 / 0)
except Exception as e:
    print("lỗi:", e)

import requests
try:
    response = requests.get("https://url-khong-ton-tai-abc123.com")
    print(response.status_code)
except Exception as e:
    print("Gọi API bị lỗi:", e)

import json

data = '{"tên": "Son", "tuoi": 25}'
ket_qua = json.loads(data)
print(ket_qua["tên"])

import json

data = '{"ten": "Son", "tuoi": 25 }'
ket_qua = json.loads(data)
print(ket_qua["tuoi"])

file = open("test.txt", "w") # open file    w:xoa het dât trong file r viết
file.write("xin chao!")
file.close()

file = open ("test.txt", "r") #"r" mở file rồi đọc 
noi_dung = file.read() # đọc toàn bộ nội dung
file.close()           # đóng file đọc
print(noi_dung)

with open("test.txt", "r") as file: #mở file và đặt tên là file
    noi_dung = file.read()  # khỉ ra khỏi khối with -> tự động đóng file
    print(noi_dung)

with open("test.txt", "w") as file:
    file.write("dòng 1\n")  #\n : xuống dòng mới
    file.write("dòng 2\n")
    file.write("dòng 3\n")