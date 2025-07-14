from django.shortcuts import render
from .gemini import generate_single_question

def Test(request):
  question = generate_single_question()

  context = {
    'question_data':question
  }
  return render(request,'index.html',context)