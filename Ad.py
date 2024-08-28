import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00374/energydata_complete.csv"
df = pd.read_csv(url)

# Feature selection (including only relevant features)
features = ['T1', 'RH_1', 'T2', 'RH_2', 'T3', 'RH_3', 'T_out', 'RH_out', 'Windspeed', 'Visibility', 'Tdewpoint']
X = df[features]  # The features to train on
y = df['Appliances']  # The target variable (energy consumption of appliances)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Streamlit Title
st.title("House Energy Consumption Prediction")

# Sidebar for Input Features
st.sidebar.header('Input Features')

house_size = st.sidebar.slider('House Size (in square meters)', min_value=50, max_value=300, value=150, step=10)
renovation_cost = st.sidebar.slider('Renovation Cost (in $)', min_value=10000, max_value=100000, value=50000, step=5000)
previous_energy_usage = st.sidebar.slider('Previous Energy Usage (kWh/year)', min_value=1000, max_value=10000, value=5000, step=500)
age_of_house = st.sidebar.slider('Age of the House (years)', min_value=1, max_value=50, value=20, step=1)
number_of_rooms = st.sidebar.slider('Number of Rooms', min_value=1, max_value=10, value=4, step=1)
location_score = st.sidebar.slider('Location Score', min_value=1.0, max_value=10.0, value=5.0, step=0.1)
energy_price = st.sidebar.slider('Energy Price ($/kWh)', min_value=0.05, max_value=0.50, value=0.12, step=0.01)

# Button to Toggle Predictions
if st.button('Predict'):
    # Input data for prediction
    new_data = pd.DataFrame({
        'T1': [house_size],
        'RH_1': [renovation_cost],
        'T2': [previous_energy_usage],
        'RH_2': [age_of_house],
        'T3': [number_of_rooms],
        'RH_3': [location_score],
        'T_out': [20],  # Default values
        'RH_out': [50],
        'Windspeed': [10],
        'Visibility': [40],
        'Tdewpoint': [10]
    })

    # Make a prediction based on the user input
    predicted_energy_savings = model.predict(new_data)

    # Calculating energy savings in monetary terms
    energy_cost_savings = predicted_energy_savings[0] * energy_price

    # Display the results
    st.write(f"### Predicted Energy Consumption: {predicted_energy_savings[0]:.2f} kWh/year")
    st.write(f"### Energy Cost Savings: ${energy_cost_savings:.2f} per year")

    # Model Evaluation on Test Set
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write(f"#### Model Mean Squared Error on Test Set: {mse:.2f}")
    st.write(f"#### Model R-squared Score on Test Set: {r2:.2f}")

    # Plot True vs Predicted Energy Consumption
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(y_test, y_pred, alpha=0.5, label='Predicted vs True')
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', lw=2, label='Perfect Fit Line')
    ax.set_xlabel("True Energy Consumption (kWh/year)")
    ax.set_ylabel("Predicted Energy Consumption (kWh/year)")
    ax.set_title("True vs Predicted Energy Consumption")
    ax.legend()
    st.pyplot(fig)

    # Feature Importance (Optional)
    feature_importances = pd.Series(model.feature_importances_, index=X.columns)
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    feature_importances.sort_values().plot(kind='barh', ax=ax2, color='skyblue')
    ax2.set_title("Feature Importance in Energy Consumption Prediction")
    st.pyplot(fig2)

else:
    st.write("Click the 'Predict' button to get results.")
