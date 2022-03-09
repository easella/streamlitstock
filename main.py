import streamlit as st
from datetime import time 
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot
from plotly import graph_objs as go
START="2015-01-01"
TODAY=date.today().strftime("%Y-%m-%d")
st.title("Stock Prediction App")
stocks=("NLSN","PYPL","NET","APPL","SHARP","CL=F")
selected_stocks=st.selectbox("Select stock for prediction",stocks)
n_years=st.slider("Years of prediction:",1,10)
period=n_years*365
