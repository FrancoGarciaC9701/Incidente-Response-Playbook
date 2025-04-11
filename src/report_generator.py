import json
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, incident_data):
        print("Generando reporte de incidente...")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/reporte_incidente_{timestamp}.json"

        with open(filename, "w") as report_file:
            json.dump(incident_data, report_file, indent=4)

        print(f"Reporte generado: {filename}")
