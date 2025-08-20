import streamlit as st

st.title('ㄴㄱㅁ')

st.write("이것은 기본 텍스트 출력입니다.")

st.markdown("**굵은 텍스트**, *기울임 텍스트*")
st.markdown("""- 첫 번째 항목
- 두 번째 항목
- 여러 줄을 쓸 때""")

st.title("메인 제목입니다")
st.header("중간 제목입니다")
st.subheader("하위 제목입니다")

st.latex(r"E = mc^2")
st.latex(r"\int_{a}^{b} x^2 dx = \frac{b^3 - a^3}{3}")




















