import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load('churn_model.pkl')

# Assume label encoder was also saved (similar process as saving model)
# For simplicity, let's assume we use the same encoder as in the Kaggle notebook
encoder = LabelEncoder()

# Define a function for user input
def user_input_features():
    gender = st.selectbox('Gender', ('Male', 'Female'))
    senior_citizen = st.selectbox('Senior Citizen', (0, 1))
    partner = st.selectbox('Partner', ('Yes', 'No'))
    dependents = st.selectbox('Dependents', ('Yes', 'No'))
    tenure = st.slider('Tenure (months)', 0, 72, 1)
    phone_service = st.selectbox('Phone Service', ('Yes', 'No'))
    multiple_lines = st.selectbox('Multiple Lines', ('Yes', 'No', 'No phone service'))
    internet_service = st.selectbox('Internet Service', ('DSL', 'Fiber optic', 'No'))
    online_security = st.selectbox('Online Security', ('Yes', 'No', 'No internet service'))
    online_backup = st.selectbox('Online Backup', ('Yes', 'No', 'No internet service'))
    device_protection = st.selectbox('Device Protection', ('Yes', 'No', 'No internet service'))
    tech_support = st.selectbox('Tech Support', ('Yes', 'No', 'No internet service'))
    streaming_tv = st.selectbox('Streaming TV', ('Yes', 'No', 'No internet service'))
    streaming_movies = st.selectbox('Streaming Movies', ('Yes', 'No', 'No internet service'))
    contract = st.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
    paperless_billing = st.selectbox('Paperless Billing', ('Yes', 'No'))
    payment_method = st.selectbox('Payment Method', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
    monthly_charges = st.number_input('Monthly Charges', 18.25, 118.75)
    total_charges = st.number_input('Total Charges', 18.25, 8684.80)

    data = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Title of the Streamlit app
st.title('Telco Customer Churn Prediction')

# Get user input
input_df = user_input_features()

# Preprocess user input
for column in input_df.columns:
    if input_df[column].dtype == 'object':
        input_df[column] = encoder.fit_transform(input_df[column])

# Predict churn
prediction = model.predict(input_df)

# Display the prediction
st.subheader('Prediction')
st.write('Churn' if prediction[0] == 1 else 'No Churn')
