# IPL Score Prediction

## Overview
This project predicts the score of an IPL (Indian Premier League) match based on various match parameters using machine learning techniques.

## Features
- Predicts the score of a T20 match based on input parameters.
- Uses machine learning algorithms for accurate predictions.
- Interactive web application built using Streamlit.

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-Learn
- Streamlit
- Matplotlib, Seaborn

## Dataset
The dataset contains historical IPL match data, including:
- Batting Team
- Bowling Team
- Venue
- Current Score
- Wickets
- Overs Bowled
- Runs in Last 5 Overs

## Model Training
- Data Preprocessing: Cleaning and feature engineering.
- Model Used: Regression models like Linear Regression, Random Forest, or Gradient Boosting.
- Model Evaluation: Metrics like RMSE and R-squared are used to evaluate performance.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Simra-Kazi/Machine-Learning.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ipl-score-prediction
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage
- Open the web app in your browser.
- Select input parameters (teams, overs, wickets, etc.).
- Get the predicted score.

## Future Enhancements
- Improve prediction accuracy with deep learning models.
- Add real-time match updates.
- Deploy the model as an API.

## Contributors
Contributions are welcome! 

## License
This project is licensed under the MIT License.

