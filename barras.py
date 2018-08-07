'''
 QUITO
==============
'''
import couchdb
import sys
import urllib2
import json
from couchdb import view
from threading import Thread
import time
URL = 'localhost'


partido=sys.argv[1]
operacion=sys.argv[2]

#Diccionario con las vistas por horas
horas={
	'esp-rus':{'esp':'http://localhost:5984/espana/_design/dEspana/_view/01JUL_hora','rus':'http://localhost:5984/rusia/_design/dRusia/_view/01JUL_hora','rus':'http://localhost:5984/rusia/_design/dRusia/_view/01JUL_hora'},
	'cro-dim':{'cro':'http://localhost:5984/croacia/_design/croacia/_view/hora_01JUL','dim':'http://localhost:5984/dinamarca/_design/dDin/_view/hora_01JUL','rus':'http://localhost:5984/rusia/_design/dRusia/_view/01JUL_hora'},
	'bel-eng':{'bel':'http://localhost:5984/belgica/_design/dBelgica/_view/hora_14JUL','eng':'http://localhost:5984/inglaterra/_design/dIngla/_view/14JUL_hora','rus':'http://localhost:5984/rusia/_design/dRusia/_view/hora_14JUL'},
	'fran-cro':{'fran':'http://localhost:5984/francia/_design/dFrancia/_view/mundial_30Jun','cro':'http://localhost:5984/croacia/_design/croacia/_view/15JUL_hora','rus':'http://localhost:5984/rusia/_design/dRusia/_view/15JUL_hora'},	
}

#Diccionario de vistas por idiomas
idiomas={
	'esp-rus':{'esp':'http://localhost:5984/espana/_design/dEspana/_view/01JUL_idioma','rus':'http://localhost:5984/rusia/_design/dRusia/_view/01JUL_idioma','rus':'http://localhost:5984/rusia/_design/dRusia/_view/01JUL_idioma'},
	'cro-dim':{'cro':'http://localhost:5984/croacia/_design/croacia/_view/idioma','dim':'http://localhost:5984/dinamarca/_design/dDin/_view/01JUL_idioma','rus':'http://localhost:5984/rusia/_design/dRusia/_view/01JUL_idioma'},
	'bel-eng':{'bel':'http://localhost:5984/belgica/_design/dBelgica/_view/14JUL_idioma','eng':'http://localhost:5984/inglaterra/_design/dIngla/_view/14JUL_idioma','rus':'http://localhost:5984/rusia/_design/dRusia/_view/14JUL_idioma'},
	'fran-cro':{'fran':'http://localhost:5984/francia/_design/dFrancia/_view/15JUL_idioma','cro':'http://localhost:5984/croacia/_design/croacia/_view/15JUL_idioma','rus':'http://localhost:5984/rusia/_design/dRusia/_view/15JUL_idioma'},
}


Diccionario={}
if 'lang' in operacion:
	Diccionario=idiomas
if 'horas' in operacion:
	Diccionario=horas


def get_jon():
	tuppURL=[]
	tuppURL.append(Diccionario[partido][partido.split("-")[0]])
	tuppURL.append(Diccionario[partido][partido.split("-")[1]])
	tuppURL.append(Diccionario[partido]['rus'])
	tuppJSON=[]
	for url in tuppURL:
		req = urllib2.Request(url)
		f = urllib2.urlopen(req)
		tuppJSON.append(json.loads(f.read()))
	return tuppJSON



def reducir(a):
	valor_actual=a[0][0]
	total=0
	lista_reduce=[]
	for v in a:
		if v[0] == valor_actual:
			total=total+1
		else:
			
			lista_reduce.append((valor_actual,total))
			valor_actual=v[0]
			total=1
	lista_reduce.append((valor_actual,total))
	return lista_reduce


def generar_grafico(lista_reduce_paises):
	plt=None
	import matplotlib.pyplot as plt
	import numpy as np
	nombre1=None
	nombre2=None

	if 'cro' in partido.split("-")[0]:
		nombre1  = 'Croacia'
	if 'esp' in partido.split("-")[0]:
		nombre1  = 'Spain'
	if 'eng' in partido.split("-")[0]:
		nombre1  = 'Inglaterra'
	if 'rus' in partido.split("-")[1]:
		nombre2  = 'Rusia'
	if 'dim' in partido.split("-")[1]:
		nombre2  = 'Dinamarca'
	if 'bel' in partido.split("-")[1]:
		nombre2  = 'Belgica'
	
	"""
	nombre1  = 'Croacia' if 'cro' in partido.split("-")[0] else 'Spain' if 'esp' in partido.split("-")[0] else 'Inglaterra'
	
	nombre2 = 'Rusia'   if 'rus' in partido.split("-")[1] else 'Dinamarca' if 'dim' in partido.split("-")[0] else 'Belgica'
	"""

	horas1 = [ i[0] for i in lista_reduce_paises[0] ]
	score1 = [ i[1] for i in lista_reduce_paises[0] ]


	horas2 = [ i[0] for i in lista_reduce_paises[1] ]
	score2 = [ i[1] for i in lista_reduce_paises[1] ]

	x_pos1 = np.arange(len(horas1))
	x_pos2 = np.arange(len(horas2))

	horas3 = [ i[0] for i in lista_reduce_paises[2] ]
	score3 = [ i[1] for i in lista_reduce_paises[2] ]


	x_pos3 = np.arange(len(horas3))

	slope1, intercept1 = np.polyfit(x_pos1, score1, 1)
	slope2, intercept2 = np.polyfit(x_pos2, score2, 1)
	slope3, intercept3 = np.polyfit(x_pos3, score3, 1)

	trendline1 = intercept1 + (slope1 * x_pos1)
	trendline2 = intercept2 + (slope2 * x_pos2)
	trendline3 = intercept3 + (slope3 * x_pos3)

	plt.subplot(221)
	plt.title('Partido: {} vs {}'.format(nombre1,nombre2))
   
	plt.bar(x_pos1, score1,align='center')
	plt.xticks(x_pos1, horas1) 
	plt.ylabel('Tweets')
	plt.xlabel('{}'.format(nombre1))

	plt.subplot(222)
 
	plt.bar(x_pos2, score2,align='center',color='green')
	plt.xticks(x_pos2, horas2) 
	plt.ylabel('Tweets')
	plt.xlabel('{}'.format(nombre2))
	

	plt.subplot(223)
   
	plt.bar(x_pos3, score3,align='center',color='green')
	plt.xticks(x_pos3, horas3) 
	plt.ylabel('Tweets')
	plt.xlabel('Rusia')
	plt.show()

def calcular(jsons):
	lista_map=[]
	mapear=lambda a: (a,1)
	for x in jsons['rows']:
		a = x['key']
		lista_map.append(mapear(a))

	lista_reduce=reducir(lista_map)
	lista_reduce.sort(key=lambda x: x[1], reverse=True)
	return lista_reduce




lista_jsons=get_jon()
lista_reduce_paises=[]
for j in lista_jsons:
	lista_reduce_paises.append(calcular(j))
print "Lista reduce de las horas:"
print lista_reduce_paises[0]
print lista_reduce_paises[1]
print lista_reduce_paises[2]


generar_grafico(lista_reduce_paises)
