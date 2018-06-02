#reads text in a document, scans it for curse words, advises if yes or no
#1 - choose a file, import it, read through it
#2 - for loop, check every word in it against a file or list of swears

print "Please select the text file to check for profanity"
def filter(text_file):

    # import textfile -> convert textfile to a list
    txtf = open(text_file, 'r')
    text_list = txtf.readlines()

    # loop thru text, if text is in swear list, stop loop, return 'warning'
    word=0
    for word in text_list:
        for swear in swear_list:
            if word in swear:
                print "Warning: Swear word " + word + " in file"
            else:
                print "No swear words detected."
                
    
    txtf.close()



filter(r"C:\Desktop\tw\classes\1 py foundation\2c - use classes - profanity editor\quotes.txt")

#notes
#open returns an object of the file type it reads
#brad is an object or instance of class turtle
# quotes = open(file_location) - quotes is an object of a file
# open is calling an __init__() fxn
# wdyl.com/profanity?q=shot
