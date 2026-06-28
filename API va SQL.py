import requests
import mysql.connector    # nạp thư viện kết nối MySQL
conn = mysql.connector.connect(   # kết nối tới MySQL
    host = "localhost",            #MySQL đang chạy trên máy tính
    user="root",                    # Tên đăng nhập, "root" là tên tk mặc định của MySQL
    password="220199",
    database="testdb"
)
print("Kết nối thành công!")


cursor = conn.cursor()
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
api_data = response.json()
cursor.execute("SELECT * FROM users WHERE id = 1")
db_data = cursor.fetchone()
assert response.status_code ==200
assert api_data["name"]== db_data[1]
print("pass")