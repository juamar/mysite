from django.http import HttpResponse,  HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question
from .models import Choice
"""Esto es parte de lo serio"""
from django.shortcuts import render

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')
	
	"""Esto es para devolver una tonteria"""
	#output = ', '.join([q.question_text for q in latest_question_list])
	#return HttpResponse(output)
	
	"""Aqui va lo serio"""
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html',context)

def detail(request, question_id):
	#return HttpResponse("You 're looking at question %s." %question_id)
    question = Question.objects.get(pk=question_id)
    return render(request, "polls/detail.html",  {
        "question":question, 
    })

def results(request, question_id):
	#response = "You are looking at the results of questions %s."
	#return HttpResponse(response % question_id)
    question = Question.objects.get(pk=question_id)
    return render(request, "polls/results.html",  {
        "question":question, 
    })
      
def vote(request, question_id):
    question=Question.objects.get(pk=question_id)
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
        return HttpResponseRedirect(reverse("polls:results", args = (question_id, )))
