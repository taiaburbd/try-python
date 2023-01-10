import random
import pyautogui as pg
import time
words=('wait dekaitesi','r dekba?','valo hou masud....')
time.sleep(8)

for i in range(100):
    a=random.choice(words )
    pg.write(a)
    pg.press('enter')