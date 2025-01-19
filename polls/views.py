from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Choice, Question
from django.http import Http404
from django.views import generic

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    # return HttpResponse("views.vote: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, "polls/detail.html", {
                "question": question,
                "error_message": "vote error - You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        # selected_choice.votes += 1
        selected_choice.save()
        # 결과 페이지 refresh 하더라도, 다시 폼 데이터가 전송x, 
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # 결과 페이지 refresh 하면, 재전송
        # return render(request, "polls/results.html", {"question": question})
