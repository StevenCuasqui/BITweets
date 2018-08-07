'''
 QUITO
==============
'''
import couchdb
import sys
import urllib2
import json
from couchdb import view
import simplekml

URL = 'localhost'


pais=sys.argv[1]

#Diccionario con las vistas por coordenadas
paises={
    'esp':'',
    'rus_jn30':'',
    'cro':'',
    'dim':'',
    'rus_jl14':'',
    'bel':'',
    'eng':'',
    'rus_jl15':'',
    'fran':'http://localhost:5984/francia/_design/dFrancia/_view/mundial_30Jun_coord',
    'cro':'',
    'rus':'', 
}


nombres_paises={
    'esp':'Spain',
    'rus_jn30':'Rusia',
    'cro':'Croacia',
    'dim':'Dinamarca',
    'rus_jl14':'Rusia',
    'bel':'Belgica',
    'eng':'Inglaterra',
    'rus_jl15':'Rusia',
    'fran':'Francia',
    'cro':'Croacia',
    'rus':'Rusia',    
}



url=paises[pais]
req = urllib2.Request(url)
f = urllib2.urlopen(req)
j= json.loads(f.read())



kml=simplekml.Kml()

for x in j['rows']:
	a = x['value']
	if a:
		kml.newpoint(coords=[a])

kml.save('kml/{}.kml'.format(nombres_paises[pais]))
