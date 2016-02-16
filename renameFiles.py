import os

'''
print os.path.realpath(__file__)
print os.path.dirname(os.path.abspath(__file__))
print __file__
'''
original_delimeter = '.'
new_delimeter = ' '
files = os.listdir(os.getcwd())

for file in files:
    #This is the script file executing
    if file == __file__:
        print 'Skip this file'
        continue
    if original_delimeter == '.':    
        found = file.split(original_delimeter)
        
        if len(found) > 2:
            max = len(found) - 2
        else:
            max = 0
        new_file = file.replace(original_delimeter, new_delimeter, max)
    else:
        new_file = file.replace(original_delimeter, new_delimeter)    
    os.rename(file, new_file)
    print new_file
    