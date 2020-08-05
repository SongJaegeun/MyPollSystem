from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # Table_의 id column_은 default_로 지정
    # id: primary key(Not Null, Unique, autoincrement, int)

    def __str__(self):  # repr(단순 표현 목적), str(연산목적) => 문자열로 표현
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,
                                    on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text