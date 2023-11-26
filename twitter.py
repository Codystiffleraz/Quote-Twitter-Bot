import pyautogui as pg
import time
import decimal
import random
# from main import paste_data


def twitter_brain():
    chrome = 507, 1058
    search_bar = -1267, 249
    post_button = -1517, 966
    post = -707, 569
    close_window = -25, 220

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

    time.sleep(int(decimal.Decimal(random.randrange(200, 500))/100))
    pg.moveTo(post_button)

    time.sleep(int(decimal.Decimal(random.randrange(200, 500))/100))
    pg.click()

    time.sleep(int(decimal.Decimal(random.randrange(200, 500))/100))
    pg.typewrite(paste_data)

    time.sleep(int(decimal.Decimal(random.randrange(200, 500))/100))
    pg.moveTo(post)

    time.sleep(int(decimal.Decimal(random.randrange(200, 500))/100))
    pg.click()

    time.sleep(int(decimal.Decimal(random.randrange(200, 500))/100))
    pg.moveTo(close_window)

    time.sleep(int(decimal.Decimal(random.randrange(200, 500))/100))
    pg.click()