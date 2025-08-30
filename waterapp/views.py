from django.shortcuts import render
import requests
from bs4 import BeautifulSoup 


# Create your views here.
class WeatherScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        titulo = soup.find('h1').text
        imgs = [img['src'] for img in soup.find_all(class_='simbW')]
        d = [day.text for day in soup.find_all(class_='text-0')]
        fecha = [day.text for day in soup.find_all(class_='subtitle-m')]
        days = [day.text for day in soup.find_all(class_='day_col')]
        combined = list(zip(imgs, days, d, fecha))

        return {
            'titulo': titulo,
            'combined': combined,
        }

ZONE_URLS = {
    'santiago': "https://www.meteored.cl/tiempo-en_Santiago+de+Chile-America+Sur-Chile-Region+Metropolitana+de+Santiago-SCEL-1-18578.html",
    'concepción': "https://www.meteored.cl/tiempo-en_Concepcion-America+Sur-Chile-Biobio-SCIE-1-18576.html",
    'temuco': 'https://www.meteored.cl/tiempo-en_Temuco-America+Sur-Chile-Araucania-SCTC-1-18267.html',
    'chillan':'https://www.meteored.cl/tiempo-en_Chillan-America+Sur-Chile-Biobio--1-18264.html',
    'talca': 'https://www.meteored.cl/tiempo-en_Talca-America+Sur-Chile-Maule--1-18263.html',
    'los angeles': 'https://www.meteored.cl/tiempo-en_Los+Angeles-America+Sur-Chile-Biobio--1-18571.html',
    'viña del mar': 'https://www.meteored.cl/tiempo-en_Vina+del+Mar-America+Sur-Chile-Valparaiso--1-18260.html',
    'valdivia': 'https://www.meteored.cl/tiempo-en_Valdivia-America+Sur-Chile-Los+Lagos--1-18266.html',
    'puerto montt': 'https://www.meteored.cl/tiempo-en_Puerto+Montt-America+Sur-Chile-Los+Lagos-SCTE-1-18567.html',
    'rancagua': 'https://www.meteored.cl/tiempo-en_Rancagua-America+Sur-Chile-Libertador+General+Bernardo+O+Higgins--1-18259.html',
    'osorno': 'https://www.meteored.cl/tiempo-en_Osorno-America+Sur-Chile-Los+Lagos-SCJO-1-18258.html',
    'valparaiso': 'https://www.meteored.cl/tiempo-en_Valparaiso-America+Sur-Chile-Valparaiso--1-18577.html',
    'la serena': 'https://www.meteored.cl/tiempo-en_La+Serena-America+Sur-Chile-Coquimbo-SCSE-1-18575.html',
    'pucon': 'https://www.meteored.cl/tiempo-en_Pucon-America+Sur-Chile-Araucania-SCPC-1-18050.html',
    'curico': 'https://www.meteored.cl/tiempo-en_Curico-America+Sur-Chile-Maule--1-18574.html',
    'molina': 'https://www.meteored.cl/tiempo-en_Molina-America+Sur-Chile-Maule--1-18207.html',
    'linares': 'https://www.meteored.cl/tiempo-en_Linares-America+Sur-Chile-Maule--1-18208.html',
    'villarica': 'https://www.meteored.cl/tiempo-en_Villarrica-America+Sur-Chile-Araucania--1-18204.html',
    'puerto varas': 'https://www.meteored.cl/tiempo-en_Puerto+Varas-America+Sur-Chile-Los+Lagos--1-18190.html',
    'castro': 'https://www.meteored.cl/tiempo-en_Castro-America+Sur-Chile-Los+Lagos--1-18183.html',
    'san fernando':'https://www.meteored.cl/tiempo-en_San+Fernando-America+Sur-Chile-Libertador+General+Bernardo+O+Higgins--1-18242.html',
}

def clima_view(request):
    context = {}
    
    if request.method == 'POST':
        zona = request.POST.get('zona')
        if zona in ZONE_URLS:
            scraper = WeatherScraper(ZONE_URLS[zona])
            context = scraper.scrape()

    return render(request, 'plantillas/response.html', context)