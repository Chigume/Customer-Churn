

# -*- coding: utf-8 -*-
"""
@author: Abgirl Chigume R195878B
"""

# -*- coding: utf-8 -*-
"""
@author: Abgirl Chigume R195878B
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(internetservice,monthlycharges,paperlessbilling,seniorcitizen):
    
    """Let's Authenticate the Churnings
    This is using docstrings for specifications.
    ---
    parameters:  
      - intenet service : variance
        in: query
        type: number
        required: true
      - paperlessbilling: skewness
        in: query
        type: number
        required: true
      - monthlycharges: curtosis
        in: query
        type: number
        required: true
      - senior citizen probability: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[internetservice,monthlycharges,paperlessbilling,seniorcitizen]])
    print(prediction)
    return prediction



def main():
    st.title("Customer Churn Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Customer Churn Predicting ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    internetservice = st.text_input("internetservice","Type Here")
    monthlycharge = st.text_input("monthlycharge","Type Here")
    paperlessbilling = st.text_input("paperlessbilling","Type Here")
    seniorcitizen = st.text_input("seniorcitizen","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(internetservice,monthlycharge,paperlessbilling,seniorcitizen)
    st.success('The probability for the customer to churn is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    





