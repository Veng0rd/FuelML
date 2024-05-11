import pandas as pd
import streamlit as st

from pred import getGasolineGraph, getGazGraph, getPrediction

st.set_page_config(page_title='Прогнозирование')
st.header('Прогнозирование цен на энергоресурсы', divider='rainbow')

option = st.selectbox(
    'На какой энергоресурс вы хотите получить прогнозирование?',
    ('Бензин', 'Природный газ'))

if option == 'Бензин':
    st.plotly_chart(getGasolineGraph())

elif option == 'Природный газ':
    st.plotly_chart(getGazGraph())

date = pd.Timestamp(st.date_input('Введите дату для прогнозирования'))

date_predict = {
    'year': date.year,
    'month': date.month,
    'day': date.day
}

if st.button('Получить прогноз'):
    if option == 'Бензин':
        st.write(f'#### Прогноз цены бензина на {date.date()} =',
                 '```{0:.4f}```'.format(float(getPrediction(option, date_predict))), 'долларов США')

    elif option == 'Природный газ':
        st.write(f'#### Прогноз цены природного газа на {date.date()} =',
                 '```{0:.4f}```'.format(float(getPrediction(option, date_predict))), 'долларов США')
