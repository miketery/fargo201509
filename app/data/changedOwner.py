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

sampleFile=0

with open("parcelData/380170003001.geojson","r") as f:
	data=json.load(f)
data["features"]=0
featuresChange=[]
filesa=["380170103031", "380170101072", "380170009041", "380170009042", "380170103052", 
"380170103062", "380170002023", "380170009015", "380170003003", "380170101082", 
"380170008023", "380170009043", "380170001003", "380170010021", "380170010022", 
"380170007002", "380170008013", "380170103071", "380170006001", 
"380170103061", "380170009012", "380170009014", "380170008014", "380170005022", 
"380170009032", "380170008021", "380170006002", "380170101062", "380170008024", 
"380170101071", "380170009011", "380170002021", "380170005011", "380170002013", 
"380170004004", "380170010013", "380170103033", "380170002011", "380170003001", 
"380170101061", "380170002022", "380170009013", "380170005013", "380170005014", 
"380170006004", "380170010011", "380170008012", "380170008022", "380170103034", 
"380170004003", "380170101091", "380170002012", "380170009031", "380170005012", 
"380170008025", "380170001002", "380170001004", "380170103032", "380170004002", 
"380170001001", "380170103051", "380170010012", "380170007001", "380170009033", 
"380170005021", "380170006003", "380170003002", "380170004001"]

files=[v for v in filesa[55:65]]

with open("parcelData/20151108arcGIoutput.geojson","r") as f:
	changes=json.load(f)

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



