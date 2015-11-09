#%%
import os
#path="C:\Xingliang\Python\update_first"
path="C:\Xingliang\Python\update_last"
os.chdir(path)

files = os.listdir(path)
files
len(files)

#%% test
files[1]
input_file = open(files[1], "r")
lines = input_file.readlines()
input_file.close()

print "\n print file", files[1], "\n"

for x in lines:
    print(x)

print("All done!")

#%% read & write
output_file = open("C:\Xingliang\Python\update_last_all.txt", "w")

for j in range(len(files)):
    input_file = open(files[j], "r")
    lines = input_file.readlines()
    input_file.close()
    print "\n print file", j, "\n"
    output_file.write("# {0}\n".format(files[j]))
    for x in lines:
        output_file.write("{0} ".format(x))
    
output_file.close()
