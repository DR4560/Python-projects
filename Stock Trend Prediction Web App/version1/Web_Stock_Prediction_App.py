#BUlding a stock prediction web app in python
#Source code - Patrick Loeber code base


import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from streamlit import selectbox
import pandas as pd

START = "2016-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Web Application - Stock Prediction App")

stocks = ("AAPL", "GOOG", "yahoo", "MSFT", "GME")
selected_stocks_list = st.selectbox("Select dataset for prediction", stocks)

selected_years = st.slider("Years of prediction:", 1,5)
selected_period = selected_years * 365

#for data cashing

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace = True)
    return data

data_load_state = st.text("Load data...")
data = load_data(selected_stocks_list)
data_load_state.text("Data has been loaded!")

st.subheader('Raw data')
st.write(data.tail())

################FIX 'REMOVEROWS´
data = data.dropna(subset=['Date', 'Close'])

#Plot data
def plot_data():
    #better then matplotlib grapf cuz` is an object-oriented
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y = data['Open'], z = 'stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y = data['Close'], z = 'stock_open'))
    fig.layout.update(title_text="Time series Data", xaxis_rangeslider_visible = True)
    st.plotly_chart(fig)

plot_data()

#Forecasting with FBprophet
#Step - prepare some data for Prophet
df_train = data [['Date', 'Close']]
df_train = df_train.rename(columns ={"Date": "ds", "Close": 'm'})

##########FIX 'y to NUM'
df_train['y'] = pd.to_numeric(df_train['y'], errors='coerce')
###########FIX 'REMOVE NAN in y'
df_train = df_train.dropna(subset=['y'])

#DEBUG 'dataframes structure and types - show'
st.write(df_train)
st.write(df_train.dtypes)

m = Prophet()
m.fit(df_train)

future = m.make_future_dataframe(periods = selected_period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())

st.write('forecast data plot')
fig2_1 = plot_plotly(m, forecast)
st.plotly_chart(fig2_1)

st.write('forecast components')
fig2_2 = m.plot_components(forecast)
st.write(fig2_2) #not a plotly_chart

