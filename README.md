# PRJ2_EmotionalChatbot

## 사용 데이터
AIHub,감성대화말뭉치
https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=86

## 사용 언어
Python(vscode),Django(Pycharm)

## 진행 과정
### 1. 프로젝트 주제 선정 및 데이터 수집

### 2. 데이터 탐색 및 전처리
  * sbert가 아닌 감정 분류 모델 학습을 위한 전처리 (잘 학습되지 않아 프로젝트 결과에 감정 분류 모델은 사용하지 않음)
 
### 3. 챗봇에 적용할 모델 생성
 #### 3-1. LSTM, RNN,CNN 등을 활용한 감정 분류 모델 학습
 * 6가지 감정으로 다중 분류가 가능한 모델을 학습시키고 추후 챗봇에서 그 감정에 맞는 응답을 구현할 예정이었으나, acc 0.1x 선으로 학습되었다.
 * 모델을 개선하기보다 챗봇 구현이라는 목적에 더 적합한 방법으로 프로젝트 계획을 수정함.
    
 #### 3-2. SBERT 모델을 사용한 문장 생성 모델 학습
 ![image](https://github.com/yngkyng/PRJ2_EmotionalChatbot/assets/121409505/33b6d078-caa0-4a85-8f6b-49e4cbffe8f2)
 * STS, NLI 학습을 시도함.
 * STS 학습 완료. NLI 학습까지는 시간 문제로 완료하지 못함.
 * 기존에 학습되어진 여러 모델을 시도해보고 가장 맥락에 맞는 답을 잘 내놓는 모델로 채택. (klue-roberta-base 모델에 nli와 sts 학습을 시킨 모델 선택)

### 4. Django를 이용한 챗봇 제작
   * Emotion
   ![image](https://github.com/yngkyng/PRJ2_EmotionalChatbot/assets/121409505/3aa560e3-dfdc-4d5d-9118-8f53b4ba9783)
