import streamlit as st
import numpy as numpy
import pandas as pandas


# 페이지 제목 설정
# st.set_page_config(page_title="나의 첫 Streamlit", page_icon="🎈")

# 메인 타이틀
st.title("나의 첫 Streamlit 앱 🎈")
st.write("깃허브를 통해 성공적으로 배포되었습니다! 환영합니다.")

st.divider() # 구분선

# 사용자 입력 받기
name = st.text_input("이름을 입력해 주세요:")

# 버튼 클릭 시 동작
if st.button("인사하기"):
    if name:
        st.success(f"반갑습니다, {name}님! 배포에 성공하셨네요 🎉")
    else:
        st.warning("이름을 먼저 입력해 주세요.")