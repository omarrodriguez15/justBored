import os
characters_to_delete = 3
files = os.listdir(os.getcwd())

for file in files:
    #This is the script file executing
    if file == __file__:
        print 'Skip this file'
        continue
        
    new_file = file[:characters_to_delete]   
    os.rename(file, new_file)
    print new_file
    