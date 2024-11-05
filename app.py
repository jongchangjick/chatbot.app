from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# .env 파일 경로를 명시적으로 지정
load_dotenv()

# API 키 설정
genai.configure(api_key="AIzaSyC9B9P49UI_aPelB6fDnPe_dSMFs5v2nM8v")

# 환경 변수 확인
api_key = os.getenv("GOOGLE_API_KEY")
if api_key is None:
    print("API key not found!")
else:
    print(f"Loaded API Key: {api_key}")  # 로드된 API 키 출력


st.set_page_config(page_title="Chat Bot of SON", page_icon="🗣️")
st.header("Chat Bot Web Application of SON")

question = st.text_input("Write a prompt....")
submit = st.button("submit")

if submit:
    model = genai.GenerativeModel("gemini-1.5-flash")
    answer = model.generate_content(question)
    st.write(answer.text)
