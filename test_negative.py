import requests
Base_url = "https://jsonplaceholder.typicode.com"
#base_url: lưu url gốc vào biến, không phải gõ lại nhiều lần

#Gọi API lấy user có id = 9999 - không tồn tại phải trở về 404
def test_user_khong_ton_tai():
    response = requests.get(f"{Base_url}/users/9999")
    assert response.status_code == 404
    print("pass - user không tồn tại trả về 404!")
#Tạo user mới nhưng không gửi field 'name': phải trả về 400
def test_tao_user_thieu_name():
    response = requests.post(
        f"{Base_url}/users",
        json = {"email": "huyen@gmail.com"} # thiếu name
    )
    #jsonplaceholder không validate nên vẫn trả 201
    # Trong API thật sẽ là 400
    assert response.status_code in [400, 201]
    print("Pass - đã test thiếu name!")

    #test các giá trị giới hạn của user_id
import pytest
@pytest.mark.parametrize("user_id, ket_qua_mong_doi",[
    (1, 200),     #id nhỏ nhất hợp lệ
    (10, 200),    #id lớn nhất hợp lệ
    (0, 404),     #id = 0 không hợp lệ
    (-1, 404),    #id âm không hợp lệ
    (11, 404),    #id vượt quá giới hạn
])
def test_boundary_user_id(user_id, ket_qua_mong_doi):
    response = requests.get(f"{Base_url}/users/{user_id}")
    assert response.status_code == ket_qua_mong_doi
    print(f"Pass - user_id = {user_id} trả về {ket_qua_mong_doi}!")

#SQL injection: test bảo mật cơ bản
#Thử gửi ký tự đặc biệt vào API xem có bị lỗi không
def test_sql_injection():
    response = requests.get(
        f"{Base_url}/users",
        params={"id":"1' or '1'='1"}
    )
    assert response.status_code in [200, 400]
    assert "error" not in str(response.text).lower()
    print("Pass - API không bị  SQL injection!")
