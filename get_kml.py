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
    'esp':'http://localhost:5984/espana/_design/dEspana/_view/coord',
    'rus':'http://localhost:5984/rusia/_design/dRusia/_view/coord',
    'cro':'http://localhost:5984/croacia/_design/croacia/_view/coord',
    'dim':'http://localhost:5984/dinamarca/_design/dDin/_view/coo',
    'bel':'http://localhost:5984/belgica/_design/dBelgica/_view/coord',
    'eng':'http://localhost:5984/inglaterra/_design/dIngla/_view/coord',
    'fran':'http://localhost:5984/francia/_design/dFrancia/_view/coord',
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
