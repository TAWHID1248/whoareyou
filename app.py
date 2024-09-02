import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('paypal.csv')

# Strip any leading/trailing whitespace from the phone number column
df['ship_email'] = df['ship_email'].astype(str).str.strip()

# Get user input for the phone number
user_input = input("Enter a phone number: ")

# Check if the phone number exists in the DataFrame
if df['ship_email'].str.contains(user_input).any():
    matching_rows = df[df['ship_email'].str.contains(user_input)]
    print("Match found! Here is the information:")
    print(matching_rows)
else:
    print("No match found.")
