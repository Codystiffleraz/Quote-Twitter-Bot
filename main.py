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

paste_data = clipboard.paste()
# Drop the quote from the csv

# Navigate to twitter
import pyautogui as pg
import time
    
chrome = 507, 1058
search_bar = -1267, 249
post_button = -1517, 966
post = -707, 569

pg.FAILSAFE = False

pg.moveTo(chrome)
time.sleep(1)
pg.click()

time.sleep(1)
pg.moveTo(search_bar)

time.sleep(1)
pg.click()

time.sleep(1)
pg.write('x.com', interval=0.1)

time.sleep(1)
pg.press("enter")

time.sleep(1)
pg.moveTo(post_button)

time.sleep(1)
pg.click()

time.sleep(1)
pg.typewrite(paste_data)

time.sleep(1)
pg.moveTo(post)

time.sleep(1)
pg.click()