from django.shortcuts import render, get_object_or_404
from polls.models import Question
# request: 클라이언트가 서버에 요청을 보내는 작업
# 클라이언트가 서버에 요청을 보낼때 여러가지 정보가 같이 서버에 제공
# 이 내용을 request_라는 객체로 만들어 사용
# response: 서버가 클라이언트에게 결과를 보내는 작업
# Question class 객체 3개를 리스트 안에 넣어서 전달


def index(request):
    # 로직처리 코드
    tmp = Question.objects.all().order_by('-pub_date')[:3]
    context = {'latest_question_list': tmp}
    return render(request, 'index.html', context)


def detail(request, question_id):
    # 로직처리 코드
    # 특정 객체 한개만 구하기
    tmp = get_object_or_404(Question, pk=question_id)
    context = {'question': tmp}
    return render(request, 'detail.html', context)
