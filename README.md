# Future Price Forecasting Application

This application is a powerful tool for predicting future values and trends using advanced time series forecasting techniques. It utilizes Facebook's Prophet library, which is particularly effective for forecasting time series data with strong seasonal effects and multiple seasonality periods.

## Features

- Interactive web interface using Streamlit
- Time series forecasting using Prophet
- Beautiful visualizations with Plotly and Matplotlib
- Support for various data formats
- Ability to handle seasonal patterns and trends
- Customizable forecast parameters

## Key Benefits

1. **Accurate Predictions**: Prophet automatically detects patterns in your data, including:
   - Yearly, monthly, and weekly seasonality
   - Holiday effects
   - Trend changes

2. **Business Applications**:
   - Sales forecasting
   - Inventory planning
   - Resource allocation
   - Budget planning
   - Market trend analysis

## Installation

1. Ensure you have Python 3.11 or later installed
2. Install required packages:
```bash
pip install streamlit pandas matplotlib plotly prophet
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Upload your time series data
3. Configure forecast parameters
4. View and analyze predictions

## Data Requirements

Your input data should include:
- A date/timestamp column
- A target value column (e.g., prices, sales, etc.)

## Technologies Used

- Python 3.11
- Streamlit for web interface
- Prophet for forecasting
- Pandas for data manipulation
- Plotly & Matplotlib for visualization

## License

This project is open source and available under the MIT License.
