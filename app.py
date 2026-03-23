import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🏠 House Price Prediction")

df = pd.read_csv("data.csv")

X = df[["area", "bedrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

area = st.number_input("Enter Area", value=1000)
bedrooms = st.number_input("Enter Bedrooms", value=2)

if st.button("Predict"):
    input_data = pd.DataFrame([[area, bedrooms]], columns=["area", "bedrooms"])
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:.2f} lakh")
    