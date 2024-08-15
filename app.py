# import pandas as pd
# import numpy as np
# import streamlit as st
# import matplotlib.pyplot as plt

# # Function to calculate energy savings and break-even point
# def calculate_savings(area_of_house, renovation_cost, insulation_savings, window_savings, hvac_savings, energy_price_increase):
#     # Calculate total annual energy savings
#     annual_energy_savings = (insulation_savings + window_savings + hvac_savings) * (area_of_house / 100)
    
#     # Factor in energy price increase for future savings
#     future_savings = annual_energy_savings * (1 + (energy_price_increase / 100))
    
#     # Calculate break-even point in years
#     break_even_years = renovation_cost / annual_energy_savings
    
#     return annual_energy_savings, future_savings, break_even_years

# # Streamlit Sliders for Parameters
# st.title("Building Energy Savings Model")
# area_of_house = st.slider("Area of the House (m²)", 50, 500, 100)
# renovation_cost = st.slider("Renovation Cost ($)", 1000, 20000, 6000)
# insulation_savings = st.slider("Insulation Savings ($/year)", 0, 1000, 200)
# window_savings = st.slider("Window Savings ($/year)", 0, 1000, 250)
# hvac_savings = st.slider("HVAC Savings ($/year)", 0, 1000, 300)
# energy_price_increase = st.slider("Energy Price Increase (%/year)", 0, 10, 2)

# # Calculate and Display Results
# annual_energy_savings, future_savings, break_even_years = calculate_savings(area_of_house, renovation_cost, insulation_savings, window_savings, hvac_savings, energy_price_increase)
# st.write(f"Annual Energy Savings: ${annual_energy_savings:.2f}")
# st.write(f"Future Energy Savings with Price Increase: ${future_savings:.2f}")
# st.write(f"Break-even Point: {break_even_years:.2f} years")

# # Plot cumulative savings over time and show break-even point
# years = np.arange(1, 21)  # Calculate savings over 20 years
# cumulative_savings = [annual_energy_savings * (1 + energy_price_increase/100)**year for year in years]

# fig, ax = plt.subplots()
# ax.plot(years, np.cumsum(cumulative_savings), label="Cumulative Savings", marker='o', color="green")
# ax.axhline(y=renovation_cost, color='red', linestyle='--', label='Renovation Cost')
# ax.axvline(x=break_even_years, color='blue', linestyle='--', label=f'Break-even Point ({break_even_years:.2f} years)')
# ax.set_xlabel("Years")
# ax.set_ylabel("Cumulative Savings ($)")
# ax.set_title(f"Cumulative Savings vs Renovation Cost (Area = {area_of_house} m²)")
# ax.legend()

# st.pyplot(fig)
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Function to calculate energy savings and break-even point
def calculate_savings(area_of_house, renovation_cost, insulation_savings, window_savings, hvac_savings, energy_price_increase):
    # Calculate total annual energy savings
    annual_energy_savings = (insulation_savings + window_savings + hvac_savings) * (area_of_house / 100)
    
    # Factor in energy price increase for future savings
    future_savings = annual_energy_savings * (1 + (energy_price_increase / 100))
    
    # Calculate break-even point in years
    break_even_years = renovation_cost / annual_energy_savings
    
    return annual_energy_savings, future_savings, break_even_years

# Streamlit Sliders for Parameters
st.title("Building Energy Savings Model")
area_of_house = st.slider("Area of the House (m²)", 50, 3000, 100)
renovation_cost = st.slider("Renovation Cost ($)", 1000, 100000, 6000)
insulation_savings = st.slider("Insulation Savings ($/year)", 0, 1000, 200)
window_savings = st.slider("Window Savings ($/year)", 0, 1000, 250)
hvac_savings = st.slider("HVAC Savings ($/year)", 0, 1000, 300)
energy_price_increase = st.slider("Energy Price Increase (%/year)", 0, 10, 2)

# Calculate and Display Results
annual_energy_savings, future_savings, break_even_years = calculate_savings(area_of_house, renovation_cost, insulation_savings, window_savings, hvac_savings, energy_price_increase)
st.write(f"Annual Energy Savings: ${annual_energy_savings:.2f}")
st.write(f"Future Energy Savings with Price Increase: ${future_savings:.2f}")
st.write(f"Break-even Point: {break_even_years:.2f} years")

# Calculate cumulative savings over time (for 20 years)
years = np.arange(1, 21)
cumulative_savings = np.cumsum([annual_energy_savings * (1 + energy_price_increase/100)**year for year in years])

# Enhanced Visualization with Shading and Annotations
fig, ax = plt.subplots(figsize=(10, 6))

# Plot cumulative savings with a smoother line and markers
ax.plot(years, cumulative_savings, label="Cumulative Savings", marker='o', color="green", linewidth=2, linestyle="-")

# Horizontal line for renovation cost
ax.axhline(y=renovation_cost, color='red', linestyle='--', label='Renovation Cost')

# Vertical line for break-even point
ax.axvline(x=break_even_years, color='blue', linestyle='--', label=f'Break-even Point ({break_even_years:.2f} years)')

# Shading before and after break-even point
ax.fill_between(years, cumulative_savings, renovation_cost, where=(years < break_even_years), color='lightcoral', alpha=0.3, label="Pre Break-even")
ax.fill_between(years, cumulative_savings, renovation_cost, where=(years >= break_even_years), color='lightgreen', alpha=0.3, label="Post Break-even")

# Add annotations for key points
ax.annotate(f'Break-even: {break_even_years:.2f} years', xy=(break_even_years, renovation_cost), xytext=(break_even_years + 1, renovation_cost + 1000),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Label axes and title
ax.set_xlabel("Years")
ax.set_ylabel("Cumulative Savings ($)")
ax.set_title(f"Cumulative Savings vs Renovation Cost (Area = {area_of_house} m²)")

# Show the legend
ax.legend()

# Show the improved graph
st.pyplot(fig)
