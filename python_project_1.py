
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Acquisition
# Define the ticker symbol and the date range
ticker_symbol = "AAPL"  # Apple Inc.
start_date = "2018-01-01"
end_date = "2025-08-26" # Current date

print(f"Fetching historical data for {ticker_symbol} from {start_date} to {end_date}...")
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save the raw data to a CSV file
stock_data.to_csv(f"{ticker_symbol}_stock_data.csv")
print(f"Raw stock data saved to {ticker_symbol}_stock_data.csv")

# 2. Data Cleaning and Preprocessing
# Check for missing values
print("\nMissing values before cleaning:")
print(stock_data.isnull().sum())

# Drop rows with any missing values (if any, for simplicity in this example)
stock_data.dropna(inplace=True)
print("Missing values after cleaning:")
print(stock_data.isnull().sum())

# Ensure 'Date' is a datetime object (yfinance usually handles this, but good practice)
stock_data.index = pd.to_datetime(stock_data.index)

# 3. Descriptive Statistics
print("\nDescriptive Statistics for AAPL Stock Data:")
print(stock_data.describe())

# Calculate daily returns
stock_data["Daily Return"] = stock_data["Adj Close"].pct_change()
print("\nDescriptive Statistics for Daily Returns:")
print(stock_data["Daily Return"].describe())

# 4. Data Visualization
# Plotting the Adjusted Close Price over time
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data["Adj Close"], label="Adj Close Price")
plt.title(f"{ticker_symbol} Adjusted Close Price Over Time")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"{ticker_symbol}_close_price.png")
print(f"Adjusted Close Price plot saved to {ticker_symbol}_close_price.png")
plt.close()

# Histogram of Daily Returns
plt.figure(figsize=(10, 6))
sns.histplot(stock_data["Daily Return"].dropna(), bins=50, kde=True)
plt.title(f"{ticker_symbol} Daily Returns Distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{ticker_symbol}_daily_returns_hist.png")
print(f"Daily Returns Histogram saved to {ticker_symbol}_daily_returns_hist.png")
plt.close()

# Plotting Moving Averages
# Calculate 20-day and 50-day Simple Moving Averages (SMA)
stock_data["SMA_20"] = stock_data["Adj Close"].rolling(window=20).mean()
stock_data["SMA_50"] = stock_data["Adj Close"].rolling(window=50).mean()

plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data["Adj Close"], label="Adj Close Price", alpha=0.7)
plt.plot(stock_data.index, stock_data["SMA_20"], label="20-Day SMA", color="orange")
plt.plot(stock_data.index, stock_data["SMA_50"], label="50-Day SMA", color="green")
plt.title(f"{ticker_symbol} Adjusted Close Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(f"{ticker_symbol}_moving_averages.png")
print(f"Moving Averages plot saved to {ticker_symbol}_moving_averages.png")
plt.close()

print("\nPython Project 1 (EDA & Statistics) completed successfully.")


