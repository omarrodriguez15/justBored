import FileStuff

#FileStuff.ListFiles('Test')

#FileStuff.ListDirectories('Test')

# List directories recursively
#FileStuff.ListDirectories('Test', True)

tot = FileStuff.ListAllFiles('../../../../Projects/StockYou', True)
print 'Total lines: ' + str(tot)
#FileStuff.ReadFile('config.js')