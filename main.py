# 임포트 
import os 
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# API 가져오는 부분
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [("system", "당신은 Kanye 전문가입니다."), ("user","{input}")]
)

# 모델끌고 오기 
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo-0125")

# 출력 처리 해주는 parser 처리 
output_parser = StrOutputParser() 

# 체인 연결 코드 LCEL
chain = prompt | llm | output_parser

# 입출력처리 코드 
# user_input = input("질문을 입력하세요 : ")

# response = chain.invoke({"input": user_input})

# print("Bot : ",response)

# 그라디오 가져오기 
import gradio as gr

def Kanye_Chat(질문하기):
    return chain.invoke({"input": 질문하기})

# 입력 및 출력 컴포넌트를 정의
inputs = gr.Textbox(label="질문을 입력하세요:")
outputs = gr.Text(label="응답:")

# Interface 객체 생성
demo = gr.Interface(
    fn=Kanye_Chat,
    inputs=inputs,
    outputs=outputs,
    title="Kanye Chat Bot",
    description="Kanye 전문가 챗봇에게 질문하고 답변을 받으세요!"
)

demo.launch()