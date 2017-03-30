import os
import re

#arg = sys.argv[1]
arg = 'C:\XX\XXX'

output_file = open(r'C:\XXXX\xxx.txt', "w")

for (dirname, dirs, files) in os.walk(arg):
  if bool(re.search('XXX', dirname)):
      continue
  for j in range(len(files)):
    thefile = os.path.join(dirname, files[j])
    
    if os.path.islink(thefile):
      continue
    try:
      input_file=open(file, "r")
      lines = input_file.readlines()
      input_file.close()
      output_file.write("\n# {0}{1}\n".format(dirname[10:], files[j]))
      for x in lines:
        output_file.write("{0} ".format(x))
    except OSError: 
      continue
      
output_file.close()
