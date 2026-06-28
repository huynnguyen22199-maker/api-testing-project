tuoi = 18
if tuoi >= 18:
    print("Đủ tuổi")
else:
    print("Chưa đủ tuổi")

diem = 50
if diem >=90:
    print("Xuất sắc")
elif diem >= 70:
    print("Khá")
else:
    print("Trung bình")

for i in range(5):
    print(i)

status_codes = [200, 404, 500]
for code in status_codes:
    if code == 200:
        print("Pass")
    else:
        print("Fall")

dem = 0
while dem < 3:
    print(dem)
    dem = dem +1
    