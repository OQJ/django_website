from django.shortcuts import render,get_object_or_404
from  django.http import  HttpResponse
from  .models import  Question
from django.http import  Http404
from django.template import RequestContext,loader
# Create your views here.
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[0:5]
    template=loader.get_template('jizhangben/index.html')

    context={
        'latest_question_list': latest_question_list,
    }
    return  render(request,'jizhangben/index.html',context)

def results(request,question_id):
    response="You're looking at the results of question %s."
    return  HttpResponse(response%question_id)

def details(request,question_id):
   question=get_object_or_404(Question,pk=question_id)
   return  render(request,"jizhangben/detail.html",{'question':question})

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)