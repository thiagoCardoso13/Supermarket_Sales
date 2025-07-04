import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')
df

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))
month = st.sidebar.selectbox('Month', df['Month'].unique())

df_filtered = df[df['Month'] == month]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x='Date', y='Total', color='City', title='Invoicing per day')
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x='Date', y='Product line', color='City',
                  title='Invoicing by type of product', orientation='h')
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()
fig_city = px.bar(city_total, x='City', y='Total', title='Invoicing by subsidiary')
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(df_filtered, values='Total', names='Payment', title='Invoicing by payment method')
col4.plotly_chart(fig_kind, use_container_width=True)

city_rating = df_filtered.groupby('City')[['Rating']].mean().reset_index()
fig_rating = px.bar(city_rating, x='City', y='Rating', title='Evaluation')
col5.plotly_chart(fig_rating, use_container_width=True)