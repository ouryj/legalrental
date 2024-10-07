#importing all necessaries packages for the app to run
import pandas as pd
import streamlit as st
import plotly.express as px

# loading dataset via pandas dataframe
df = pd.read_csv('vehicles_us.csv')
#setting a header for the application
st.header('Vehicle Rental Dashboard')
# setting price ranges
lower = df['price'].quantile(0.5)
higher = df['price'].quantile(0.95)

#setting outliers checks

outlier_option = st.checkbox('Any Outliers Preference ?')

if outlier_option:
    new_df = df[(df['price'] >= lower) & (df['price'] <= higher) ]
else:
    new_df = df

#creating a histogram
if st.checkbox('Histogram Price distribution'):
    hist = px.histogram(new_df, x='price', title='Price Distribution Curve')
    st.plotly_chart(hist)

if st.checkbox("Scatter Visual Price Vs Mileage"):
    scatter = px.scatter(new_df,x='price',y='odometer', labels={'price':'USD $$',
                                                                'odometer': 'Miles'}, title='Price Vs Mileage')
    st.plotly_chart(scatter)

#prefer raw data
st.write(new_df)
#run streamlit run app.py on your terminal for the final product

