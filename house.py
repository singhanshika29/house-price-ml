import streamlit as st
import pandas as pd

st.title("House Price Prediction")

# Example inputs
area = st.number_input("Enter area (sq ft)")
bedrooms = st.number_input("Enter number of bedrooms")

# Dummy logic (replace with your ML model)
if st.button("Predict"):
    price = area * 1000 + bedrooms * 50000
    st.success(f"Predicted Price: ₹ {price}")
    