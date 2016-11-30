import os
import sys

def check_files(dir, password, counter):
   files = filter(lambda f: not f.startswith('.'), os.listdir(dir))

   for file in files:
      filePath = os.path.abspath(os.path.join(dir, file))
      
      with open(filePath) as f:
         lines = f.readlines()

      local_count = 0
      
      for line in lines:
         if local_count == 0:
            print_progress_simple("{0}".format(file))

         if line.find(password) > 0:
            counter += 1
            local_count += 1
            print_progress_simple("File:{0:<25}|  Count:{1:<15}".format(file, local_count))
      
      sys.stdout.write("\r")
      sys.stdout.flush()

      print "File:{0:<25}|  Count:{1:<15}".format(file, local_count)
      
   return counter

def print_progress_simple(msg):
   sys.stdout.write("\r{0}         ".format(msg))
   sys.stdout.flush()

# dir = os.path.expanduser('~/Documents/passwords/files/')
# password = 'password'

if len(sys.argv) > 2:
   dir = os.path.expanduser(sys.argv[1])
   password = sys.argv[2]
   final_count = check_files(dir, password, 0)
   print "Final Count: {0}".format(final_count)
   sys.stdout.write("\n")
else:
   print "\n\n----------------------------------------------------------"
   print "You need to pass in the following two arguments like so:"
   print "----------------------------------------------------------\n"
   print "python {0} <PathToPasswordFiles> <Password>".format(os.path.basename(__file__))
   print "\n----------------------------------------------------------\n"
