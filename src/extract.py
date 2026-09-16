import requests

class Extract:
    def __init__(self):
        pass

    def pnadc(self):
        url = "https://servicodados.ibge.gov.br/api/v3/agregados/4093/periodos/201201-202602/variaveis/4093|4099?localidades=N3[26]&classificacao=2[all]"
        r = requests.get(url)
        data = r.json()
        return data