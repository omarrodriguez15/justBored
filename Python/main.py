import FileStuff

#FileStuff.ListFiles('Test')

#FileStuff.ListDirectories('Test')

# List directories recursively
#FileStuff.ListDirectories('Test', True)

tot = FileStuff.ListAllFiles('../../jackalWeb/', True)
print 'Total lines: ' + str(tot)
#FileStuff.ReadFile('config.js')