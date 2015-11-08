#!/usr/bin/python

import json
import requests
from pprint import pprint
from shapely.geometry import mapping, shape, Point
from geojson import Polygon

import sys
reload(sys)

with open("data/files.txt","r") as f:
	data=json.load(f)

data.sort()


for num in range(len(data)):
	print(str(num)+"\t"+data[num])
