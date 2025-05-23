import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('vehicles_us.csv')

# Clean the data
df = df.dropna(subset=['price', 'odometer'])
df = df[df['price'] > 0]
df = df[df['odometer'] > 0]

# Set page config
st.set_page_config(page_title="Car Sale Web App", layout="wide")

# App title
st.title("Car Sale Web App")
st.markdown("Explore used car listings and filter based on your preferences.")

# Sidebar filters
st.sidebar.header("Filter Listings")
selected_type = st.sidebar.multiselect("Select Type", options=df['type'].dropna().unique(), default=df['type'].dropna().unique())
selected_condition = st.sidebar.multiselect("Select Condition", options=df['condition'].dropna().unique(), default=df['condition'].dropna().unique())

# Filter the data
filtered_df = df[df['type'].isin(selected_type) & df['condition'].isin(selected_condition)]

# Show filtered data
st.subheader("Filtered Listings")
st.write(f"Showing {len(filtered_df)} vehicles")
st.dataframe(filtered_df[['model', 'price', 'odometer', 'type', 'condition']].sort_values(by='price'))

# Scatter plot
st.subheader("Odometer vs Price")
st.caption("Note: Some points may overlap. — Created by Keoni Quintana")
fig_scatter = px.scatter(filtered_df, x='odometer', y='price', hover_data=['model'], title='Odometer vs Price')
st.plotly_chart(fig_scatter, use_container_width=True)

# Histogram: Price Distribution
st.subheader("Price Distribution")
fig_price_hist = px.histogram(filtered_df, x='price', nbins=50, title='Distribution of Vehicle Prices')
st.plotly_chart(fig_price_hist, use_container_width=True)

# Histogram: Odometer Distribution
st.subheader("Odometer Distribution")
fig_odometer_hist = px.histogram(filtered_df, x='odometer', nbins=50, title='Distribution of Vehicle Odometer Readings')
st.plotly_chart(fig_odometer_hist, use_container_width=True)


