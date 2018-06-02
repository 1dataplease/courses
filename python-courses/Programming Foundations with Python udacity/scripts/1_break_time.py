import time
import webbrowser

num_breaks = input("How many breaks do you want to take today? ")
break_period = 8*60*60/2
break_count = 0

print("This program started on " + time.ctime())
while break_count < num_breaks:
    time.sleep(break_period)
    webbrowser.open("google.com")
    break_count +=1

