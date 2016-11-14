import os

def ListFiles(dir):
   files = os.listdir(dir)
   for file in files:
      print file

def ListDirectories(dir, recursive = False, buffer = []):
   skip_dot_files = True
   files = os.listdir(dir)
   directories = []

   for file in files:
      if skip_dot_files and file.startswith('.'):
         continue

      if os.path.isdir(os.path.join(dir, file)):
         directories.append(file)
   
   for file in directories:
      buffer.append(file)
      if recursive:
         ListDirectories(os.path.join(dir, file), True, buffer)
         buffer = []
   
   for index, buffedFile in enumerate(buffer):
      print buffedFile

def ListAllFiles(dir, recursive = False, ext = '.cs', count = 0):
   skip_dot_files = True
   files = os.listdir(dir)
   for file in files:
      if skip_dot_files and file.startswith('.'):
         continue
      if os.path.isdir(os.path.join(dir, file)):
         if recursive:
            count = ListAllFiles(os.path.join(dir, file), True, ext, count)
      elif file.endswith(ext):
         #print file
         count += ReadFile(os.path.join(dir, file))
   return count

def ReadFile(filename):
   with open(filename) as f:
      lines = f.readlines()
   count = 0
   for line in lines:
      count += 1
      #print line
   return count