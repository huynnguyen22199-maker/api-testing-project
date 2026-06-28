def test_cong():
    ket_qua = 1+1
    assert ket_qua == 2

#def test_cong(): tên hàm phải bắt đầu bằng test_ thì pytest mới chạy
#assert ket_qua ==2 : kiểm tra kết quả đúng không

def test_tru():
    ket_qua = 10 - 3
    assert ket_qua == 7

import requests
def test_lay_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200

def test_ten_user_dung():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert data["name"]== "Leanne Graham"
def test_user_khong_ton_tai():
    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    assert response.status_code == 404