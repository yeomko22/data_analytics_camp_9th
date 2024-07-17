import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt

st.title("Uber pickups in NYC1")
st.text("Uber pickup in NYC data analytics project.")
st.image("./data/banner.png")

DATE_COLUMN = 'date/time'


# cache 적용 후 새로고침하면 그대로 데이터 로딩 과정을 건너 뜀
@st.cache_data
def load_data():
    df = pd.read_csv("./data/uber.csv")
    df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])
    return df


# 데이터 로딩하기
data_load_state = st.text('Loading data...')
df = load_data()
data_load_state.text('Loading data...done!')

# dataframe 출력하기
# toggle button으로 감추기
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(df)


# 주요 지표 나타내기 위한 col 사용
st.subheader("Major metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70", "1.2")
col2.metric("Wind", "9mph", "-8%")
col3.metric("Humidity", "86%", "4%")


# streamlit 내장 bar_chart 함수로 histogram 그리기
st.subheader("Number of pickups by hour with st.bar_chart")
st.text("Usually the order peak time is between 17 - 20")
hist_values = np.histogram(df[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# matplot으로 histogram 그린 뒤, streamlit으로 그리기
st.subheader("Number of pickups by hour with pyplot")
bins = np.arange(0, 25, 1)
plt.figure(figsize=(10, 5))
plt.hist(
    df[DATE_COLUMN].dt.hour,
    bins=bins,
    label="count",
    width=0.8,
)
plt.legend()
plt.xlim(0, 24)
plt.xticks(bins, fontsize=8)
st.pyplot(plt)

# seaborn으로 histogram 그린 뒤, streamlit으로 그리기
st.subheader("Number of pickups by hour with seaborn")
ax = sns.histplot(
    df[DATE_COLUMN].dt.hour,
    bins=bins,
    kde=True,
)
st.pyplot(ax.figure)
