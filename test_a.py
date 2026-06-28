import requests
import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "220199",
    database = "testdb"
)

#Kiểm tra database
def test_verify_db():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = 1")
    db_data = cursor.fetchone()
    
    assert db_data[0] == 1
    assert db_data[1] == "Huyen"
    assert db_data[2] == "huyen@gmail.com"
    assert db_data[3] == 22
    print("PASS - DB data đúng hết!")

# test kết hợp API thật + DB vào file
def test_tao_user_va_verify_db():
    # Bước 1: Gọi API tạo user mới
    new_user = {"name": "Huyen", "email": "huyen@gmail.com"}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=new_user
    )
    # Bước 2: Verify API
    assert response.status_code == 201
    assert response.json()["name"]=="Huyen"
    print("Pass - APO tạo user thành công!")
    # Bước 3: Verify DB
    cursor = conn.cursor()
    cursor.execute("select * from users where name ='Huyen'")
    db_data = cursor.fetchone()
    assert db_data[1] == "Huyen"
    print("Pass - DB có user Huyen!")