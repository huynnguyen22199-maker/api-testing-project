import mysql.connector    # nạp thư viện kết nối MySQL
conn = mysql.connector.connect(   # kết nối tới MySQL
    host = "localhost",            #MySQL đang chạy trên máy tính
    user="root",                    # Tên đăng nhập, "root" là tên tk mặc định của MySQL
    password="220199",
    database="testdb"
)
print("Kết nối thành công!")


cursor = conn.cursor()
cursor.execute("select * from users")
ket_qua = cursor.fetchall()
for row in ket_qua:
    print(row)

#cursor : công cụ để chạy câu SQL
#cursor.execute(): chạy câu SQL
#cursor.fetchall(): lấy tất cả kết quả về
#for row in ket_qua: in từng dòng
#fetchall: lấy tất cả

cursor.execute("select * from users where id =1")
mot_dong = cursor.fetchone()
print(mot_dong)
# fetchone: chỉ lấy 1 dòng đầu tiên thôi

import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
api_data = {"name" : "Huyen"}
cursor.execute("SELECT * FROM users WHERE id = 1")
db_data = cursor.fetchone()
assert response.status_code ==200
assert api_data["name"]== db_data[1]
print("pass")