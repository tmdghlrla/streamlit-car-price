import streamlit as st

from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app


def main() :
    st. title('자동차 가격 예측 대시보드')
    menu = ['Home', 'EDA', 'ML']

    choice_side_menu =st.sidebar.selectbox('메뉴 선택', options=menu)

    if choice_side_menu == menu[0] :
        run_home_app()
    elif choice_side_menu == menu[1] :
        run_eda_app()
    elif choice_side_menu == menu[2] :
        run_ml_app()

if __name__ == '__main__' :
    main()