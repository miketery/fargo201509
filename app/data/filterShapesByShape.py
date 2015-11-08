#!/usr/bin/python

import json
import pprint
from shapely.geometry import shape, Point, Polygon, mapping
from shapely.ops import cascaded_union

import sys
reload(sys)
sys.setdefaultencoding('utf8')

if len(sys.argv) < 4:
    print "Please input arguments for input, filter, and output file"
    exit()


with open(sys.argv[2], 'r') as f:
    filterFile = json.load(f)

filterShapes=[]

for feature in filterFile['features']:
	filterShapes.append([feature['properties']['GEOID'],shape(feature['geometry'])])
	#if feature['properties']['CITYNAME']=='FARGO CITY':
	#	filterShape=shape(feature['geometry'])
	#	break
		

#filterShape=cascaded_union(filterShapes)

filtered=[]

with open(sys.argv[1], 'r') as f:
	inputFile = json.load(f)	

output=[[] for i in range(len(filterShapes))]

for feature in inputFile['features']:
	point=shape(feature['geometry']).representative_point()
	for i in range(len(output)):
		if filterShapes[i][1].contains(point):
			output[i].append(feature)
			break

inputFile['features']=[]


for i in range(len(output)):
	with open(filterShapes[i][0]+".geojson",'w') as outputFile:
		inputFile['features']=output[i]
		json.dump(inputFile,outputFile)
