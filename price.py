import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv'
df = pd.read_csv(r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv')


# Determine the most common price range
most_common_price_range = df['Price range'].mode()[0]
print(f'The most common price range is: {most_common_price_range}')

# Calculate the average rating for each price range
avg_rating_per_price_range = df.groupby('Price range')['Aggregate rating'].mean()
print('\nAverage rating for each price range:')
print(avg_rating_per_price_range)

# Identify the color that represents the highest average rating among different price ranges
highest_avg_rating = avg_rating_per_price_range.idxmax()
color_for_highest_avg_rating = df[df['Price range'] == highest_avg_rating]['Rating color'].mode()[0]
print(f'\nThe color that represents the highest average rating ({highest_avg_rating}) is: {color_for_highest_avg_rating}')

# Plotting the average rating per price range
plt.figure(figsize=(10, 6))
colors = ['skyblue' if price_range != highest_avg_rating else color_for_highest_avg_rating 
          for price_range in avg_rating_per_price_range.index]
avg_rating_per_price_range.plot(kind='bar', color=colors)
plt.title('Average Rating for Each Price Range')
plt.xlabel('Price Range')
plt.ylabel('Average Rating')
plt.xticks(rotation=0)
plt.show()
