import streamlit as st
import numpy as np
import pickle

# -------------------------------
# Load Model and Scaler
# -------------------------------
@st.cache_resource
def load_model():
    with open(r'C:\Users\IICET 16\Desktop\ruchali\machine learning project\iris project\log_reg_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open(r'C:\Users\IICET 16\Desktop\ruchali\machine learning project\iris project\scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

model, scaler = load_model()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🌼 Iris Flower Prediction App")
st.write("Enter the flower measurements below to predict the Iris species.")

# Input fields (numeric)
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width  = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width  = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

# Iris class names
class_labels = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}

# Predict button
if st.button("Predict"):
    # Convert to array
    sample = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Scale input
    sample_scaled = scaler.transform(sample)

    # Predict
    prediction = model.predict(sample_scaled)[0]
    probabilities = model.predict_proba(sample_scaled)[0]

    # Display results
    st.subheader("Prediction")
    st.write(f"**Predicted Species:** {class_labels[prediction]}")

    st.subheader("Probabilities")
    st.write(f"- Iris-setosa: {probabilities[0]:.4f}")
    st.write(f"- Iris-versicolor: {probabilities[1]:.4f}")
    st.write(f"- Iris-virginica: {probabilities[2]:.4f}")
