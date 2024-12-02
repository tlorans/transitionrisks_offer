import pandas as pd
import streamlit as st
import numpy as np
import yfinance as yf

st.title("Understanding Transition Risks")

st.write("""We apply a simple free-cash flows model, embedding NGFS climate scenarios, to estimate the repricing effect caused by changes in investor expectations around transition scenarios. 
We do so to understand the relative importance of the source of transition risks. 
         """)

etfs = {
    "IWRD.L": "iShares MSCI World UCITS ETF",
    "SPY" : "SPDR S&P 500 ETF Trust",
        "EEM" : "iShares MSCI Emerging Markets ETF",
        "IWM" : "iShares Russell 2000 ETF"
}

list_tickers = list(etfs.values())

name_etf = st.sidebar.selectbox('Select ETF', list_tickers)

# find the corresponding key
ticker = [key for key, value in etfs.items() if value == name_etf][0]

list_models = ['GCAM 6.0 NGFS', 'MESSAGEix-GLOBIOM 1.1-M-R12', 'REMIND-MAgPIE 3.2-4.6']
name_model = st.sidebar.selectbox('Select Model', list_models)

list_scenarios = ['Delayed Transition', 'Net Zero 2050', 'Fragmented World', 'Below 2°C']
name_scenario = st.sidebar.selectbox('Select Scenario', list_scenarios)

import plotly.graph_objects as go

# Randomly generate loss data for demonstration
total_loss = np.random.uniform(10, 30)  # Total loss as a random number
loss_from_net_carbon_tax = total_loss * np.random.uniform(0.4, 0.7)  # Portion due to net carbon tax
loss_from_revenue = total_loss - loss_from_net_carbon_tax  # Remainder is revenue loss

# Create a DataFrame for display
data = {
    "Component": ["Net Carbon Tax Loss", "Revenue Loss", "Total Loss"],
    "Impact": [loss_from_net_carbon_tax, loss_from_revenue, total_loss],
}
df = pd.DataFrame(data)


# Display the data as a table
st.write("### Decomposition of Loss")

# Create a Plotly figure
fig = go.Figure()


# Add bars for each component
fig.add_trace(go.Bar(
    x=["Net Carbon Tax Loss", "Revenue Loss", "Total Loss"],
    y=[loss_from_net_carbon_tax, loss_from_revenue, total_loss],
    marker=dict(color=['#1f77b4', '#ff7f0e', '#2ca02c']),
    text=[f"{x:.2f}" for x in [loss_from_net_carbon_tax, loss_from_revenue, total_loss]],
    textposition='auto',
    name="Loss Components"
))

# Update layout
fig.update_layout(
    title="Portfolio Loss Impact by Component",
    xaxis_title="Component",
    yaxis_title="Loss Impact",
    template="plotly_white"
)

# Display the plot
st.plotly_chart(fig)