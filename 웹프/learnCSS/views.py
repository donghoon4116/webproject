from django.http import request
from django.shortcuts import render,redirect
from .models import Html_content, Css_content

def index(request): 
    return render(request, 'learnCSS/index.html')

def codeEditor(request):
    html_content=Html_content.objects.all()
    return render(request, 'learnCSS/codeEditor.html',{'html_content':html_content})
# Create your views here.
def html(request):
    html_content= Html_content.objects.all()
    return render(request,'apptest/question_form.html',{'html_content':html_content})
def css(request):
    css_content='213123'
    return render(request,'apptest/question_form.html',{'css_content':css_content})

