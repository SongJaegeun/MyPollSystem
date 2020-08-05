from django.contrib import admin
from polls.models import Question, Choice

# () <- 등록할 클래스명
admin.site.register(Question)
admin.site.register(Choice)
