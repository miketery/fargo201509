#!/usr/bin/python

import json
import requests
import pprint

def getDetails(ids):
    url='http://gis.cityoffargo.com/arcgis/rest/services/Basemap/FargoParcels/MapServer/0/query'
    params={'f':'json',
            'where':'(1=1) AND ( 1443292602558=1443292602558 )',
            'returnGeometry':'true',
            'spatialRel':'esriSpatialRelIntersects',
            'objectIds':ids,
            'outFields':'*',
            'outSR':'102100'}
    r = requests.get(url,params=params)
    #print(r.url)
    #print(r)
    #print(r.content)
    #return
    out = json.loads(r.text)
    #print(out)
    return out

    

def gisGetIds(geo):
    url='http://gis.cityoffargo.com/arcgis/rest/services/Basemap/FargoParcels/MapServer/0/query'
    params= {'f':'json',
            'returnIdsOnly':'true',
            'where':'',
            'returnGeometry':'false',
            'geometry':geo,
            'geometryType':'esriGeometryPolygon',
            'inSR': '102100',
            'outSR': '102100'}
    r = requests.get(url,params=params)
    out=json.loads(r.text)
    return out['objectIds']

geo = '{"rings":[[[-10785446.805073708,5926026.066610649],[-10785676.116158564,5925854.083297009],[-10785657.006901491,5925873.19255408],[-10785485.02358785,5926102.503638934],[-10785313.040274208,5926331.81472379],[-10784739.762562072,5926828.655407643],[-10784166.484849934,5927172.622034926],[-10783383.005310012,5927325.496091496],[-10782503.979484733,5927249.059063211],[-10781854.26474431,5927096.185006641],[-10781128.112975601,5926542.016551574],[-10780784.146348318,5925949.629582365],[-10780726.818577105,5925070.603757086],[-10780726.818577105,5924439.998273734],[-10780803.25560539,5923274.333592387],[-10780975.23891903,5921994.013368612],[-10781491.188859956,5921000.332000906],[-10781796.936973097,5920656.365373624],[-10782427.542456448,5920694.583887766],[-10784166.484849934,5921038.550515048],[-10784949.964389855,5921573.609713044],[-10785561.460616136,5922414.41702418],[-10785580.569873206,5922567.2910807505],[-10785580.569873206,5922911.257708033],[-10785580.569873206,5923503.644677242],[-10785465.914330779,5924554.653816162],[-10785446.805073708,5925815.864782866],[-10785446.805073708,5926026.066610649]]],"spatialReference":{"wkid":102100,"latestWkid":3857}}'

parcelIds = gisGetIds(geo)
#parcelIds=[18687139,18687138]
data = getDetails(",".join(str(v) for v in parcelIds[0:2])) #171 is limit
pprint.pprint(data)
#getDetails(",".join(str(v) for v in parcelIds[172:272]))
#print(parcelIds)

