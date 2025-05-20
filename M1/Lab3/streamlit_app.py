# Import Python libraries
import streamlit as st
import pandas as pd

st.title(f"🏔️ Avalanche Data Set")

df = pd.read_csv("data/customer_reviews.csv")

# Drop-down widget
unique_products = sorted(df.PRODUCT.unique())
selected_products = st.multiselect("Select product(s)", unique_products, unique_products)

st.write("Selected products:", list(selected_products))

st.dataframe(df[df.PRODUCT.isin(selected_products)])
# st.dataframe(df.head())

# Calendar widget
st.subheader("Dates")

df["DATE"] = pd.to_datetime(df["DATE"])

d = st.date_input(
    "Select dates",
    (df["DATE"].min().date(), df["DATE"].median().date() ),
    df["DATE"].min().date(),
    df["DATE"].max().date()
)
    
# Check if both dates are specified
if len(d)==2:
    start_date = pd.to_datetime(d[0])
    end_date = pd.to_datetime(d[1])
    
    st.write("Selected dates:", start_date, end_date)
    
    df_filtered = df[ (df["DATE"] >= start_date) & (df["DATE"] <= end_date)]
    df_filtered
