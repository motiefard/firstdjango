from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question as Q
# from django.template import loader
from django.http import Http404



def index(request):
    latest_question_list = Q.objects.order_by("-pub_date")[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        "latest_question_list" : latest_question_list,
    }
    # output = ",, ".join([q.question_text for q in latest_question_list])
    # output = template.render(context, request)
    # return HttpResponse(output)
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # try:
    #     question = Q.objects.get(pk=question_id)
    # except Q.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Q, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)