import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('src/athlete_events.csv')

# Print first few rows of the dataset
print(df.head())

# Example plot
plt.figure(figsize=(10, 6))
df['Age'].dropna().hist(bins=30)
plt.title('Age Distribution of Athletes')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
