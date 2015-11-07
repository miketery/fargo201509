#!/usr/bin/python
# encoding=utf8

import json
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) < 3:
    print "Please input arguments for input and output file"
    exit()

with open(sys.argv[1], 'r') as f:
    data = json.load(f)

feature = data['features'][0]
keys=feature['properties'].keys()

out = open(sys.argv[2],"w")
output = csv.writer(out)
output.writerow(feature['properties'].keys())

i=1
print i
i=i+1
for feature in data['features']:
    output.writerow(feature['properties'].values())
