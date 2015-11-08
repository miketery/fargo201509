#!/usr/bin/python

#import cgi
#import cgitb
import json
from pprint import pprint
from shapely.geometry import shape, Point, Polygon, mapping
from shapely.ops import cascaded_union

import sys
reload(sys)
sys.setdefaultencoding('utf8')

with open('files.txt','r') as f:
	files=json.load(f)
#print("Content-Type: text/html")
#print

#cgitb.enable()

#form = cgi.FieldStorage()

#import pdb
#pdb.set_trace()


with open("parcelData/380170003001.geojson","r") as f:
	data=json.load(f)
data["features"]=0
featuresChange=[]

with open("topAcres.txt","r") as f:
	owners=json.load(f)

with open("files.txt","r") as f:
	files=json.load(f)

ownersParcels=[0 for i in range(len(owners))]


for file in files:
	pprint(file)
	with open("parcelData/"+file+".geojson","r") as file:
		parcels=json.load(file)
		for feature in parcels["features"]:
			for i in range(len(owners)):
				if owners[i] == feature["properties"]["Owner1"]:
					ownersParcels[i]=feature
for i in range(len(owners)):
	with open("topAcres/"+owners[i]+".geojson","w") as f:
		data["features"]=ownersParcels[i]
		json.dump(data,f)
		data["features"]=0

exit()


for file in files:
	print(file)
	with open("parcelData/"+file+".geojson","r") as parcelFile:
		parcels=json.load(parcelFile)
		for feature in parcels["features"]:
			for newFeature in changes:
				if newFeature["attributes"]["GISPIN"] == feature["properties"]["GISPIN"]:
					if newFeature["attributes"]["Owner1"] != feature["properties"]["Owner1"]:
						featuresChange.append(feature)
						break
	with open("changed/c"+file+".geojson","w") as wf:
		data["features"]=featuresChange
		json.dump(data,wf)
		featuresChange=[]
exit()

with open("NDparcels.geojson","w") as f:
	data["features"]=featuresND
	json.dump(data,f)
with open("MNparcels.geojson","w") as f:
	data["features"]=featuresMN
	json.dump(data,f)
with open("OutOfStateParcels.geojson","w") as f:
	data["features"]=featuresOther
	json.dump(data,f)

exit()



