'''
 QUITO
==============
'''
import couchdb
import sys
import urllib2
import json
import textblob
from pylab import *
import re
from couchdb import view

pais=sys.argv[1]


paises={
    'esp':'http://localhost:5984/espana/_design/dEspana/_view/mun_01JUL_en',
    'rus_jn30':'',
    'cro':'http://localhost:5984/croacia/_design/croacia/_view/text_croacia_up',
    'dim':'http://localhost:5984/dinamarca/_design/text_en/_view/dina',
    'rus_jl14':'',
    'bel':'http://localhost:5984/belgica/_design/belgicavista/_view/belgicavista',
    'eng':'http://localhost:5984/inglaterra/_design/text/_view/ingla',
    'rus_jl15':'',
    'fran':'http://localhost:5984/francia/_design/dFrancia/_view/mundial_30Jun',
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



URL = 'localhost'
db_name = 'england'
patron = re.compile('^[a-zA-Z 0-9,.;#@\'\"&?$%()-+!]*$')


#url = 'http://localhost:5984/inglaterrat/_design/eur/_view/ingtrat'
url=paises[pais]
req = urllib2.Request(url)
print req

f = urllib2.urlopen(req)

d = json.loads(f.read())

archivo = open("{}.csv".format(nombres_paises[pais]),"a") #opens file with name of "test.txt"
cont_positives = 0
cont_negatives = 0
cont_neutrals = 0
cont_total = 0

class info():
    def __init__(self,texto,label):
        self.texto=texto    
        self.label=label
    def __str__(self):
        return '{},{}'.format(self.texto,self.label)

for x in d['rows']:

    a = x['value']
    if patron.match(a):
        texto_tweet = textblob.TextBlob(a)

        aux = ''
        inf=None
        if texto_tweet.sentiment.polarity > 0:
            aux = a + '::positive\n'
            cont_positives = cont_positives + 1
        elif texto_tweet.sentiment.polarity < 0:
            aux = a + '::negative\n'
            cont_negatives = cont_negatives + 1
        else:
            aux = a + '::neutral\n'
            cont_neutrals = cont_neutrals + 1

        archivo.write(aux.encode("utf-8"))
        cont_total = cont_total + 1

archivo.close()

print ("total: " + str(cont_total))
print ("positives: " + str(cont_positives))
print ("negatives: " + str(cont_negatives))
print ("neutrals: " + str(cont_neutrals))



# make a square figure and axesfigure(1, figsize=(8,8))# tamanio de figura
ax = axes([0, 0, 0.9, 0.9])# donde esta la figura ancho alto etc..
#----------------------------------------------------------------------
labels = 'Positivos ', 'Negativos', 'Neutrales '#nomre de los datos
fracs = [cont_positives,cont_negatives,cont_neutrals]#datos a graficar
#----------------------------------------------------------------------
explode=(0, 0.1, 0)#exposicion de uno de los datos segun donde se encuentra
#tipo de grafico(datos,exposicion, titulos de los datos, nose,sombras true o false
pie(fracs, explode=explode,labels=labels, autopct='%10.0f%%', shadow=True)
legend()
title('Evaluacion de Sentimientos del pais: {}'.format(nombres_paises[pais]), bbox={'facecolor':'0.8', 'pad':5})

savefig("tweets_sentiments_{}.png".format(nombres_paises[pais]))
show()#mostrar grafico
f.close()

