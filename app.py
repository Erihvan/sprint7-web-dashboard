import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Sales Dashboard')

if st.button('Show Price Histogram'):
    fig = px.histogram(
        df,
        x='price',
        title='Distribution of Vehicle Prices'
    )
    st.plotly_chart(fig)

if st.button('Show Price vs. Mileage'):
    fig = px.scatter(
        df,
        x='odometer',
        y='price',
        title='Price vs. Mileage'
    )
    st.plotly_chart(fig)