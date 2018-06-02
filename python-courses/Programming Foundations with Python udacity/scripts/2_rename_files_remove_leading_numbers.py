import os
def rename_files():
    # Get file names from the folder
    filelist = os.listdir(r"C:\Users\wainman\Desktop\tw\classes\py foundation\rename")
    print(filelist)
    #saves wd, temp uses dir with files in it, sets the wd back after loop    
    saved_path = os.getcwd()
    print("Current working directory is: " + saved_path)
    os.chdir(r"C:\Users\wainman\Desktop\tw\classes\py foundation\rename")
    for filename in filelist:
        print ("Old name: " + filename)
        print ("New name: " + filename.translate(None, "0123456789"))
        os.rename(filename, filename.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()