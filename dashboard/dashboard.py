import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

hour_df = pd.read_csv("https://raw.githubusercontent.com/ekobw/bike_sharing/main/dashboard/all_hour.csv")

st.header('Bike Sharing Data Analysis Project :bike:')


st.subheader('Average Rental Bikes per Day')

average_rental_bike = hour_df.groupby('weekday')['cnt'].mean().sort_values(ascending=False)
average_rental_bike_list = average_rental_bike.index.tolist()

fig, ax = plt.subplots(figsize=(8, 6))
ax = sns.barplot(hour_df, x='cnt', y='weekday', estimator='mean', order=average_rental_bike_list, errorbar=None)
ax.bar_label(ax.containers[0], fontsize=10)
ax.set_title('Average Rental Bikes per Day')
ax.set_xlabel('Rental Bikes')
ax.set_ylabel('Day')
st.pyplot(plt)


st.subheader('Rental Bikes per Season per Year')

season_per_year = pd.pivot_table(hour_df, values='cnt', index='season', columns='yr', aggfunc='sum')
season_per_year = season_per_year.reset_index()
melted_season_per_year = season_per_year.melt(id_vars='season', var_name='Year', value_name='Sum of Rental Bikes')

fig, ax = plt.subplots(figsize=(8, 6))
ax = sns.barplot(x='season', y='Sum of Rental Bikes', hue='Year', data=melted_season_per_year)
ax.bar_label(ax.containers[0], fontsize=10)
ax.bar_label(ax.containers[1], fontsize=10)
ax.set_xlabel("Season")
ax.set_ylabel("Summary")
ax.set_title("Rental Bikes per Season per Year")
ax.legend(title='Year')
st.pyplot(plt)
