//texto
function(doc){
	var str=doc.created_at;
	var date=str.substring(4,10);
	var txt=String(doc.text);
	//Esta lista puede variar de acuerdo al pais
	var lista_hashtag= ["FIFAWorldCup","wordcup","WordCup","World","WORLDCUP","World2018","WORLDCUP18","Russia2018","FIFA","go england","ENG","Russia","BELENG","England","football"];
	var es_mundial=false;
	for (i=0;i<lista_hashtag.length;i++) {
		if (txt.indexOf(lista_hashtag[i]) >= 0){
  			es_mundial=true;
  			break;
  		}
	}

	if (es_mundial){
		if(date=='Jul 14' && doc.lang=='en'){
			date=str.substring(11,13)
        	emit(date,doc.text);
  		}
	}
	

}
//Hora
function(doc){
	var str=doc.created_at;
	var date=str.substring(4,10);
	var hora=str.substring(11,13);
	var txt=String(doc.text);
	if(date=='Jul 14'){
        	emit(hora,doc.text);
	}
}

//idioma
function(doc){
	var str=doc.created_at;
	var date=str.substring(4,10);
	var txt=String(doc.text);
	if (date=='Jul 14'){
        	emit(doc.lang);
	}
}
//coordenadas
function(doc) {
 emit(doc.user.screen_name,doc.coordinates.coordinates);
}
