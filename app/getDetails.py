#!/usr/bin/python

import json
import requests
import pprint
from shapely.geometry import shape, Point, Polygon, mapping
from shapely.ops import cascaded_union

def getDetails(ids,fields):
    url='http://gis.cityoffargo.com/arcgis/rest/services/Basemap/FargoParcels/MapServer/0/query'
    params={'f':'json',
            'where':'(1=1) AND ( 1443292602558=1443292602558 )',
            'returnGeometry':'true',
            'spatialRel':'esriSpatialRelIntersects',
            'objectIds':ids,
            'outFields':fields,
            'outSR':'102100'}
    r = requests.get(url,params=params)
    #print(r.url)
    print(r)
    #print(r.content)
    #return
    out = json.loads(r.text)
    #print(out)
    return out

with open('arcGISids.json','r') as file:
	parcelIds=json.load(file)

fields="ACRES,SOURCE,GISPIN,ParcelNo,Owner1,Owner2,BldgSF,LandValue,BldgValue,TotalValue,AptUnits,Type,UseCode,LandUseDesignation,SegSqFt,BlockLegal,A4SF"
with open('20151108arcGIoutput.json','w') as f:
	print(len(parcelIds))
	for i in range(40):
		s=i*150
		e=s+150
		data = getDetails(",".join(str(v) for v in parcelIds[s:e]),fields) #171 is limit
		json.dump(data["features"],f)

pprint.pprint(data.keys())
pprint.pprint(data["features"][0]["attributes"])

