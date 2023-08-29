import pyautogui as pg
import time

chat = "*Aplikasi di instal SMS Notifikasi*"
count = int(input("Berapa Kali => "))
time.sleep(5)
for i in range(count):
    pg.write(chat)
    pg.press("enter")
