# raedic
Definiciones obtenidas de la [Real Academia Española - RAE](https://dle.rae.es).


# Requisitos
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)

## shell
```shell
apt install python3-bs4
```
### python
```python
pip install beautifulsoup4
pip install request
```

# Repositorio
Clonamos el repositorio.
```
git clone https://github.com/Alaralan/raedic
```


# Línea de comandos
Desde línea de comandos podemos buscar una o varias palabras ejecutando:
```python3
python3 raedic.py palabra1 palabra2
```


# Desde otro fichero python
Para Incluirlo en nuestro script de python3 solo necesitaremos el script "raedic.py":
```
import raedic
```

** La función devuelve una lista. **
```
for line in raedic.BuscarPalabra("palabra")
	print(line)
```
