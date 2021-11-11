# -*- coding: utf-8 -*-
# ■ IMPORTS ■
from bs4 import BeautifulSoup
import requests, sys
# ■ FUNCTIONS ■
def BuscarPalabra(arg1):
	"""
	Busca una palabra en el diccionario de la RAE.

	Args:
	· (str)		Palabra a buscar

	Returns
	· (list)	Resultado de la búsqueda.

		Nota:
			list[0]						-- Cabecera
			list[len(list)]		-- Píe
	"""
	msg=[]
	msg.clear()
	web='https://dle.rae.es/{}'.format(arg1.lower())
	headers={
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
		#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
		#'referer':'https://dlr.rae.es'
	}

	try:
		_web_=requests.get(web, headers=headers)
		soup=BeautifulSoup(_web_.text, 'html.parser')
		if _web_.status_code==200:
			msg=[soup.find('header',{'class': 'f'}).get_text()]
			msg.append("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
			for resultado in soup.find('article').find_all('p'):
				if resultado.find('abbr')==None and resultado.find('a',{'class':'a'})==None:
					msg.append("\n■ "+resultado.get_text())
				elif resultado.find('a',{'class':'a'})==None:
					msg.append("· "+resultado.get_text())
			msg.append("───────────────\n"+web)
		else:
			print("❌ [{}] Error obteniendo la URL: {}".format(_web_.status_code, web))
	except:
		msg.append("❌ Error")

	return msg
# ■ MAIN ■
if __name__ == "__main__":
	if len(sys.argv) > 1:
		# Recorre los parámetros introducidos por línea de comandos.
		msg=""
		for i in range(1,len(sys.argv)):
			# "──────────────────────────────\n"
			# Genera el mensaje con los resultados.
			result=BuscarPalabra(sys.argv[i])
			if len(result)>0:
				for j in result and len(result)>0:
					msg+=j+"\n"
				print(msg)
	else:
		sys.exit("❌ Debe introducir una palabra a buscar.")
