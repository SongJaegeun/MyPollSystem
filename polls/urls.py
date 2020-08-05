from django.urls import path
from . import views

app_name = 'polls'
# http://localhost:8080/polls/polls

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail')

]

