from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    '''This function will show the latest question list of the poll website:
    
        :parem request: This will take the request from the user
        
        :returns: Takes user to polls website
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html",context)

# Giving detail of the question
def detail(request, question_id):
    '''Going to the detail website of each individual question:

        :parem request: The request of the user
        :parem question ID: This is the ID of the question
        
        :returns: Takes user to that individual question to the detail website
    '''
    return render(request, "polls/detail.html",{"question":Question.objects.get(pk=question_id)})

# Giving the vote of the question
@login_required
def vote(request, question_id):
    '''To vote on that specific question:
    
        :parem request: Request from the user
        :parem question ID : This is the question's ID
        
        :returns: To either the display website if the user didn't choose or to the result website
    '''
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # This function will prevent that data will not be posted twice
        return HttpResponseRedirect(
            reverse('polls:result', args=(question_id))
        )
        
# This will represents the final page display      
def results(request, question_id):
    '''The results of the voting of that individual question:

        :parem request: The request of the user
        :parem Question ID: This is the ID of the question
        
        :returns: To reults page of the question
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
