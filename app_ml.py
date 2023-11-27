import streamlit as st
import joblib
import numpy as np

def run_ml_app() :
    st.subheader('구매 금액 예측')
    # 인공지능 파일 읽어와서
    # 예측하는 화면을 개발한다.

    regressor=joblib.load('model/regressor.pkl')

    gender = st.radio('성별 선택', options=['여자', '남자'])

    if gender =='여자' :
        gender=0

    elif gender =='남자' :
        gender=1

    age = st.number_input('나이 입력', min_value=20, max_value=100)
    salary = st.number_input('연봉 입력', min_value=1000, max_value=1000000)
    debt = st.number_input('카드빚 입력', min_value=0, max_value=100000)
    worth = st.number_input('자산 입력', min_value=0, max_value=1000000)
    
    
    prediction = np.array([gender, age, salary, debt, worth])
    prediction=prediction.reshape(1,5)

    y_pred=regressor.predict(prediction)[0]
    if st.button('구매 예상 금액 예측') :
        # 예측한 결과를 화면에 보여준다.
        if y_pred <= 0 :
            st.text('차를 구매하는 것을 추천하지 않습니다.')
        elif y_pred > 0 :
            st.text("구매 예상 금액은 " + str("{:.2f}".format(y_pred)) + " 달러 입니다." )
        
    else :
        st.text('')
