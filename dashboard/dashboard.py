import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

def create_pollution_A_df(df):
    mean_poll_A_df = df.resample(rule='Y', on='Date').agg({
        'PM2.5_A': 'mean',
        'PM10_A': 'mean',
        'SO2_A': 'mean',
        'NO2_A': 'mean',
        'CO_A': 'mean',
        'O3_A': 'mean'
    })

    mean_poll_A_df.index = mean_poll_A_df.index.strftime('%Y')
    mean_poll_A_df = mean_poll_A_df.reset_index()
    return mean_poll_A_df

def create_pollution_C_df(df):
    mean_poll_C_df = df.resample(rule='Y', on='Date').agg({
    'PM2.5_C' : 'mean',
    'PM10_C' : 'mean',
    'SO2_C' : 'mean',
    'NO2_C' : 'mean',
    'CO_C' : 'mean',
    'O3_C' : 'mean'
})

    mean_poll_C_df.index = mean_poll_C_df.index.strftime('%Y')
    mean_poll_C_df = mean_poll_C_df.reset_index()
    return mean_poll_C_df

def create_avg_temp_df(df):
    avg_temp_df = df.resample(rule='Y', on='Date').agg({
        'TEMP_A' : 'max',
        'TEMP_C' : 'max'
})

    avg_temp_df.index = avg_temp_df.index.strftime('%Y')
    avg_temp_df = avg_temp_df.reset_index()
    return avg_temp_df

    # ------------------------------------------------------- #
air_df = pd.read_csv('https://raw.githubusercontent.com/RakhaHanif/air-quality-analysis/main/dashboard/air_df.csv')
air_df['Date'] = pd.to_datetime(air_df['Date'])

min_date = air_df['Date'].min()
max_date = air_df['Date'].max()


with st.sidebar:
        st.header('Air Quality Data Analysis')
        st.image('tornado.png')

        start_date, end_date = st.date_input(
            label='Select a time range :', min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
main_df = air_df[(air_df['Date'] >= str(start_date)) & 
                        (air_df['Date'] <= str(end_date))] 

mean_poll_A_df = create_pollution_A_df(main_df)
mean_poll_C_df = create_pollution_C_df(main_df)
avg_temp_df =  create_avg_temp_df(main_df)

st.header('Air Quality Dashboard 🌪🟡')
st.markdown(
    """
    - Nama: Rakha Hanif Maheswara
    - Email: rakhahanif21@gmail.com
    - ID Dicoding: rakhahanif21
    """
)
st.subheader('Air Pollution Levels')
col1, col2, col3= st.columns(3)
with col1:
    cnt_rent = main_df['No'].sum()
    formatted_cnt_rent = '{:,.0f}'.format(cnt_rent).replace(',', '.')
    st.metric('Amount of data', value=formatted_cnt_rent)
with col2:
    cnt_rent = main_df['TEMP_A'].max()
    formatted_cnt_rent = '{:,.0f}'.format(cnt_rent).replace(',', '.')
    st.metric('Aotizhongxin Supreme Temperature', value=formatted_cnt_rent)
with col3:
    cnt_rent = main_df['TEMP_C'].max()
    formatted_cnt_rent = '{:,.0f}'.format(cnt_rent).replace(',', '.')
    st.metric('Changping Supreme Temperature', value=formatted_cnt_rent)

tab1, tab2, tab3 = st.tabs(['Aotizhongxin Pollution Level', 'Changping Pollution Level', 'Highest Temperature'])
with tab1:
    st.subheader('Average Air Pollution in Aotizhongxin 📈')
    st.write('\*Use the date input in the sidebar to organize the visualization')

    # Plotting menggunakan plotly.express
    mean_poll_A_chart = px.line(
        mean_poll_A_df,
        x='Date',
        y=mean_poll_A_df.columns[1:],  # Gunakan semua kolom kecuali 'Date'
        title='Average Pollution Concentration based on Year',
        markers=True
    )
    
    # Update layout
    mean_poll_A_chart.update_layout(
        xaxis_title='Year',
        yaxis_title='Pollution Levels'
    )

    st.plotly_chart(mean_poll_A_chart)

with tab2:
    st.subheader('Average Air Pollution in Changping 📈')
    st.write('\*Use the date input in the sidebar to organize the visualization')

    mean_poll_C_chart = px.line(
        mean_poll_C_df,
        x='Date',
        y=mean_poll_C_df.columns[1:],  # Gunakan semua kolom kecuali 'Date'
        title='Average Pollution Concentration based on Year',
        markers=True
    )
    
    # Update layout
    mean_poll_C_chart.update_layout(
        xaxis_title='Year',
        yaxis_title='Pollution Levels'
    )
    st.plotly_chart(mean_poll_C_chart)

with tab3:
    st.subheader('Highest Temperature in Each City 📈')
    st.write('\*Use the date input in the sidebar to organize the visualization')
    
    avg_temp_chart = px.line(
        avg_temp_df,
        x='Date',
        y=avg_temp_df.columns[1:],  # Gunakan semua kolom kecuali 'Date'
        title='Highest Temperature Based on Year',
        markers=True
    )
    
    # Update layout
    avg_temp_chart.update_layout(
        xaxis_title='Year',
        yaxis_title='Pollution Levels'
    )
    st.plotly_chart(avg_temp_chart) 

st.write('*The column with the last name _A belongs to Aotizhongxin city, while the column with the last name _C belongs to Changping city')
st.caption('Copyright (c) 2024 by Rakha')