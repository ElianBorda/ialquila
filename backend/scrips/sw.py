import requests
import re
import json
from bs4 import BeautifulSoup

url = "https://www.properati.com.ar/s/bernal/departamento/alquiler"

response = requests.get(url)

ruta_archivo_json = "./datasw.json"

data = []

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ejemplo: Extraer todos los títulos de las etiquetas h2
    tarjetas = soup.find_all('div', class_='listing')
    
    for tarjeta in tarjetas:
        infoTarjeta = (tarjeta.find('div', class_='listing-card__information')).find('div', class_='listing-card__information-main')
        
        titulo = infoTarjeta.find('div', class_='listing-card__title').text
        precio = (infoTarjeta.find('div', class_='listing-card__price-wrapper')).find('div', class_='price').text
        preciolimpio = float(precio.replace('$ ', '').replace('USD ', '').replace('.', ''))
        
        precio_cambio = re.sub(r'[\d,]+', '', precio).replace('.', ''). replace(' ','')
        
        data.append({"titulo": titulo, "cambio": precio_cambio, "precio": preciolimpio})  
        
else:
    print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")
    
with open(ruta_archivo_json, 'w') as archivo_json:
    json.dump(data, archivo_json, indent=2)