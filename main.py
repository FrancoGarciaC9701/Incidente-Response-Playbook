from src.playbook import IncidentResponsePlaybook
from src.virustotal import ThreatEnrichment
from src.notification import NotificationService
from src.splunk_logger import SplunkLogger
from src.soar_integration import SplunkSOAR

def main():
    playbook = IncidentResponsePlaybook()
    playbook.run()
    # Instanciar los servicios
    enrichment_service = ThreatEnrichment("YOUR_VIRUSTOTAL_API_KEY")
    notification_service = NotificationService("your_email@gmail.com", "your_password")
    splunk_logger = SplunkLogger("YOUR_SPLUNK_URL", "YOUR_SPLUNK_TOKEN")
    soar_integration = SplunkSOAR("YOUR_SOAR_URL", "YOUR_SOAR_TOKEN")

    # Ejemplo de uso de los servicios
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

if __name__ == "__main__":
    main()
