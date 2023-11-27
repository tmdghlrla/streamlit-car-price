import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app() :
    st.subheader('데이터 분석')
    choice_menu = ['전체 데이터 확인하기','통계 데이터 보기']
    selected_menu=st.tabs(choice_menu)

    df=pd.read_csv('data/Car_Purchasing_Data.csv')

    with selected_menu[0] :    
        st.text('전체 데이터')
        st.dataframe(df)
    
    with selected_menu[1] :
        st.text('통계데이터')
        st.dataframe(df.describe())

        st.text('최대 / 최소 데이터 확인하기')

        column_list=df.columns[4:]
        selected_columns=st.selectbox('컬럼을 선택하세요',column_list)
        st.text(selected_columns + '컬럼의 최소값')
        st.dataframe(df.loc[df[selected_columns]==df[selected_columns].min(),])
        st.text(selected_columns + '컬럼의 최대값')
        st.dataframe(df.loc[df[selected_columns]==df[selected_columns].max(),])
        st.text(selected_columns + '컬럼의 희스토그램')
        fig1=plt.figure(figsize=(3,2))
        plt.hist(data=df, x=selected_columns, rwidth=0.8, bins=10)
        st.pyplot(fig1, use_container_width=False)