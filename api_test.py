import requests        # requests — nạp thư viện vào
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print(response.status_code)    # con số 200/404/500...
data = response.json()  #dữ liệu bên trong server trả về (dạng JSON)
print(data["name"])
print(data["email"])
if response.status_code ==200:
    print("Pass - Status code đúng")
else:
    print("Fail - Status code sai")