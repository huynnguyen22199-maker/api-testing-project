import anthropic
import requests
client = anthropic.Anthropic(api_key="ANTHROPIC_API_KEY")
def sinh_test_case(api_docs):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{
            "role":"user",
            "content":f""" Dựa vào API docs này, sinh ra 5 test case dạng JSON:{api_docs}
            Trả về đúng format này, không giải thích gì thêm:
            [
                {{"ten": "test hợp lệ", "status_code": 200}},
                {{"ten": "test thiếu field", "status_code": 400}}
            ]"""
        }]
    )
    return message.content[0].text
api_docs = """
Post /register
body:{
    "username": "string",
    "password": "string",
    "email": "string"
}
"""
ket_qua = sinh_test_case(api_docs)
print(ket_qua)

import json
def test_ai_sinh_test_case():
    ket_qua = sinh_test_case(api_docs)
    # Làm sạch kết quả
    ket_qua = ket_qua.strip() # cat khoang trang
    if "```json" in ket_qua:
        ket_qua = ket_qua.split("```json")[1].split("```")[0].strip()
    elif "```" in ket_qua:
        ket_qua = ket_qua.split("```")[1].split("```")[0].strip()
    #chuyển chữ json thành list Python
    danh_sách = json.loads(ket_qua)
    #kiểm tra AI sinh ra đúng 5 test case
    assert len(danh_sách) == 5
    print(f"pass - AI sinh ra{len(danh_sách)} test case!")
    #in ra từng test case
    for test in danh_sách:
        print(f"-{test['ten']} -> {test['status_code']}")

    #fixture trong pytest
import pytest 
@pytest.fixture
def api_client():
    return requests.Session()
    #@pytest.fixture: đánh dấu hàm này là fixture
    #requests.session(): tạo 1 session dùng chung cho tất cả test, thay vì mỗi test tự tạo connection riêng.
def test_lay_user(api_client):
    response = api_client.get(
    "https://jsonplaceholder.typicode.com/users/1"
    )
    assert response.status_code == 200
    print("Pass - lấy user thành công!")  
    # def test_lay_user(api_client): truyền fixture vào như tham số
    #pytest tự động nhận ra 'api_client' là fixture và truyền vào
#Lưu ý: Trong python, code bên trong hàm chỉ chạy khi khi hàm đó được gọi - và chỉ tồn tại trong phạm vi hàm đó thôi.

    #parametrize : chạy 1 test với nhiều dữ liệu khác nhau
@pytest.mark.parametrize("user_id, status_code", [
    (1, 200),
    (2, 200),
    (9999, 404),
])
def test_lay_nhieu_user(user_id, status_code):
    reponse = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    )
    assert reponse.status_code == status_code
    print(f"Pass - user {user_id} trả về {status_code}!")
    #@pytest.mark.paramatrize : chạy test nhiều lần với data khác nhau\
    #"user_id, status_code": tên các tham số
    #[(1, 200), (2, 200), (9999, 404)]: 3 bộ data khác nhau
    #pytest tự chạy 3 lần với 3 bộ data đó.
