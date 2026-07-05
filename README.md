# 🩺 Obesity Status Prediction using Machine Learning

A Streamlit-based web application that predicts an individual's obesity status using machine learning techniques based on their demographic information, eating habits, lifestyle, and physical activity patterns. The application not only predicts obesity status but also provides personalized health recommendations to help users adopt healthier lifestyles.

---

## 📖 Overview

Obesity is one of the world's leading public health challenges, increasing the risk of chronic diseases such as diabetes, hypertension, cardiovascular diseases, and certain cancers. Early assessment of obesity status enables individuals to make informed lifestyle decisions and seek appropriate medical guidance.

This project leverages supervised machine learning algorithms to classify an individual's obesity status into one of four categories:

* 🟡 Underweight
* 🟢 Normal Weight
* 🟠 Overweight
* 🔴 Obese

Four machine learning models were developed and evaluated using standard classification metrics. After performance comparison, the **Random Forest Classifier** achieved the best results and was selected as the final model deployed in the Streamlit application.

---

## ✨ Features

* 🤖 Machine learning-based obesity status prediction
* 📊 Comparison of multiple classification algorithms
* ⚡ Real-time predictions through an interactive Streamlit interface
* 💡 Personalized health recommendations based on prediction results
* 🧹 Data preprocessing and feature engineering
* 📈 Model performance evaluation using standard classification metrics
* 🖥️ Simple and user-friendly interface

---

## 🧠 Machine Learning Models Evaluated

The following classification algorithms were trained and evaluated:

* ✅ Random Forest Classifier *(Selected Model)*
* Decision Tree Classifier
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)

---

## 📊 Model Evaluation Metrics

The models were evaluated using the following performance metrics:

* Accuracy
* Precision
* Recall
* F1-Score

The **Random Forest Classifier** produced the highest overall performance and was selected for deployment.

---

## 📋 Input Features

The application predicts obesity status using the following user information:

| Feature                                  | Possible Values                                                      |
| ---------------------------------------- | -------------------------------------------------------------------- |
| **Sex**                                  | Male, Female                                                         |
| **Age**                                  | Integer value (Years)                                                |
| **Height**                               | Numeric value (cm)                                                   |
| **Family History of Overweight/Obesity** | Yes, No                                                              |
| **Fast Food Consumption**                | Yes, No                                                              |
| **Frequency of Vegetable Consumption**   | Rarely, Sometimes, Always                                            |
| **Number of Main Meals Daily**           | 1–2 Meals, 3 Meals, More than 3 Meals                                |
| **Smoking Habit**                        | Yes, No                                                              |
| **Daily Liquid Intake**                  | Less than 1 Liter, 1–2 Liters, More than 2 Liters                    |
| **Calorie Intake Monitoring**            | Yes, No                                                              |
| **Physical Exercise Frequency**          | No Activity, 1–2 Days, 3–4 Days, 5–6 Days, More than 6 Days per Week |
| **Daily Technology Usage**               | 0–2 Hours, 3–5 Hours, More than 5 Hours                              |
| **Primary Mode of Transportation**       | Automobile, Motorbike, Bicycle, Public Transportation, Walking       |

---

## 🎯 Prediction Output

The application predicts one of the following obesity status categories:

* 🟡 Underweight
* 🟢 Normal Weight
* 🟠 Overweight
* 🔴 Obese

Predictions are generated instantly after the user submits the required information.

---

## 💡 Personalized Recommendations

After making a prediction, the application generates personalized health recommendations tailored to the predicted obesity class.

### 🟡 Underweight

* Increase intake of nutrient-rich foods.
* Eat balanced meals more frequently.
* Include healthy proteins, carbohydrates, and healthy fats.
* Consult a healthcare professional if necessary.

### 🟢 Normal Weight

* Maintain a balanced diet.
* Continue regular physical activity.
* Stay hydrated.
* Maintain healthy lifestyle habits.

### 🟠 Overweight

* Reduce fast-food and sugary drink consumption.
* Increase physical activity.
* Practice portion control.
* Monitor calorie intake regularly.

### 🔴 Obese

* Adopt a structured weight-management plan.
* Exercise regularly under professional guidance.
* Follow a balanced, calorie-controlled diet.
* Seek medical advice for long-term health management.

> **Disclaimer:** The recommendations provided are for educational purposes only and should not replace professional medical advice.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Joblib
* Jupyter Notebook

---

## 📂 Project Structure

```text
Obesity-Status-Prediction/
│
├── app.py                     # Streamlit application
├── model.pkl                  # Trained Random Forest model
├── requirements.txt           # Python dependencies
├── notebooks/                 # Model development notebooks
├── dataset/                   # Dataset 
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/sufyanzakariyya/Obesity-Status-ML-Web-App.git
```

### Navigate into the project directory

```bash
cd Obesity-Status-Prediction
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

The application will automatically open in your web browser.

---

## 📊 Dataset

The model was trained using an obesity dataset containing demographic information, dietary habits, lifestyle choices, and physical activity data. The dataset includes four target classes:

* Underweight
* Normal Weight
* Overweight
* Obese

---

## 🔮 Future Improvements

* Deploy the application on Streamlit Community Cloud or another cloud platform.
* Add Explainable AI (SHAP or LIME) to explain model predictions.
* Integrate Body Mass Index (BMI) visualization.
* Provide downloadable health reports.
* Support multilingual interfaces.
* Include additional health risk assessments and wellness tracking.

---

## 👨‍💻 Author

**Sufyan Zakariya Sani**

Machine Learning Engineer

---

## ⭐ Support

If you found this project helpful, please consider giving this repository a **star ⭐**. Your support is greatly appreciated!
