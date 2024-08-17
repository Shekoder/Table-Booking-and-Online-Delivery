import pandas as pd

# Load the dataset
file_path = r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv'
df = pd.read_csv(r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv')


# Extract additional features
df['Restaurant Name Length'] = df['Restaurant Name'].apply(len)
df['Address Length'] = df['Address'].apply(len)

# Display the new features
print('First few rows with new features:')
print(df[['Restaurant Name', 'Restaurant Name Length', 'Address', 'Address Length']].head())

# Create new features by encoding categorical variables
df['Has Table Booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online Delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)

# Display the new encoded features
print('\nFirst few rows with encoded features:')
print(df[['Has Table booking', 'Has Table Booking', 'Has Online delivery', 'Has Online Delivery']].head())


