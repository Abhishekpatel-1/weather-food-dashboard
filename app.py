import pandas as pd
import streamlit as st
from pathlib import Path

# Load datasets using script-relative paths
base_dir = Path(__file__).resolve().parent
weather_path = base_dir / "data" / "weather_data.csv"
orders_path = base_dir / "data" / "food_orders.csv"

try:
	weather = pd.read_csv(weather_path, parse_dates=["date"]) 
	orders = pd.read_csv(orders_path, parse_dates=["date"]) 
except FileNotFoundError as e:
	st.error(f"Data file not found: {e}")
	raise

# Merge data
data = pd.merge(weather, orders, on="date")

st.title("🌦️ Weather vs Food Orders Dashboard")

st.write("### Combined Dataset")
st.dataframe(data)

st.write("### Temperature vs Food Orders")
st.line_chart(data[["temperature", "orders"]])

st.write("### Rainfall vs Food Orders")
st.bar_chart(data[["rainfall", "orders"]])

st.markdown("""
### 📊 Insight
Food orders tend to **increase on rainy and colder days**, indicating that weather
conditions strongly influence online food delivery demand.
""")
