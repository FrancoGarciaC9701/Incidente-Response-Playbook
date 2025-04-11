import requests
import json

class SplunkSOAR:
    def __init__(self, soar_url, soar_token):
        self.soar_url = soar_url
        self.soar_token = soar_token

    def create_case(self, case_data):
        headers = {
            'Authorization': f'Bearer {self.soar_token}',
            'Content-Type': 'application/json',
        }
        
        url = f"{self.soar_url}/rest/case"
        data = json.dumps(case_data)
        response = requests.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            print("Caso creado en Splunk SOAR.")
        else:
            print(f"Error al crear el caso en Splunk SOAR: {response.status_code}")
