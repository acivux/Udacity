__author__ = 'jannie'

import webbrowser
import time


for counter in range(0, 3):
    time.sleep(10)
    print "Break", counter, time.ctime()
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
