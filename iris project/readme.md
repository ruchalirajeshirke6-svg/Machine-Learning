Iris Flower Prediction App

A simple and interactive Machine Learning web application built using Streamlit, Logistic Regression, and Scikit-learn to classify Iris flower species based on user-entered measurements.

 **Project Overview**

This project uses a trained Logistic Regression model to predict the species of an Iris flower using four input features:

Sepal Length

Sepal Width

Petal Length

Petal Width

The app provides:

A clean Streamlit UI

Instant predictions

Probability scores for each species

📁 Project Structure
├── app.py                  # Streamlit application
├── log_reg_model.pkl       # Trained logistic regression model
├── scaler.pkl              # StandardScaler used during training
├── classification project1.ipynb   # Jupyter notebook (training & analysis)
└── README.md               # Documentation

🛠️ Installation & Setup

Follow the steps below to run the project on your system:

1️⃣ Clone the repository
git clone <your-repo-link>
cd iris-project

2️⃣ Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

3️⃣ Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt, here are the key packages:

pip install streamlit scikit-learn numpy pickle5

▶️ Running the App

Run the Streamlit server:

streamlit run app.py


The app should open automatically in your browser at:

http://localhost:8501

🧠 Model Details

Algorithm: Logistic Regression

Dataset: Iris dataset (from sklearn)

Preprocessing: StandardScaler

The model predicts one of three Iris species:

Iris-setosa

Iris-versicolor

Iris-virginica

📷 Application Screenshot (Optional)

Add a screenshot or GIF if you want to showcase the UI.

📝 Features

✔️ User-friendly Streamlit UI
✔️ Real-time predictions
✔️ Probability output for each class
✔️ Clean and modular code

📌 Future Improvements

Add model comparison (SVM, RandomForest, etc.)

Improve UI with images

Deploy on Streamlit 
