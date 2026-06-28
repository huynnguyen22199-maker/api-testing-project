import requests
response = requests.get(
    "https://httpbin.io/basic-auth/user/pass",
    auth = ("user","sai_mat_khau")
)
print(response.status_code)
print(response.json())
#httpbin.org : website dùng để test HTTP request, 
#/basic-auth/user/pass: endpoint yêu cầu username=user, password=pass
#auth=("user","pass"): truyền username và passwork vào

def test_dang_nhan_dung():
    response = requests.get(
        "https://httpbin.io/basic-auth/user/pass",
        auth=("user","pass")
    )
    assert response.status_code == 200
    assert response.json()["authorized"] == True
    print("Pass - Đăng nhập thành công!")
def test_dang_nhap_sai():
    response = requests.get(
        "https://httpbin.io/basic-auth/user/pass",
        auth=("user", "sai_mat_khau")
    )
    assert response.status_code == 401
    print("Pass - sai password trả về 401!")

#token Auth
response = requests.post(
    "https://httpbin.io/post",
    json = {"username": "user", "password":"pass"}
)
print(response.status_code)
print(response.json())
#giả sử sau khi đăng nhập nhận được  token này
token = "my_secret_token_123"

#Dùng token đề gọi API
response = requests.get(
    "https://httpbin.io/bearer",
    headers={"Authorization": f"Bearer {token}"}
)
print(response.status_code)
print(response.json())

#testcase cho bearer Token:
def test_bearer_token_dung():
    token = "my_secret_token_123"
    response = requests.get(
        "https://httpbin.io/bearer",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["authenticated"] == True
    print("PASS - Token hợp lệ!")

def test_bearer_token_sai():
    response = requests.get(
        "https://httpbin.io/bearer"
        # Không gửi token gì cả
    )
    assert response.status_code == 401
    print("PASS - Không có token trả về 401!")


#JWT: loại token (phổ biến nhất)
import jwt
#tạo jwt token
token = jwt.encode(
    {"user_id": 1, "email":"huyen@gmail.com"},
    "secret_key_phai_dai_hon_32_ky_tu_nhe",
    algorithm="HS256"
)
print("Token:", token)
#giải mã jwt token
data = jwt.decode(
    token,
    "secret_key_phai_dai_hon_32_ky_tu_nhe",
    algorithms=["HS256"]
)
print("Data:",data)
#iwt.encode(): tạo token từ dữ liệu
#{"user_id":1, "email":"..."} : dữ liệu bỏ vào token
#"secret_key": chìa khóa bí mật để mã khóa
#jwt.decode(): giải mã token ra dữ liệu
def test_jwt_hop_le():
    token = jwt.encode(
        {"user_id":1, "email": "huyen@gmail.com"},
        "secret_key_phai_dai_hon_32_ky_tu_nhe",
        algorithm="HS256"
    )
    data = jwt.decode(
        token,
        "secret_key_phai_dai_hon_32_ky_tu_nhe",
        algorithms=["HS256"]
    )
    assert data["user_id"] == 1
    assert data["email"] == "huyen@gmail.com"
    print("Pass - jwt hợp lệ!")
def test_jwt_sai_key():
    token = jwt.encode(
        {"user_id":1},
        "secret_key_phai_dai_hon_32_ky_tu_nhe",
        algorithm="HS256"
    )

    try:
        jwt.decode(token, "key_sai_hoan_toan_abcdefghijk", algorithms=["HS256"])
        assert False, "Phải báo lỗi!"
    except jwt.InvalidSignatureError:
        print("Pass - jwt sai key bị tự chối!")
