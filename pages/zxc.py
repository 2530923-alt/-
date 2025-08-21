import streamlit as st

st.title('김준 R.I.P')


tab1, tab2 = st.tabs(["박채윤", "154"])  # 2개의 탭 생성

with tab1:
    fuck = st.selectbox('선택해주세요:', [1])

    fuck_data = {'you' : {'r"E = mc^2"'}}

    if st.button('fuckyou'):
        if fuck in fuck_data:
            you = fuck_data[fuck]['you']
            st.write(f"**fuck**: {you}")
    
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용




























