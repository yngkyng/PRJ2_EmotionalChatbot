from django.http import HttpResponse, JsonResponse
from chatbot.FindAnswer import FindAnswer
import numpy as np
import pandas as pd
import torch
from sentence_transformers import util, SentenceTransformer
import pickle


# 데이터 로드
# data = pd.read_excel('C:/vscode/django/Emotion/static/TrainingData2.xlsx')
# model = SentenceTransformer('ddobokki/klue-roberta-base-nli-sts-ko-en')
# with open('C:/vscode/django/Emotion//static/embedding_data.pickle', 'rb') as file:
#     embedding_data = pickle.load(file)

data = pd.read_excel('C:/vscode/django/Emotion/static/TrainingData_total.xlsx')

model2 = SentenceTransformer('ddobokki/klue-roberta-base-nli-sts-ko-en')
model1 = SentenceTransformer('jhgan/ko-sroberta-multitask')
model_list = [model2, model2]

with open('C:/vscode/django/Emotion/static/embedding_data1.pickle', 'rb') as file:
    embedding_data2 = pickle.load(file)
with open('C:/vscode/django/Emotion/static/embedding_data2.pickle', 'rb') as file:
    embedding_data1 = pickle.load(file)
embedding_list = [embedding_data1, embedding_data2]


# 답변 출력
def chatanswer(query):
    try:
        f = FindAnswer(data, model_list, embedding_list)
        answer = f.return_answer(query)
    except:
        answer = "죄송합니다. 질문 내용을 이해하지 못했습니다."
    json = {
        "Query": query,
        "Answer": answer,
    }
    return json


if __name__ == '__main__':
    msg = chatanswer('죽고싶지만 떡볶이는 먹고싶어')
    print(msg)