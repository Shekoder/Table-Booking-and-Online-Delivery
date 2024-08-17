import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv'
df = pd.read_csv(r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\dataset.csv')


# Convert boolean-like columns to actual boolean values
df['Has Table booking'] = df['Has Table booking'] == 'Yes'
df['Has Online delivery'] = df['Has Online delivery'] == 'Yes'

# 1. Determine the Percentage of Restaurants Offering Table Booking and Online Delivery

# Calculate the percentage of restaurants that offer table booking
table_booking_percentage = (df['Has Table booking'].value_counts(normalize=True) * 100).get(True, 0)

# Calculate the percentage of restaurants that offer online delivery
online_delivery_percentage = (df['Has Online delivery'].value_counts(normalize=True) * 100).get(True, 0)

print(f"Percentage of restaurants offering table booking: {table_booking_percentage:.2f}%")
print(f"Percentage of restaurants offering online delivery: {online_delivery_percentage:.2f}%")

# 2. Compare Average Ratings Based on Table Booking Availability

# Calculate the average ratings for restaurants with and without table booking
average_rating_table_booking = df[df['Has Table booking'] == True]['Aggregate rating'].mean()
average_rating_no_table_booking = df[df['Has Table booking'] == False]['Aggregate rating'].mean()

print(f"Average rating for restaurants with table booking: {average_rating_table_booking:.2f}")
print(f"Average rating for restaurants without table booking: {average_rating_no_table_booking:.2f}")

# 3. Analyze Online Delivery Availability Among Restaurants with Different Price Ranges

# Analyze the availability of online delivery among restaurants with different price ranges
online_delivery_by_price_range = df.groupby('Price range')['Has Online delivery'].mean() * 100

print("Percentage of restaurants offering online delivery by price range:")
print(online_delivery_by_price_range)

# Visualize the analysis
plt.figure(figsize=(12, 8))
sns.barplot(x=online_delivery_by_price_range.index, y=online_delivery_by_price_range)
plt.title('Percentage of Restaurants Offering Online Delivery by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Percentage of Restaurants Offering Online Delivery')
plt.xticks(rotation=0)
plt.show()
