import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from prophet import Prophet
from datetime import datetime
import plotly.express as px

# Set page config
st.set_page_config(page_title="Future Price Forecaster", layout="wide")

# Title and description
st.title("Future Price Forecaster")
st.write("Upload your time series data and predict future values!")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    
    # Show raw data
    st.subheader("Raw Data Preview")
    st.write(df.head())
    
    # Column selection
    st.subheader("Select Columns")
    date_column = st.selectbox("Select Date Column", df.columns)
    value_column = st.selectbox("Select Value Column", df.columns)
    
    if st.button("Generate Forecast"):
        # Prepare data for Prophet
        df_prophet = df[[date_column, value_column]].copy()
        df_prophet.columns = ['ds', 'y']
        
        # Create and fit Prophet model
        model = Prophet(yearly_seasonality=True, 
                       weekly_seasonality=True,
                       daily_seasonality=False,
                       changepoint_prior_scale=0.05)
        model.fit(df_prophet)
        
        # Create future dates for forecasting
        future_periods = st.slider("Select number of future periods to forecast", 
                                 min_value=1, max_value=365, value=90)
        future = model.make_future_dataframe(periods=future_periods)
        
        # Make predictions
        forecast = model.predict(future)
        
        # Plot the forecast
        st.subheader("Forecast Results")
        
        # Create interactive plot with Plotly
        fig = go.Figure()
        
        # Add actual values
        fig.add_trace(go.Scatter(x=df_prophet['ds'], 
                                y=df_prophet['y'],
                                name='Actual',
                                mode='markers+lines'))
        
        # Add predicted values
        fig.add_trace(go.Scatter(x=forecast['ds'],
                                y=forecast['yhat'],
                                name='Predicted',
                                mode='lines'))
        
        # Add uncertainty intervals
        fig.add_trace(go.Scatter(x=forecast['ds'],
                                y=forecast['yhat_upper'],
                                fill=None,
                                mode='lines',
                                line_color='rgba(0,100,255,0.2)',
                                name='Upper Bound'))
        
        fig.add_trace(go.Scatter(x=forecast['ds'],
                                y=forecast['yhat_lower'],
                                fill='tonexty',
                                mode='lines',
                                line_color='rgba(0,100,255,0.2)',
                                name='Lower Bound'))
        
        # Update layout
        fig.update_layout(title='Time Series Forecast',
                         xaxis_title='Date',
                         yaxis_title='Value',
                         hovermode='x unified')
        
        # Show plot
        st.plotly_chart(fig, use_container_width=True)
        
        # Show forecast components
        st.subheader("Forecast Components")
        fig_comp = model.plot_components(forecast)
        st.pyplot(fig_comp)
        
        # Show forecast data
        st.subheader("Forecast Data")
        st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(future_periods))
        
        # Download forecast data
        csv = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(index=False)
        st.download_button(
            label="Download Forecast Data",
            data=csv,
            file_name="forecast_results.csv",
            mime="text/csv"
        )
else:
    st.info("Please upload a CSV file to begin forecasting.")
    
    # Example data format
    st.subheader("Expected Data Format:")
    example_data = pd.DataFrame({
        'date': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'value': [100, 102, 101]
    })
    st.write(example_data)
