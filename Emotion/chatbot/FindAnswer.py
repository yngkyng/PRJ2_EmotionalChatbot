# 임베딩값으로 답변 검색
import numpy as np
import pandas as pd
import torch
from sentence_transformers import util
import random


class FindAnswer:
    # def __init__(self, data, model, embedding_data):
    #     self.data = data
    #     self.model = model
    #     self.embedding_data = embedding_data
    def __init__(self, data, model_list, embedding_list):
        self.data = data
        self.model = random.choice(model_list)
        if self.model == model_list[0]:
            self.embedding_data = embedding_list[1]
        else:
            self.embedding_data = embedding_list[1]
        # print("선택된 파일:", self.embedding_data)
        # print("선택된 모델:", self.model)

    # 사용자 문장 임베딩
    def return_sim_question(self, input_sentence):
        input_sentence = self.model.encode(input_sentence)
        input_sentence = torch.tensor(input_sentence)
        return input_sentence

    # 임베딩값으로 답변 출력
    def return_answer(self, message):
        message = message.strip()
        # 입력 문장 임베딩
        embedding_sentence = self.return_sim_question(message)

        # 미리 구해진 임베딩 데이터와 현재 임베딩 데이터의 코사인 유사도 추출
        cos_sim = util.pytorch_cos_sim(embedding_sentence, self.embedding_data)
        # cos_sim = cos_sim.cpu()

        # 유사도가 가장 비슷한 질문 인덱스 반환
        best_sim_idx = int(np.argmax(cos_sim))

        # 유사도가 가장 비슷한 질문에 해당하는 답변 제공
        answer = self.data['A'][best_sim_idx]
        return answer