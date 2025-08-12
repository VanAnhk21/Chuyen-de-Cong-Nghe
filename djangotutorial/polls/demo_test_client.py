from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse

# Chuẩn bị môi trường test
setup_test_environment()

# Tạo client giả lập request
client = Client()

# Gửi request đến trang chủ "/"
response = client.get("/")
print("Status code / :", response.status_code)  # 404

# Gửi request đến /polls/ (sử dụng reverse tránh hardcode URL)
response = client.get(reverse("polls:index"))
print("Status code /polls/ :", response.status_code)  #200

# In ra nội dung HTML trả về
print(response.content)

# Lấy dữ liệu từ biến context (truyền vào template)
print(response.context["latest_question_list"])
