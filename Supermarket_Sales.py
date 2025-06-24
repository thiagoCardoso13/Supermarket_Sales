{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "909ccd19-2323-4546-8ff8-47b912f8345e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f6bb5cf5-03b3-42f2-b20c-0cc0f83dde93",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.set_page_config(layout='wide')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f263ade7-d77d-4816-b361-9fc0fba69026",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Invoice ID</th>\n",
       "      <th>Branch</th>\n",
       "      <th>City</th>\n",
       "      <th>Customer type</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Product line</th>\n",
       "      <th>Unit price</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Tax 5%</th>\n",
       "      <th>Total</th>\n",
       "      <th>Date</th>\n",
       "      <th>Time</th>\n",
       "      <th>Payment</th>\n",
       "      <th>cogs</th>\n",
       "      <th>gross margin percentage</th>\n",
       "      <th>gross income</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>750-67-8428</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Female</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>74.69</td>\n",
       "      <td>7</td>\n",
       "      <td>26.1415</td>\n",
       "      <td>548.9715</td>\n",
       "      <td>1/5/2019</td>\n",
       "      <td>13:08</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>522.83</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>26.1415</td>\n",
       "      <td>9.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>226-31-3081</td>\n",
       "      <td>C</td>\n",
       "      <td>Naypyitaw</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Female</td>\n",
       "      <td>Electronic accessories</td>\n",
       "      <td>15.28</td>\n",
       "      <td>5</td>\n",
       "      <td>3.8200</td>\n",
       "      <td>80.2200</td>\n",
       "      <td>3/8/2019</td>\n",
       "      <td>10:29</td>\n",
       "      <td>Cash</td>\n",
       "      <td>76.40</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>3.8200</td>\n",
       "      <td>9.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>631-41-3108</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>46.33</td>\n",
       "      <td>7</td>\n",
       "      <td>16.2155</td>\n",
       "      <td>340.5255</td>\n",
       "      <td>3/3/2019</td>\n",
       "      <td>13:23</td>\n",
       "      <td>Credit card</td>\n",
       "      <td>324.31</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>16.2155</td>\n",
       "      <td>7.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>123-19-1176</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Male</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>58.22</td>\n",
       "      <td>8</td>\n",
       "      <td>23.2880</td>\n",
       "      <td>489.0480</td>\n",
       "      <td>1/27/2019</td>\n",
       "      <td>20:33</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>465.76</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>23.2880</td>\n",
       "      <td>8.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>373-73-7910</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Sports and travel</td>\n",
       "      <td>86.31</td>\n",
       "      <td>7</td>\n",
       "      <td>30.2085</td>\n",
       "      <td>634.3785</td>\n",
       "      <td>2/8/2019</td>\n",
       "      <td>10:37</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>604.17</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>30.2085</td>\n",
       "      <td>5.3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0   Invoice ID Branch       City Customer type  Gender  \\\n",
       "0           0  750-67-8428      A     Yangon        Member  Female   \n",
       "1           1  226-31-3081      C  Naypyitaw        Normal  Female   \n",
       "2           2  631-41-3108      A     Yangon        Normal    Male   \n",
       "3           3  123-19-1176      A     Yangon        Member    Male   \n",
       "4           4  373-73-7910      A     Yangon        Normal    Male   \n",
       "\n",
       "             Product line  Unit price  Quantity   Tax 5%     Total       Date  \\\n",
       "0       Health and beauty       74.69         7  26.1415  548.9715   1/5/2019   \n",
       "1  Electronic accessories       15.28         5   3.8200   80.2200   3/8/2019   \n",
       "2      Home and lifestyle       46.33         7  16.2155  340.5255   3/3/2019   \n",
       "3       Health and beauty       58.22         8  23.2880  489.0480  1/27/2019   \n",
       "4       Sports and travel       86.31         7  30.2085  634.3785   2/8/2019   \n",
       "\n",
       "    Time      Payment    cogs  gross margin percentage  gross income  Rating  \n",
       "0  13:08      Ewallet  522.83                 4.761905       26.1415     9.1  \n",
       "1  10:29         Cash   76.40                 4.761905        3.8200     9.6  \n",
       "2  13:23  Credit card  324.31                 4.761905       16.2155     7.4  \n",
       "3  20:33      Ewallet  465.76                 4.761905       23.2880     8.4  \n",
       "4  10:37      Ewallet  604.17                 4.761905       30.2085     5.3  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('supermarket_sales.csv', sep=';', decimal=',')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "20c0f65d-5b5d-4a11-97d3-36dbdc4e6b90",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Date'] = pd.to_datetime(df['Date'])\n",
    "df = df.sort_values('Date')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f6cfdf77-571b-45c4-9a82-c85d1e08726f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-24 16:48:32.110 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`\n",
      "2025-06-24 16:48:32.480 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Anaconda\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))\n",
    "month = st.sidebar.selectbox('Month', df['Month'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1459b070-c72f-4160-9691-9cfb538bbd36",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_filtered = df[df['Month'] == month]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a246698e-12bc-46b0-af25-2f50c202e75c",
   "metadata": {},
   "outputs": [],
   "source": [
    "col1, col2 = st.columns(2)\n",
    "col3, col4, col5 = st.columns(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "9eb21e60-07d0-4ceb-8151-b5b736303ceb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fig_date = px.bar(df_filtered, x='Date', y='Total', color='City', title='Invoicing per day')\n",
    "col1.plotly_chart(fig_date, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8af9e828-2aa5-4917-93ae-03d54f5ed02c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fig_prod = px.bar(df_filtered, x='Date', y='Product line', color='City',\n",
    "                  title='Invoicing by type of product', orientation='h')\n",
    "col2.plotly_chart(fig_prod, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "0170fb28-67a2-4b17-a8f9-dd3adc6d07b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city_total = df_filtered.groupby('City')[['Total']].sum().reset_index()\n",
    "fig_city = px.bar(city_total, x='City', y='Total', title='Invoicing by subsidiary')\n",
    "col3.plotly_chart(fig_city, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "9963c7c5-e680-4a2e-8f2b-cb2e96c8147a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fig_kind = px.pie(df_filtered, values='Total', names='Payment', title='Invoicing by payment method')\n",
    "col4.plotly_chart(fig_kind, use_container_width=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a94eee21-91de-4b67-b466-63b2f74bce90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city_rating = df_filtered.groupby('City')[['Rating']].mean().reset_index()\n",
    "fig_rating = px.bar(city_rating, x='City', y='Rating', title='Evaluation')\n",
    "col5.plotly_chart(fig_rating, use_container_width=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
