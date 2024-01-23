from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# from django.template import loader
from .models import Question, Choice
from django.http import Http404


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})

    #### It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

    # There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). It raises Http404 if the list is empty.


def results(request, question_id):
    response = "You're looking at the results of question %s."
    me = []
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    return HttpResponse("You're voting on question %s." % question_id)
