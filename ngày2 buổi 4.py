import  requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)
print(response.json())


assert response.status_code==200  # assert: khẳng định cáu này phải đúng, nếu đúng -> chạy tiết, nếu sai -> báo lỗi ngay
print("pass-status code đúng")
data = response.json()
assert data["name"]=="Leanne Graham"
print("Pass - Tên đúng")

new_user = {
    "name": "Huyen",
    "email": "huyen@gmail.com"
}
response_post = requests.post(  #requests.post() - gửi Post request
    "https://jsonplaceholder.typicode.com/users",
    json=new_user   #json=new_user : gửi kèm dữ liệu dạng json
)
print(response_post.status_code)
print(response_post.json())
assert response_post.status_code == 201
assert response_post.json()["name"] == "Huyen"
print("Pass - Tại user thành công")