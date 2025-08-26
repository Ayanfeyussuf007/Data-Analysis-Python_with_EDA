# Python Project 1: Exploratory Data Analysis (EDA) and Statistics on Financial Data

## Project Overview
This project demonstrates fundamental data analysis techniques using Python, focusing on Exploratory Data Analysis (EDA) and basic statistical computations on financial time-series data. The goal is to extract insights from historical stock data, visualize trends, and understand key statistical properties.

## Dataset
The dataset used is historical stock data for Apple (AAPL), obtained using the `yfinance` library. It includes daily open, high, low, close prices, adjusted close prices, and volume.

## Key Features Demonstrated
-   **Data Acquisition:** Fetching real-time or historical financial data.
-   **Data Cleaning and Preparation:** Handling missing values and ensuring data quality.
-   **Descriptive Statistics:** Calculating mean, median, standard deviation, etc.
-   **Time Series Analysis:** Analyzing trends, seasonality, and daily returns.
-   **Moving Averages:** Calculating and visualizing simple moving averages (SMA) for trend identification.
-   **Data Visualization:** Creating informative plots using Matplotlib and Seaborn to represent financial data and statistical distributions.

## Files in this Project
-   `python_project_1.py`: The main Python script containing the EDA and statistical analysis code.
-   `AAPL_stock_data.csv`: The raw historical stock data downloaded.
-   `AAPL_close_price.png`: Line plot of Apple's closing price over time.
-   `AAPL_daily_returns_hist.png`: Histogram showing the distribution of daily returns.
-   `AAPL_moving_averages.png`: Line plot of closing price with 20-day and 50-day moving averages.

## How to Run the Project
1.  **Prerequisites:** Ensure you have Python installed. You will also need the following libraries:
    -   `pandas`
    -   `numpy`
    -   `matplotlib`
    -   `seaborn`
    -   `yfinance`
    You can install them using pip:
    ```bash
    pip install pandas numpy matplotlib seaborn yfinance
    ```
2.  **Clone the Repository:** If you haven't already, clone this repository to your local machine.
3.  **Execute the Script:** Navigate to the `python_project_1` directory in your terminal and run the Python script:
    ```bash
    python python_project_1.py
    ```
    This will generate the CSV data file and the PNG plots in the same directory.

## Analysis Highlights
-   The project demonstrates how to calculate daily returns and analyze their distribution, which is crucial for understanding stock volatility.
-   Moving averages are used as a simple technical analysis tool to identify potential trends and support/resistance levels.
-   Visualizations provide a clear overview of stock performance and statistical characteristics.

## Future Enhancements
-   Implement more advanced statistical tests (e.g., hypothesis testing for returns).
-   Explore different types of moving averages or other technical indicators.
-   Integrate interactive visualizations using libraries like Plotly.
-   Expand to analyze multiple stocks and compare their performance.


