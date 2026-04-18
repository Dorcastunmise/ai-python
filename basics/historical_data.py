import requests, os, pandas as pd, matplotlib.pyplot as plt
from datetime import datetime, timedelta


"""
timedelta is used to calculate the date one week ago from today.
It allows us to easily manipulate dates by adding or subtracting a specified amount of time. 
In this case, we subtract 7 days from today's date to get the date for one week ago.

matplotlib is a popular plotting library in Python that provides a wide range of functions for creating static, animated, and interactive visualizations.
"""
# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Lagos weather for past week
latitude = 6.6137
longitude = 3.3792
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

"""
Pandas
Pandas is a powerful data manipulation library in Python that provides data structures and functions for working with structured data. It allows you to easily handle and analyze data in tabular form, making it ideal for tasks like data cleaning, transformation, and analysis. In this code, we use Pandas to create a DataFrame from the daily weather data, which allows us to organize and manipulate the data efficiently.
"""

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Lagos Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

# Creating data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/lagos_weather.csv', index=False)
print("Data saved to data/lagos_weather.csv")