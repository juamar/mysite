from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question
from .models import Choice
"""Esto es parte de lo serio"""
from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
      
def vote(request, pk):
    question=Question.objects.get(pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,  Choice.DoesNotExist):
        return render(request, 'polls/detail.html',  {
            'question':question, 
            'error_message':"You didn't select a choice.", 
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args = (pk, )))
