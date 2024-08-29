from django.urls import reverse
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question as Q, Choice
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
    question = get_object_or_404(Q, pk=question_id)
    # response = "You're looking at the results of question %s."
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Q, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("results", args=(question.id,)))