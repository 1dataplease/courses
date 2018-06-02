#reads text in a document, scans it for curse words, advises if yes or no
#1 - choose a file, import it, read through it
#2 - for loop, check every word in it against a file or list of swears

import urllib

def read_text():
    quotes = open(r"C:\Desktop\tw\classes\py foundation\2c - use classes - profanity editor\quotes.txt")
    file_contents = quotes.read()
    print(file_contents)
    quotes.close()
    check_profanity(file_contents)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no swear words!")
    else:
        print("Could not scan the file properly")


read_text()

#1 - download their text doc
#2 - download twilio and use that twilio.com/docs/python/install
# twilio.com/signup/verify
#3 - answer 3 questions in assignemnt 4
