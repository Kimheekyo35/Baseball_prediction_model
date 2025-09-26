import streamlit as st
import numpy as np


st.title("투수 및 타자 연봉 예측 모델🤖")


with st.chat_message("assistant"):
    
    st.write("""
이 웹은 KBO 투수와 타자의 다양한 경기 성적 데이터를 기반으로 연봉을 예측하는 모델입니다.
데이터를 탐색하고, 모델을 학습시키고, 새 데이터를 통해 예측해볼 수 있습니다.
""")



