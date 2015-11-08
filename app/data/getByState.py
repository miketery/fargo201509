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
states ="NOT ND,MN"

featuresOther=[]
featuresND=[]
featuresMN=[]
sampleFile=0

with open("parcelData/380170003001.geojson","r") as f:
	data=json.load(f)

for file in files:
	with open("parcelData/"+file+".geojson","r") as parcelFile:
		parcels=json.load(parcelFile)
		for feature in parcels["features"]:
			if feature["properties"]["MailSt"] == "ND":
				featuresND.append(feature)
			elif feature["properties"]["MailSt"] == "MN":
				featuresMN.append(feature)
			else:
				featuresOther.append(feature)

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



