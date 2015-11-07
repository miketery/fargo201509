#!/usr/bin/python

import json
import requests
import pprint
from shapely.geometry import mapping, shape, Point
from geojson import Polygon

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class GeoThing(object):
	def __init__(self,d):
		self.__geo_interface__=d

blocks="data/fargoCensus.geojson"

parcelsFile="../fargoparcels/FargoParcels.geojson"
#parcelsFile="single.parcel"

with open(blocks, 'r') as f:
	data = json.load(f)

blocks=[]
for feature in data['features']:
	#thing=GeoThing(feature['geometry'])
	#polygon=mapping(thing)
	blocks.append(feature)

with open(parcelsFile, 'r') as f:
	feature = json.load(f)

for feature in data['features']:
	#thing=GeoThing(feature['geometry'])
	#poly=mapping(thing)
	#print poly
	parcel=shape(feature['geometry'])
	point=parcel.representative_point()
	for block in blocks:
		polygon=shape(block['geometry'])
		if polygon.contains(point):
			print block['properties']
			break

