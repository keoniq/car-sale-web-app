import streamlit as st
import pandas as pd

# Set app title and layout
st.set_page_config(page_title="Car Sale Web App", layout="wide")

# Main title
st.title("Car Sale Web App")
st.write("""
This app loads the 'vehicles_us.csv' dataset and provides a preview along with basic statistics.
Make sure the CSV file is in the same folder as this script.
""")

# Load the CSV file
try:
    df = pd.read_csv("vehicles_us.csv")
    st.success("Data loaded successfully from 'vehicles_us.csv'.")

    # Show raw data
    st.subheader("Preview of Data")
    st.dataframe(df)

    # Show basic info
    st.subheader("Dataset Info")
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")

    # Column names
    st.write("Columns in the dataset:")
    st.write(df.columns.tolist())

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe(include='all'))

    # Price Distribution Histogram
    st.subheader("Price Distribution")
    st.bar_chart(df['price'].value_counts().sort_index())

    # Odometer vs Price Scatter Plot
    st.subheader("Odometer vs Price")
    st.write("Note: Some points may overlap.")
    st.scatter_chart(df[['odometer', 'price']].dropna())

except FileNotFoundError:
    st.error("File 'vehicles_us.csv' not found. Please make sure it's in the same folder as this app.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Built by Keoni Quintana | Powered by Streamlit")
