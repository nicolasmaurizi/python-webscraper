import requests
from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Solo la primera vez nltk.download('punkt') nltk.download('stopwords')

def analizar_pagina(url):
    print(f"\nAnalizando: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza error si no hay 200
    except Exception as e:
        print(f"Error al acceder a la URL: {e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    titulo = soup.title.string.strip() if soup.title else "Sin título"
    imagenes = soup.find_all('img')
    links = soup.find_all('a')
    parrafos = soup.find_all('p')

    # Texto limpio para análisis de palabras
    texto = ' '.join([p.get_text() for p in parrafos])
    palabras = word_tokenize(texto.lower())
    stop_words = set(stopwords.words('spanish') + stopwords.words('english'))

    palabras_filtradas = [w for w in palabras if w.isalnum() and w not in stop_words]
    palabras_comunes = Counter(palabras_filtradas).most_common(10)

    # Resultados
    print(f"\nTítulo de la página: {titulo}")
    print(f"Número de imágenes: {len(imagenes)}")
    print(f"Número de enlaces: {len(links)}")
    print(f"Número de párrafos: {len(parrafos)}")
    print("\nPalabras más frecuentes:")
    for palabra, freq in palabras_comunes:
        print(f" - {palabra}: {freq} veces")

if __name__ == "__main__":
    url = input("Ingresá la URL de la página a analizar: ")
    analizar_pagina(url)
