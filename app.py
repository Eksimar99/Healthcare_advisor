# import langchain
import streamlit as st
# from python_dotenv import os
import os 
import google.generativeai as genai
from dotenv import load_dotenv 
load_dotenv() # this will load the local enviornment vars
import pandas as pd

# Set up Gemini api_key in vscode
genai.configure(api_key = os.getenv('GOOGLE-API-KEY'))


#Streamlit Page
st.header("👨‍⚕️Healthcare :blue[Advisor]⚕️", divider='green')
input = st.text_input("Hi! I am your Medical Expert📋. Ask me anything...")
submit = st.button('Submit')

# Ceate a BMI Calculator
st.sidebar.subheader('BMI Calculator🎚️')
weight = st.sidebar.text_input("Weight (in kgs):")  # will capture info in text
height = st.sidebar.text_input("Height (in cms):")

#BMI = weight/height**2
height_num = pd.to_numeric(height)
weight_num = pd.to_numeric(weight)
height_mts = height_num/100
bmi = round(weight_num/(height_mts)**2, 2)
st.sidebar.markdown(bmi)

# BMI scale
notes = f'''The BMI Value can be interpreted as:
* Underweight: BMI < 18.5
* Normal Weight: BMI 18.5 - 24.9
* Overweight: BMI 25-29
* Obese: BMI >= 30'''

if bmi:
    st.sidebar.markdown("The BMI is:")
    st.sidebar.write(bmi)
    st.sidebar.write(notes)


# Setup Generative AI into application 
def get_response(text):
    model =  genai.GenerativeModel("gemini-pro")
    if text !='':
        response = model.generate_content(text)
        return (response.text)
    else:
        response = st.write("Please enter the Prompt!")
    

if submit:
    response = get_response(input)
    st.subheader("The :orange[Response] is: ")
    st.write(response)

# Disclaimer
st.subheader("Disclaimer", divider=True)
notes = f'''
1. This is an advisor providing guidance and should not be constructed as Medical Advisor.
2. Before taking any action, it is be recommended to consult a Doctor.'''
st.markdown(notes)