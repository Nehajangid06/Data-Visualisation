import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Resale flat prices.csv')
# Convert Approval Date to datetime format

df['Approval Date'] = pd.to_datetime(df['Approval Date'])

# Sort DataFrame by Approval Date

df = df.sort_values(by='Approval Date')

# Create a line plot

plt.figure(figsize=(10, 6))
plt.plot(df['Approval Date'], df['Resale Flat Price'], marker='o')
plt.title('Resale Flat Prices Based on Approval Date (2000 Feb - 2012 Feb)')
plt.xlabel('Approval Date')
plt.ylabel('Resale Flat Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

#Show the plot
plt.show()
