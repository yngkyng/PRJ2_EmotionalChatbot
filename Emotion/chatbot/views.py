from django.shortcuts import render, redirect
from chatbot.mychatbot import chatanswer
from chatbot.models import Chat
from django.http import JsonResponse
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "c:/vscode/django/Emotion/templates/chatbot/chathome.html")



def query(question):
    question = question.GET["question"]
    msg = chatanswer(question)
    Query = msg['Query']
    Answer = msg['Answer']

    #레코드에 저장
    # Chat(query=query).save()
    # Chat(answer=answer).save()
    # print('저장되었습니다.')
    # items=Chat.objects
    # return render(request, 'C:/vscode/django/Emotion/templates/chatbot/result.html', {'items':items})

    return JsonResponse(msg, content_type="application/json")