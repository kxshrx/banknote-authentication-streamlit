import streamlit as st
import joblib

# Load the saved model
model = joblib.load('banknote_authentication_model.pkl')

# Streamlit application
st.title("Banknote Authentication")

st.write("### Predict Banknote Authentication")
variance = st.number_input("Variance")
skewness = st.number_input("Skewness")
curtosis = st.number_input("Curtosis")
entropy = st.number_input("Entropy")

if st.button("Predict"):
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    if prediction[0] == 0:
        st.success("The banknote is Genuine")
    else:
        st.error("The banknote is Counterfeit")
