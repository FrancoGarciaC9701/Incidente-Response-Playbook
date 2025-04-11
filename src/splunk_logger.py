import requests
import json

class SplunkLogger:
    def __init__(self, splunk_url, splunk_token):
        self.splunk_url = splunk_url
        self.splunk_token = splunk_token

    def log_incident(self, incident_data):
        headers = {
            'Authorization': f'Splunk {self.splunk_token}',
            'Content-Type': 'application/json',
        }
        
        data = json.dumps(incident_data)
        response = requests.post(self.splunk_url, headers=headers, data=data)
        
        if response.status_code == 200:
            print("Incidente registrado en Splunk.")
        else:
            print(f"Error al enviar a Splunk: {response.status_code}")
