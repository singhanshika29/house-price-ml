import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# ui for mlflow user can give input and see the output
# create a calculator which do addition, subtraction,
#  multiplication and division
st.title("Simple Calculator App")
st.write("Welcome to the calculator app")
#input fields for the two numbers
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
#prepare the the caclulation
sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "Division by zero is not allowed"

#display the results
st.write("The sum of the two numbers is: ", sum_result)
st.write("The difference of the two numbers is: ", sub_result)  
st.write("The product of the two numbers is: ", mul_result)
st.write("The quotient of the two numbers is: ", div_result)


