import random
import csv
# Copy Quote to clipboard
import clipboard
import pandas as pd

df = pd.read_csv("quotes.csv")
random_row_number = random.choice(df["Number"])
random_row = df[df["Number"] == random_row_number]
random_quote = df["Quote with Author"][random_row_number]

clipboard.copy(random_quote)
# Drop the quote from the csv

# Navigate to twitter
# Click post button
# Post Quote
# Close tab