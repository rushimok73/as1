from django.shortcuts import render
from .models import Question


def owner(request):
       question_list = Question.objects.all()
       print(question_list)
       context  = {'q':question_list}
       return render(request, 'polls/index.html', context)