# 챗봇 소켓통신 서버

import threading
import json
import pandas as pd
from chatbot.server.BotServer import BotServer
from chatbot.FindAnswer import FindAnswer
import torch
from sentence_transformers import util, SentenceTransformer
import pickle
from chatbot.db.DatabaseConfig import *
from chatbot.db.Database import Database


# 데이터 로드
data = pd.read_excel('C:/vscode/미니프로젝트/2차프로젝트_챗봇/data/TrainingData2.xlsx')
model = SentenceTransformer('ddobokki/klue-roberta-base-nli-sts-ko-en')
with open('/chatbot/static/embedding_data.pickle', 'rb') as file:
    embedding_data = pickle.load(file)


# 답변 모델
def to_client(conn, addr, params):
    db = params['db']
    try:
        db.connect() # 디비 연결

        # 데이터 수신
        read = conn.recv(2048) # 수신 데이터가 있을 때 까지 블로킹
        print('===========================')
        print('Connection from: %s' % str(addr))
        if read is None or not read:
            # 클라이언트 연결이 끊어지거나, 오류가 있는 경우
            print('클라이언트 연결 끊어짐')
            exit(0)

        # json 데이터로 변환
        recv_json_data = json.loads(read.decode())
        print("데이터 수신 : ", recv_json_data)
        query = recv_json_data['Query']

        # 답변 검색
        try:
            f = FindAnswer(data, model, embedding_data)
            answer = f.return_answer(query)
        except:
            answer = "죄송합니다. 질문 내용을 이해하지 못했습니다."
        send_json_data_str = {
            "Query": query,
            "Answer": answer,
        }

        message = json.dumps(send_json_data_str)
        conn.send(message.encode())
    except Exception as ex:
        print(ex)
    finally:
        if db is not None: # db 연결 끊기
            db.close()
        conn.close()


if __name__ == '__main__':
    # 질문/답변 학습 디비 연결 객체 생성
    db = Database(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
    )
    print("DB 접속")
    port = 5050
    listen = 100

    # 봇 서버 동작
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start")
    while True:
        conn, addr = bot.ready_for_client()
        params = {
            "db": db
        }
        client = threading.Thread(target=to_client,
                                  args=(conn, addr, params))
        client.start()
