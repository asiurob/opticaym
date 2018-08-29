from django.shortcuts import render
from django.http import HttpResponse as hres
import json

def index( req ):
	return hres( 'Aquí irá el INDEX' )



def landing( req ):
	return render( req, 'Crawler/landing.html')



def crawl( req ):
	return render( req, 'Crawler/crawl.html' );


def crawlit( self, req ):
	res = {}

	automail = req.POST['automail']
	multiple = req.POST['multiple']
	value = req.POST['value']
	mails = req.POST['mails']

	if multiple is True and value == '':
		res['success'] = False
		res['message'] = 'Debe haber etiquetas de búsqueda si la casilla de Búsqueda por etiquetas está marcada'
		res['data'] = None
	else:
		res['success'] = True
		res['message'] = 'Se envió correctamente la instrucción de búsqueda'
		res['data'] = None

	return hres( json.dumps( res ) )