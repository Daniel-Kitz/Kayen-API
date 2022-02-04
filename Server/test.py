import glob
import os
from datetime import datetime
# * means all if need specific format then *.csv
allFiles = glob.glob('Backup/*')

listoflists = [[], [], []]
newestFiles = []
datestamps = [[], [], []]

for i in allFiles:
    k = i.lstrip('Backup\\').split('_')
    if (k[0] == 'humid'):
        listoflists[0] += [i]
        datestamps[0].append(datetime.strptime(k[1], '%d-%m-%Y').date())
    elif (k[0] == 'temp'):
        listoflists[1] += [i]
        datestamps[1].append(datetime.strptime(k[1], '%d-%m-%Y').date())
    else:
        listoflists[2] += [i]
        datestamps[2].append(datetime.strptime(k[1], '%d-%m-%Y').date())

print(listoflists)

for i in datestamps:
    newestFiles.append(max(i))
for i in range(len(newestFiles)):
    newestFiles[i] = datetime.strftime(newestFiles[i], '%d-%m-%Y')

print(newestFiles)

for i in allFiles:
    k = i.lstrip('Backup\\')
    for n in newestFiles:
        if n in i:
            newestFiles.append(i)
            newestFiles.remove(n)

print(newestFiles)

latest_file = max(allFiles, key=os.path.getctime)
