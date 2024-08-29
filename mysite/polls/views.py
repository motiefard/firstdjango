from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from .models import Question as Q, Choice
# from django.template import loader
# from django.http import Http404



class IndexView(generic.ListView):
    # latest_question_list = Q.objects.order_by("-pub_date")[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     "latest_question_list" : latest_question_list,
    # }
    # output = ",, ".join([q.question_text for q in latest_question_list])
    # output = template.render(context, request)
    # return HttpResponse(output)
    # return render(request, "polls/index.html", context)

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Q.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Q
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Q
    template_name = "polls/results.html"

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