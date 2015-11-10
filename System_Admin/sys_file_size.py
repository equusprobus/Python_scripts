'''
Use:
Input an absolute path as a root directory, then it will: 
- print this directory;
- check the total size with du;
- check the total size with df;
- get the top n largest files under this directory;
- get all the group ids under this directory;
- print the sub-directories that you have no read permission (so you cannot visit those files).

Author: equusprobus
Version: 1.0 (November 10, 2015)   
''' 

#%%
import os
import sys
import re
#cwd = os.getcwd()
#print cwd

arg = sys.argv[1]
print '\nThe directory to check: \n\t', arg

#%%
cmd = 'du -hs {0}'.format(str(arg))
fp = os.popen(cmd)
res = fp.read()
print "\nTotal size with du: \n\t", res
fp.close()


cmd = 'df -h | grep {0}'.format(str(arg))
fp = os.popen(cmd)
res = fp.read()
print "Total size with df: \n\t", res
fp.close()


#%%
sizes = []
group_ids = set()
dir_no_permission = set()
#arg = '/fmacdata/utility/eromm4'
#arg = 'C:\Xingliang\Python'

for (dirname, dirs, files) in os.walk(arg):
    #skip .snapshot    
    if bool(re.search('.snapshot', dirname)):
        continue
    
    for j in range(len(files)):
        thefile = os.path.join(dirname, files[j])
        if os.path.islink(thefile):
            continue
        try: 
            size = float(os.path.getsize(thefile))/1024/1024/1024
            statinfo = os.stat(thefile)
            user_id = statinfo[4]
            group_ids.add(statinfo[5])
            tub = (size, user_id, thefile)
            sizes.append(tub)
        except OSError:
            dir_no_permission.add(dirname)
            continue
            
#%%
#sizes.sort(key=lambda tub: tub[0], reverse=True)
sizes.sort(reverse=True)

n=100
print '\nTop {0} largest files are:'.format(n)
for j in range(min(n, len(sizes))):
    t = sizes[j]
    print '\t', str(round(t[0],1))+'G\t', t[1], '\t', t[2]

total_size = sum([p[0] for p in sizes])
print "\nTotal size: \t", str(round(total_size, 1)) + 'G'

print '\nGroup IDs are:'
for gid in group_ids:
    print '\t', gid

print '\nDirectories with no read permission:'
for directory in dir_no_permission:
    print directory
