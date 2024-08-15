# House-energy-saving-dummy-model

## Overview
The **House-energy-saving-dummy-model** is a simple, dummy model designed to simulate basic energy savings for individual houses based on renovation upgrades. It calculates break-even points, cumulative energy savings, and return on investment (ROI) for renovations like insulation, window improvements, and HVAC upgrades. 

This model is **only for testing purposes** and is not a full-fledged energy simulation tool. It focuses on **individual houses** rather than district-wide or large-scale energy analysis. 

## Features
- **Interactive Sliders**: Allows you to adjust house parameters like area, renovation cost, and savings from insulation, window, and HVAC upgrades.
- **Cumulative Savings Graph**: Visualizes cumulative energy savings over a 20-year period.
- **Break-even Point Calculation**: Identifies the year when the savings from energy efficiency measures exceed renovation costs.
- **Return on Investment (ROI)**: Shows the ROI for the renovation project.

## Usage
1. Adjust the sliders to simulate house area, renovation cost, and the expected savings from various upgrades.
2. View the graph, which shows:
   - **Cumulative savings** over time.
   - **Renovation costs** as a reference line.
   - The **break-even point** where savings equal the renovation cost.
3. Use the sliders to explore different scenarios and their financial implications.

## Technologies Used
- **Streamlit**: For the interactive web interface.
- **Matplotlib**: For plotting graphs and visualizing energy savings.
- **Pandas and NumPy**: For data manipulation and calculations.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/House-energy-saving-dummy-model.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Requirements
To run this project, ensure that your `requirements.txt` file includes:

