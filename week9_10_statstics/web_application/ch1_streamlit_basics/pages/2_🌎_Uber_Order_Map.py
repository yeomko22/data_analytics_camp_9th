import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st
import numpy as np
import seaborn as sns

st.title("Uber pickups in NYC1")

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

# 슬라이드 바로 시간대 필터링하기
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_df = df[df[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader("Map of all pickups")
st.map(filtered_df)
