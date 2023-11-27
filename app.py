import streamlit as st
from streamlit_option_menu import option_menu

from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app

def main() :
    st.set_page_config(layout='wide')
    st. title('자동차 가격 예측 대시보드')
    menu = ['Home', 'EDA', 'ML']

    with st.sidebar:
     choice_side_menu = option_menu("Menu", menu,
                         icons=['car-front-fill', 'clipboard-data', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#d3d3d3"},
    }
    )

    if choice_side_menu == menu[0] :
        run_home_app()
    elif choice_side_menu == menu[1] :
        run_eda_app()
    elif choice_side_menu == menu[2] :
        run_ml_app()

if __name__ == '__main__' :
    main()