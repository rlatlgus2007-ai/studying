import streamlit as st
import pandas as pd

# 1. 앱의 제목을 설정합니다.
st.title('공부 습관 대시보드')

# 2. pandas를 이용해 study.csv 파일을 읽어옵니다.
df = pd.read_csv('study.csv')

# 3. 전체 학생 수, 평균 점수, 평균 공부시간을 계산합니다.
total_students = len(df)
avg_score = df['점수'].mean()
avg_study_time = df['공부시간'].mean()

# 4. 화면을 3개의 열(칸)로 나누어 핵심 지표를 한 줄에 보여줍니다.
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="전체 학생 수", value=f"{total_students}명")
with col2:
    st.metric(label="평균 점수", value=f"{avg_score:.1f}점")
with col3:
    st.metric(label="평균 공부시간", value=f"{avg_study_time:.1f}시간")

st.divider()

# 5. 슬라이더를 만들어 사용자로부터 '최소 공부시간'을 입력받습니다.
# (기본값은 0, 최대값은 데이터 내 공부시간의 최댓값으로 설정합니다.)
max_study_time = float(df['공부시간'].max())
min_study_time = st.slider('최소 공부시간을 선택하세요:', min_value=0.0, max_value=max_study_time, value=0.0)

# 6. 선택한 최소 공부시간 이상인 학생들만 남도록 데이터를 필터링(조건 검색)합니다.
filtered_df = df[df['공부시간'] >= min_study_time]

# 7. 필터링된 데이터를 바탕으로 공부시간과 점수의 관계를 보여주는 산점도를 그립니다.
st.subheader('공부시간과 점수의 관계')
st.scatter_chart(data=filtered_df, x='공부시간', y='점수')

# 8. 필터링된 데이터를 바탕으로 학생별 점수를 보여주는 막대 그래프를 그립니다.
st.subheader('학생별 점수')
st.bar_chart(data=filtered_df, x='학생ID', y='점수')
