import streamlit as st

st.title("🏠 House Price Prediction App")

area = st.number_input("Enter area (sq ft)")
bedrooms = st.number_input("Enter number of bedrooms")

if st.button("Predict"):
    price = area * 1000 + bedrooms * 50000
    st.success(f"Predicted Price: ₹ {price:,.0f}")
