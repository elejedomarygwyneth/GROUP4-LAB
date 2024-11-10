import pandas as pd
import matplotlib.pyplot as plt

#data from CSV file
file_path = 'breadprice.csv'  
data = pd.read_csv(file_path)

#Average price for each year
data['AveragePrice'] = data.mean(axis=1)

#'Year' and 'AveragePrice' columns
data = data[['Year', 'AveragePrice']]

# Sorting of data
data = data.sort_values(by='Year')

# Plotting of data
plt.figure(figsize=(10, 5))
plt.plot(data['Year'], data['AveragePrice'], marker='o')
plt.title('Average Price of Bread Over Years')
plt.xlabel('Year')
plt.ylabel('Average Price (USD)')
plt.grid(True)
plt.show()
