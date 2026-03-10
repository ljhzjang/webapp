import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="숫자 맞추기 게임", page_icon="🎮")

st.title("🎮 1~100 숫자 맞추기 (UP & DOWN)")
st.write("컴퓨터가 생각한 1부터 100 사이의 숫자를 맞춰보세요!")
st.divider()

# 게임 상태(정답, 시도 횟수, 종료 여부)를 기억하기 위한 세션 상태 초기화
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# 숫자 입력받기
guess = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1)

# 정답 확인 버튼
if st.button("정답 확인"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1
        
        if guess < st.session_state.target_number:
            st.warning(f"⬆️ UP! {guess}보다 큽니다. (현재 시도: {st.session_state.attempts}번)")
        elif guess > st.session_state.target_number:
            st.warning(f"⬇️ DOWN! {guess}보다 작습니다. (현재 시도: {st.session_state.attempts}번)")
        else:
            st.success(f"🎉 정답입니다! 컴퓨터가 생각한 숫자는 {st.session_state.target_number}였습니다.")
            st.info(f"총 {st.session_state.attempts}번 만에 맞추셨네요!")
            st.balloons() # 축하 애니메이션
            st.session_state.game_over = True
    else:
        st.warning("이미 정답을 맞추셨습니다. 새 게임을 시작해 주세요!")

st.divider()

# 새 게임 시작 버튼
if st.session_state.game_over:
    if st.button("🔄 새 게임 시작하기"):
        # 상태 초기화 후 화면 새로고침
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()