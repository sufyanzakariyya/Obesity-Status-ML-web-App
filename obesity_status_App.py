import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Streamlit App Interface
st.write("""
# Obesity Status Prediction App

"A smart and intuitive app that analyzes social and physical activity patterns to predict and manage individual obesity risk, empowering users with actionable health insights and personalized recommendations."
""")
st.write('---')

df = pd.read_csv("ObesityDataset.csv") 
st.sidebar.header("User Input Features")

# Collect User Input Features Into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        sex = st.sidebar.selectbox("Sex: 1. Male. 2. Female", (1, 2)) 
        age = st.sidebar.slider("Age", int(df['Age'].min()), int(df['Age'].max()), int(df['Age'].mean()))
        height = st.sidebar.slider("Height", int(df['Height'].min()), int(df['Height'].max()), int(df['Height'].mean()))
        Overweight_Obese_Family = st.sidebar.selectbox("Overweight/Obese Families: [1] Yes. [2] No", (1, 2))
        Consumption_of_Fast_Food = st.sidebar.selectbox("Consumption of Fast Food: [1] Yes. [2] No", (1, 2))
        Frequency_of_Consuming_Vegetables = st.sidebar.selectbox("Frequency of Consuming Vegetables: [1] Rarely. [2] Sometimes. [3] Always", (1,2,3))
        Number_of_Main_Meals_Daily = st.sidebar.selectbox("Number of Main Meals Daily: [1] 1-2. [2] 3. [3] 3+", (1,2,3))
        Food_Intake_Between_Meals = st.sidebar.selectbox("Food Intake Between Meals: [1] Rarely. [2] Sometimes.[3] Usually. [4] Always", (1,2,3,4))
        Smoking = st.sidebar.selectbox("Smoking:  [1] Yes. [2] No", (1,2))
        Liquid_Intake_Daily = st.sidebar.selectbox("Liquid Intake Daily: [1] < 1 liter. [2] 1–2 liters. [3] > 2 liters", (1,2,3))
        Calculation_of_Calorie_Intake = st.sidebar.selectbox("Calculation Of Calorie Intake: [1] Yes. [2] No",(1,2))
        Physical_Excercise = st.sidebar.selectbox("Physical Exercise: [1] None. [2] 1–2 days. [3] 3–4 days. [4] 5–6 days. [5] 6+ days",(1,2,3,4,5))
        Schedule_Dedicated_to_Technology = st.sidebar.selectbox("Time Dedicated to technology: [1] 0–2 hrs. [2] 3–5 hrs. [3] >5 hrs",(1,2,3))
        Type_of_Transportation_Used = st.sidebar.selectbox("Transport Type: [1] Car. [2] Motorbike. [3] Bike. [4] Public Transport. [5] Walking", (1,2,3,4,5))
        
        data = {
            "Sex": sex,
            "Age": age,
            "Height": height,
            "Overweight_Obese_Family": Overweight_Obese_Family,
            "Consumption_of_Fast_Food": Consumption_of_Fast_Food,
            "Frequency_of_Consuming_Vegetables": Frequency_of_Consuming_Vegetables,
            "Number_of_Main_Meals_Daily": Number_of_Main_Meals_Daily,
            "Food_Intake_Between_Meals": Food_Intake_Between_Meals,
            "Smoking": Smoking,
            "Liquid_Intake_Daily": Liquid_Intake_Daily,
            "Calculation_of_Calorie_Intake": Calculation_of_Calorie_Intake,
            "Physical_Excercise": Physical_Excercise,
            "Schedule_Dedicated_to_Technology": Schedule_Dedicated_to_Technology,
            "Type_of_Transportation_Used": Type_of_Transportation_Used
        }
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

# Display User Input Features 
st.subheader("User Input features")
if uploaded_file is not None:
    st.write(input_df)
else:
    st.write("Awaiting CSV file to be uploaded.")
    st.write(input_df)

# Load the saved model
load_clf = pickle.load(open("classifier.pkl", "rb"))

# Only predict when the button is clicked
if st.button("Predict"):
    prediction = load_clf.predict(input_df)

    #st.subheader("Prediction")
    if prediction == 1:
        st.success(f"Predicted Obesity Category: {prediction[0]} - Underweight")
    elif prediction == 2:
        st.success(f"Predicted Obesity Category: {prediction[0]} - Normal")
    elif prediction == 3:
        st.success(f"Predicted Obesity Category: {prediction[0]} - Overweight")
    else:
        st.success(f"Predicted Obesity Category: {prediction[0]} - Obese")

    st.subheader("Recommendation")
    if prediction == 1:
        st.write("Eat nutrient-rich, high-calorie foods more frequently. Include healthy fats, proteins, and snacks.")
    elif prediction == 2:
        st.write("Maintain a balanced diet and active lifestyle to stay within the healthy weight range.")
    elif prediction == 3:
        st.write("Increase physical activity and make healthier food choices. Focus on fruits, vegetables, and whole grains.")
    else:
        st.write("Incorporate regular exercise and adopt a balanced, portion-controlled diet. Limit processed foods and sugary drinks.")
