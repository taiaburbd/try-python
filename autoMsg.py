import random
import pyautogui as pg
import time
words=('Python learner','Python For Beginners','Try python')
time.sleep(8)

for i in range(100):
    a=random.choice(words )
    pg.write(a)
    pg.press('enter')