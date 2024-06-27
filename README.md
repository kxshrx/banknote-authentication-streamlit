
# Banknote Authentication Streamlit App

This is a simple Streamlit application for banknote authentication using a logistic regression model. The application takes user inputs for variance, skewness, curtosis, and entropy to predict whether a banknote is genuine or counterfeit.

## Table of Contents

- Overview

- Installation

- Usage

- Dataset

- Model

- Streamlit App

- Contributing

- License

## Overview

The project uses a logistic regression model to classify banknotes as genuine or counterfeit based on certain features. The model is trained on the UCI Banknote Authentication dataset and deployed as a Streamlit web application.

## Installation

To run this project locally, you need to have Python and the following packages installed:

- streamlit

- pandas

- scikit-learn

- joblib

- ucimlrepo

You can install the required packages using the command:

`pip install streamlit pandas scikit-learn joblib ucimlrepo`

## Usage

1\. Clone the repository:

   `git clone https://github.com/your-username/banknote-authentication-streamlit.git`

   `cd banknote-authentication-streamlit`

2\. Ensure you have the saved model file (`banknote_authentication_model.pkl`) in the project directory.

3\. Run the Streamlit application:

   `streamlit run app.py`

4\. Open your web browser and go to `http://localhost:8501` to interact with the app.

## Dataset

The dataset used in this project is the UCI Banknote Authentication Dataset. It contains features like variance, skewness, curtosis, and entropy of wavelet-transformed images of banknotes.

## Model

The model is a logistic regression classifier trained using the scikit-learn library. The training process includes splitting the data into training and testing sets, fitting the model, and saving it using joblib.

## Streamlit App

The Streamlit application allows users to input the features of a banknote and get a prediction on whether it is genuine or counterfeit. The app also provides some basic data visualization, such as a correlation heatmap and pairplot, to help understand the dataset better.
