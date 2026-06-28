import requests
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "220199",
    database = "testdb"
)

def test_lay_user_va_verify_db():
    # Bước 1: Gọi API
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    api_data = response.json()
    
    # Bước 2: Kiểm tra API
    assert response.status_code == 200
    
    # Bước 3: Kiểm tra DB
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = 1")
    db_data = cursor.fetchone()
    
    # Bước 4: So sánh
    assert db_data[0] == 1
    print("PASS - User tồn tại trong DB!")
# trường hợp API data và db data không trùng nhau
def test_lay_user_va_verify_db():
    # Kiểm tra API
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Leanne Graham"
    print("PASS - API đúng!")
    
    # Kiểm tra DB riêng
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = 1")
    db_data = cursor.fetchone()
    assert db_data[1] == "Huyen"
    print("PASS - DB đúng!")
# Trường hợp API data và db data trùng nhau

def test_lay_user_va_verify_db():
    # Bước 1: Gọi API
    response = requests.get("http://api-cong-ty.com/users/1")
    api_data = response.json()
    
    # Bước 2: Kiểm tra API
    assert response.status_code == 200
    
    # Bước 3: Lấy data từ DB
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = 1")
    db_data = cursor.fetchone()
    
    # Bước 4: So sánh API và DB phải khớp nhau
    assert api_data["id"] == db_data[0]
    assert api_data["name"] == db_data[1]
    assert api_data["email"] == db_data[2]
    print("PASS - API và DB khớp nhau!")

#Kiểm tra database
def test_verify_db():
    cursor = conn.cursor()
    cursor.execute("select * from users where id = 1")
    db_data = cursor.fetchone()
    assert db_data[0] == 1
    assert db_data[1] == "Huyen"
    assert db_data[2] == "huyen@gmail.com"
    assert db_data[3] == 22
    print("pass - DB data đúng hết!")
    

