#%%
import os
import sys
#cwd = os.getcwd()
#print cwd

arg = sys.argv[1]
print '\n Directory: ', arg

#%%
sizes = []
group_ids = set()
#arg = 'C:\Xingliang\Python'

for (dirname, dirs, files) in os.walk(arg):
    for j in range(len(files)):
        thefile = os.path.join(dirname, files[j])
        if os.path.islink(thefile):
            continue
        size = float(os.path.getsize(thefile))/1024/1024/1024
        statinfo = os.stat(thefile)
        user_id = statinfo[4]
        group_ids.add(statinfo[5])
        tub = (size, user_id, thefile)
        sizes.append(tub)
#        print tub
            
#%%
sizes.sort(key=lambda tub: tub[0], reverse=True)

print '\n Top 20 largest files are: \n'
for j in range(min(20, len(sizes))):
    t = sizes[j]
    print str(round(t[0],1))+'G', t[1], t[2]

print '\n group IDs are: \n'
for gid in group_ids:
    print gid
