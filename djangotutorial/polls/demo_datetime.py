import datetime
from django.utils import timezone
from models import Question
# Tạo một Question với pub_date 30 ngày trong tương lai
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))

# Kiểm tra xem nó có được xuất bản gần đây không
print(future_question.was_published_recently())
