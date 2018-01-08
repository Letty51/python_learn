import time
import webbrowser

count = 0
while (count < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/")
    count = count + 1

