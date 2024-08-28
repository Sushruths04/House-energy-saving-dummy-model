import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Advanced Energy Savings Estimator")

# Input: House characteristics
area_of_house = st.number_input('House area (m²)', min_value=50, max_value=500, step=10)
house_age = st.number_input('Age of the house (years)', min_value=1, max_value=100, step=1)
base_energy_consumption = st.number_input('Baseline energy consumption (kWh/year)', min_value=1000, max_value=50000, step=100)

# Input: Insulation
insulation_quality = st.selectbox('Insulation quality', ['Poor', 'Average', 'Good', 'Excellent'])
insulation_cost = st.slider('Insulation cost ($)', 500, 20000, step=500)
insulation_efficiency = {'Poor': 0.1, 'Average': 0.25, 'Good': 0.4, 'Excellent': 0.6}[insulation_quality]

# Input: Windows
window_type = st.selectbox('Window type', ['Single Pane', 'Double Pane', 'Triple Pane'])
window_cost = st.slider('Window cost ($)', 1000, 30000, step=1000)
window_efficiency = {'Single Pane': 0.1, 'Double Pane': 0.3, 'Triple Pane': 0.5}[window_type]

# Input: HVAC
hvac_efficiency = st.slider('HVAC efficiency (%)', 70, 100, step=1)
hvac_cost = st.slider('HVAC upgrade cost ($)', 1000, 20000, step=1000)

# Input: External factors
average_temperature = st.slider('Average external temperature (°C)', -10, 40, step=1)
energy_price = st.slider('Current energy price ($/kWh)', 0.05, 0.50, step=0.01)

# Advanced calculations
# Estimating dynamic energy savings
insulation_savings = base_energy_consumption * insulation_efficiency * (20 - average_temperature) / 20
window_savings = base_energy_consumption * window_efficiency * (20 - average_temperature) / 20
hvac_savings = base_energy_consumption * (1 - hvac_efficiency/100) * (average_temperature / 30)

total_savings = insulation_savings + window_savings + hvac_savings

# Calculating costs
total_cost = insulation_cost + window_cost + hvac_cost

# ROI and Break-even calculations
roi = (total_savings * energy_price) / total_cost
years_to_breakeven = total_cost / (total_savings * energy_price)

# Display the results
st.write(f"Total annual energy savings: {total_savings:.2f} kWh/year")
st.write(f"Total renovation cost: ${total_cost}")
st.write(f"Estimated ROI: {roi:.2f}")
st.write(f"Years to break even: {years_to_breakeven:.2f}")

# Scenario analysis for future energy prices
future_years = np.arange(1, 21)
future_energy_prices = energy_price * (1 + 0.03) ** future_years  # assuming a 3% annual increase in energy price
future_savings = total_savings * future_energy_prices
cumulative_savings = np.cumsum(future_savings)

# Plot the cumulative savings
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(future_years, cumulative_savings, label='Cumulative Savings')
ax.axhline(y=total_cost, color='red', linestyle='--', label='Total Renovation Cost')
ax.axvline(x=years_to_breakeven, color='blue', linestyle='--', label=f'Break-even Point ({years_to_breakeven:.2f} years)')
ax.set_xlabel("Years")
ax.set_ylabel("Cumulative Savings ($)")
ax.set_title("Cumulative Savings vs. Renovation Cost")
ax.legend()
st.pyplot(fig)

# Scenario comparison
best_case_savings = total_savings * 1.2  # 20% better performance
worst_case_savings = total_savings * 0.8  # 20% worse performance

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(future_years, np.cumsum(best_case_savings * future_energy_prices), label='Best Case')
ax.plot(future_years, np.cumsum(worst_case_savings * future_energy_prices), label='Worst Case')
ax.axhline(y=total_cost, color='red', linestyle='--', label='Total Renovation Cost')
ax.set_xlabel("Years")
ax.set_ylabel("Cumulative Savings ($)")
ax.set_title("Scenario Comparison: Cumulative Savings")
ax.legend()
st.pyplot(fig)
