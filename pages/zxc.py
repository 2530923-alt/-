import streamlit as st

st.title('공식')


tab1, tab2 = st.tabs(["수학", "물리"])  # 2개의 탭 생성

with tab1:
    mbti = st.selectbox('MBTI를 선택해주세요:', [
    'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP'
])

    
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용




























