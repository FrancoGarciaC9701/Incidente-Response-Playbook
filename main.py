import json
import os
from datetime import datetime

from src.playbook import IncidentResponsePlaybook
from src.virustotal import ThreatEnrichment
from src.notification import NotificationService
from src.splunk_logger import SplunkLogger
from src.soar_integration import SplunkSOAR

def export_report_to_json(data):
    # Crear carpeta de reportes si no existe
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    # Pedir al usuario el nombre del archivo
    user_input = input("Ingrese el nombre para el reporte JSON (dejar en blanco para usar nombre automático): ").strip()

    if not user_input:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"incident_report_{timestamp}.json"
    else:
        filename = f"{user_input}.json"

    full_path = os.path.join(reports_dir, filename)

    with open(full_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"[+] Reporte JSON generado: {full_path}")

def main():
    playbook = IncidentResponsePlaybook()
    playbook.run()

    # Instanciar los servicios
    enrichment_service = ThreatEnrichment("YOUR_VIRUSTOTAL_API_KEY")
    notification_service = NotificationService("your_email@gmail.com", "your_password")
    splunk_logger = SplunkLogger("YOUR_SPLUNK_URL", "YOUR_SPLUNK_TOKEN")
    soar_integration = SplunkSOAR("YOUR_SOAR_URL", "YOUR_SOAR_TOKEN")

    # Datos ficticios de ejemplo para el reporte
    report_data = {
        "incident": "Phishing detectado",
        "details": {
            "email_sospechoso": "example@example.com",
            "IOC_enriquecido": enrichment_service.enrich_ioc("some_file_hash"),
            "notificacion": "Enviada",
            "splunk": "Incidente registrado",
            "soar": "Caso creado"
        }
    }

    # Enriquecimiento de un IOC
    enrichment_service.enrich_ioc("some_file_hash")

    # Enviar notificación por correo
    notification_service.send_notification("recipient@example.com", "Alerta de incidente", "Detalles del incidente")

    # Registrar incidente en Splunk
    incident_data = {"tipo": "Phishing", "email_sospechoso": "example@example.com"}
    splunk_logger.log_incident(incident_data)

    # Crear un caso en Splunk SOAR
    case_data = {"type": "Phishing", "status": "Nuevo"}
    soar_integration.create_case(case_data)

    # Exportar el reporte JSON automáticamente
    export_report_to_json(report_data)

if __name__ == "__main__":
    main()
