import pandas as pd
import plotly.graph_objects as go
import pickle


def getPrediction(option, date):
    if option == 'Бензин':
        with open('models/gazoline_xgboost_model.pkl', 'rb') as file:
            model = pickle.load(file)
    elif option == 'Природный газ':
        with open('models/nature_gaz_xgboost_model.pkl', 'rb') as file:
            model = pickle.load(file)
    prediction = model.predict(pd.DataFrame(date, index=[0]))
    return prediction


def getGazGraph():
    actual_prices = pd.read_csv('data/actual_prices_gaz.csv')
    predicted_prices = pd.read_csv('data/predicted_prices_gaz.csv')
    X_sorted = pd.read_csv('data/X.csv')

    X_sorted['Date'] = pd.to_datetime(X_sorted[['year', 'month', 'day']])

    with open('models/nature_gaz_xgboost_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Создаем график с помощью Plotly
    fig = go.Figure()

    # Добавляем фактические цены
    fig.add_trace(
        go.Scatter(x=X_sorted['Date'], y=actual_prices['Actual_Prices'], mode='lines', name='Фактическая цена'))

    # Добавляем предсказанные цены
    fig.add_trace(
        go.Scatter(x=X_sorted['Date'], y=predicted_prices['Predicted_Prices'], mode='lines',
                   name='Предсказанная цена',
                   line=dict(color='#ff7857'))
    )

    # Настройка макета графика
    fig.update_layout(
        title='График цены природного газа обученной модели в период с 08.09.2000 по 03.05.2024',
        xaxis_title='Дата',
        yaxis_title='Цена',
        showlegend=True,
    )

    return fig


def getGasolineGraph():
    actual_prices = pd.read_csv('data/actual_prices_gasoline.csv')
    predicted_prices = pd.read_csv('data/predicted_prices_gasoline.csv')
    X_sorted = pd.read_csv('data/X.csv')

    X_sorted['Date'] = pd.to_datetime(X_sorted[['year', 'month', 'day']])

    with open('models/gazoline_xgboost_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Создаем график с помощью Plotly
    fig = go.Figure()

    # Добавляем фактические цены
    fig.add_trace(
        go.Scatter(x=X_sorted['Date'], y=actual_prices['Actual_Prices'], mode='lines', name='Фактическая цена'))

    # Добавляем предсказанные цены
    fig.add_trace(
        go.Scatter(x=X_sorted['Date'], y=predicted_prices['Predicted_Prices'], mode='lines',
                   name='Предсказанная цена',
                   line=dict(color='#ff7857'))
    )

    # Настройка макета графика
    fig.update_layout(
        title='График цены бензина обученной модели в период с 08.09.2000 по 20.03.2024',
        xaxis_title='Дата',
        yaxis_title='Цена',
        showlegend=True,
    )

    return fig
