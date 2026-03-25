import streamlit as st

st.title("🏠 House Price Prediction App")

area = st.number_input("Enter area (sq ft)", min_value=100)
bedrooms = st.number_input("Enter number of bedrooms", min_value=1)

st.divider()

if st.button("Predict"):
    price = area * 1000 + bedrooms * 50000
    st.success(f"Predicted Price: ₹ {price:,.0f}")

st.caption("This is a demo ML model for house price prediction")
