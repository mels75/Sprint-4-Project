import pandas as pd
import streamlit as st
import plotly_express as px
vehicles_df = pd.read_csv('notebooks/vehicles_us.csv') 
st.header('Software Development Tools Project')

vehicles_df['model_year'] = vehicles_df['model_year'].fillna(vehicles_df['model_year'].median())

fig = px.scatter(vehicles_df, x='model_year',
                 y = 'price',
                 title = 'Price and Model Year',
                 labels = {'model_year' : 'Model Year', 'price' : 'Sell Price'})
fig.update_yaxes(range=[5000, 200000])
st.plotly_chart(fig)

show_histogram = st.checkbox('Show Histogram')

if show_histogram:
    fig = px.histogram(vehicles_df, x='type', title = 'Stock of Car Type', labels={'type':'Car Type'})
    fig.update_layout(yaxis_title = 'Amount in Stock')
    st.plotly_chart(fig)
    