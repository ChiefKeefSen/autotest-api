import httpx
from tools.http.fakers import fake

create_user_payload = {
    "email": fake.email(),,
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(f"Create user data:", create_user_response_data)

login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"Login data:", login_response_data)

create_file_headers = {
    "Authorization": f"Bearer {login_response_data["token"]['accessToken']}"
}

# with open("C:/Users/EpticExp/Desktop/test.jpg", "rb") as f:
#     # Все параметры передаем в files
#     create_file_response = httpx.post(
#         url="http://localhost:8000/api/v1/files",
#         data={
#             "filename": "test",
#             "directory": "courses"
#         },
#         files={
#             "upload_file": ("test.jpg", f, "image/jpeg"),  # (имя, объект, mime-type)
#                # (None, значение) для обычных полей
#         },
#         headers=create_file_headers
#     )

create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data={
        "filename": "test3.jpg",
        "directory": "courses"
    },
    files={
        "upload_file": open("C:/Users/EpticExp/Desktop/test3.jpg", "rb")
    },
    headers=create_file_headers
)
create_file_response_data = create_file_response.json()
print(f"Create file data:", create_file_response_data)