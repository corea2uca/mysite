import datetime                     # 전체 모듈 가져옴(py내장 모듈)
from django.utils import timezone   # utils 중에 필요한 timezone만 가져옴
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # def str(self):        # 차후 테스트, <Question object (1)>
    def __str__(self):      # "What's new?" (사람이 읽기 쉬운 텍스트)
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text