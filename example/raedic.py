# ■ IMPORTS ■
from bs4 import BeautifulSoup
import requests, sys
# ■ FUNCTIONS ■
def BuscarPalabra(arg1):
	"""
	Busca una palabra en el diccionario de la RAE.
	
	Args:
		arg1 (str): Palabra a buscar
	
	Returns:
		list: Resultado de la búsqueda.
		
		Nota:
			list[0]						-- Cabecera
			list[len(list)]		-- Píe
	"""
	msg=[]
	msg.clear()
	web='https://dle.rae.es/{}'.format(arg1.lower())
	try:
		_web_=requests.get(web)
		soup=BeautifulSoup(_web_.text, 'html.parser')
		if _web_.status_code==200:
			msg=[soup.find('header',{'class': 'f'}).get_text()+"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"]
			for resultado in soup.find('article').find_all('p'):
				if resultado.find('abbr')==None and resultado.find('a',{'class':'a'})==None:
					msg.append("\n■ "+resultado.get_text())
				elif resultado.find('a',{'class':'a'})==None:
					msg.append("· "+resultado.get_text())
		msg.append("▬      ▬      ▬      ▬      ▬\n"+web)
	except:
		msg.append("❌ Error")
	
	return msg
# ■ MAIN ■
if __name__ == "__main__":
	if len(sys.argv) > 1:
		# Recorre los parámetros introducidos por línea de comandos.
		for i in range(1,len(sys.argv)):
			msg=""
			# "──────────────────────────────\n"
			# Genera el mensaje con los resultados.
			for j in BuscarPalabra(sys.argv[i]):
				msg+=j+"\n"
			print(msg)
	else:
		print("❌ Debe introducir una palabra a buscar.")
