import requests

class ThreatEnrichment:
    def __init__(self, api_key):
        self.api_key = api_key

    def enrich_ioc(self, ioc):
        url = f"https://www.virustotal.com/api/v3/files/{ioc}"  # Para hashes de archivos
        headers = {
            "x-apikey": self.api_key
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                print(f"Enriquecimiento de IOC {ioc}:")
                print(f"Reputación: {data['data']['attributes']['last_analysis_stats']}")
                return data
            else:
                print("No se pudo enriquecer el IOC.")
        else:
            print(f"Error al conectar con VirusTotal: {response.status_code}")
            return None
