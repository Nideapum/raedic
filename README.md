# raedic
Definiciones obtenidas de la [Real Academia Española - RAE](https://dle.rae.es).

# Requisitos
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

## python
```python
pip install beautifulsoup4
pip install request
```

### shell (otra opción)
```shell
apt install python3-bs4
```

# Repositorio
Clonamos el repositorio.
```shell
git clone https://github.com/Alaralan/raedic
```


# Línea de comandos
Desde línea de comandos podemos buscar una o varias palabras ejecutando:
```python3
python3 raedic.py palabra1 palabra2
```


# Desde otro fichero python
Para Incluirlo en nuestro script de python3 solo necesitaremos el script "raedic.py":
```python
import raedic

## La función devuelve una lista.
for line in raedic.BuscarPalabra("palabra")
	print(line)
```
