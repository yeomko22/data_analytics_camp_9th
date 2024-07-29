import csv
import pickle

import numpy as np
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt


st.markdown(
    """
<style>
[data-testid="stMetricLabel"] p {
    font-size: 25px;
}
</style>
""",
    unsafe_allow_html=True,
)

st.title("타이타닉 생존율 예측")
st.subheader("만약 내가 타이타닉호에 탔다면 생존률은 얼마일까?")
st.image("./data/banner.png")


@st.cache_data
def load_model():
    with open("./data/model.pkl", "rb") as fr:
        model = pickle.load(fr)
    return model


@st.cache_data
def load_scores():
    scores = []
    with open("./data/scores.csv") as fr:
        reader = csv.reader(fr)
        for row in reader:
            scores.append(float(row[0]))
    return scores


# 모델 로딩하기
data_load_state = st.text('Loading model...')
model = load_model()
scores = load_scores()
data_load_state.text('Loading model...done!')


def inference(sex, age, pclass):
    sex_label = 1 if sex == "Male" else 0
    input_data = [[pclass, sex_label, age]]
    survival_ratio = model.predict(input_data)[0]
    return survival_ratio


def get_distribution_plot(survival_ratio):
    # sns.set(rc={'axes.facecolor': '#FFFFFFFF', 'figure.facecolor': (0, 0, 0, 0)})
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot()
    sns.set_style("whitegrid")
    sns.kdeplot(
        scores,
        fill=True,
        color="#1263e3",
        alpha=0.5,
        linewidth=0,
        ax=ax,
    )
    plt.axvline(survival_ratio, color="coral", linewidth=3, label="YOU")
    plt.xticks(np.arange(0, 1.2, 0.2))
    plt.legend()
    return fig


# 폼 작성하기
with st.form("form"):
    name = st.text_input("이름")
    col1, col2, col3 = st.columns(3)
    with col1:
        sex = st.selectbox("성별", ["Male", "Female"])
    with col2:
        age = st.number_input("나이", format="%d", min_value=0, max_value=100, step=1)
    with col3:
        pclass = st.selectbox("좌석 등급", [1, 2, 3])

    submitted = st.form_submit_button("Submit")
    if submitted:
        if not name:
            st.error("이름을 입력해주세요!")
        else:
            with st.spinner('Wait for it...'):
                survival_ratio = inference(sex, age, pclass)
                fig = get_distribution_plot(survival_ratio)

            st.metric(label=f"{name}님의 생존율은?", value=f"{round(survival_ratio * 100, 2)} %")
            with st.spinner('Plotting...'):
                st.pyplot(fig)
